from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.apps import App
from google.adk.tools import ToolContext,exit_loop

import os
import requests
from datetime import datetime

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

# ----------------------------
# TOOL: append_to_state
# ----------------------------
def append_to_state(tool_context: ToolContext, key: str, value: str):
    lst = tool_context.state.get(key, [])
    lst.append(value)
    tool_context.state[key] = lst
    return {"status": "ok"}

# ----------------------------
# TOOL: wiki_lookup
# ----------------------------
def wiki_lookup(tool_context: ToolContext, query: str):
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "%20")
        resp = requests.get(url, timeout=10)
        data = resp.json()
        summary = data.get("extract", "No summary found.")
    except Exception as e:
        summary = f"Error: {e}"

    append_to_state(tool_context, "research", summary)
    return {"summary": summary}

# ----------------------------
# TOOL: write_to_file
# ----------------------------
def write_to_file(tool_context: ToolContext):
    drafts = tool_context.state.get("drafts", [])
    if not drafts:
        return {"status": "no_drafts"}

    final_text = drafts[-1]

    folder = os.path.expanduser("~/adk_multiagent_systems/movie_pitches")
    os.makedirs(folder, exist_ok=True)

    fname = f"pitch_{datetime.now().strftime('%H%M%S')}.txt"
    path = os.path.join(folder, fname)

    with open(path, "w") as f:
        f.write(final_text)

    return {"status": "written", "path": path}

# ----------------------------
# AGENTS
# ----------------------------

researcher = LlmAgent(
    name="researcher",
    model=MODEL,
    instruction="""
    Research the subject using wiki_lookup.
    Each time you find info, call wiki_lookup and then append_to_state with key 'research'.
    """,
    tools=[wiki_lookup, append_to_state]
)

screenwriter = LlmAgent(
    name="screenwriter",
    model=MODEL,
    instruction="""
    Use all items in state['research'] to write a movie outline.
    Store the outline using append_to_state with key 'drafts'.
    """,
    tools=[append_to_state]
)

file_writer = LlmAgent(
    name="file_writer",
    model=MODEL,
    instruction="Write the final movie outline to a file using write_to_file.",
    tools=[write_to_file]
)

film_concept_team = SequentialAgent(
    name="film_concept_team",
    description="Runs researcher → screenwriter → file_writer",
    sub_agents=[researcher, screenwriter, file_writer]
)

greeter = LlmAgent(
    name="greeter",
    model=MODEL,
    instruction="Welcome the user and ask for a historical figure.",
    sub_agents=[film_concept_team]
)

app = App(
    name="workflow_agents",
    root_agent=greeter
)
