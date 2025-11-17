# 🎬 Multi-Agent Movie Concept Generator (Google Cloud Technical Series 2025)

🎯 Goal of the Project

To demonstrate:

Agent-to-agent communication

Workflow automation using SequentialAgent

Using tools (functions) to store state, call APIs, and write files

How multi-agent LLM systems can replicate production pipelines (e.g., writing, research, reviews)

📌 Overview
This project is a Multi-Agent Workflow System built using the Google Agent Developer Kit (ADK).
It demonstrates how multiple LLM-powered agents can collaborate in a Sequential Pipeline to generate a complete movie pitch, including:

Research about a historical figure

A screenplay-style plot outline

A titled movie pitch written to a file

This is a real example of agent orchestration, workflow automation, and tool-augmented agents, which are becoming highly valuable in modern AI engineering.

🚀 What This System Does (in simple words)

User says “hello”

Root agent (Greeter) asks: “Tell me a historical figure for the movie.”

When the user gives a name, the system starts a pipeline workflow:

1️⃣ Researcher Agent

Calls the Wikipedia tool (wiki_lookup)

Collects multiple research snippets

Stores info in session.state["research"]

2️⃣ Screenwriter Agent

Reads the research collected

Creates a movie storyline

Saves it inside state (session.state["drafts"])

3️⃣ File Writer Agent

Titles the movie

Writes the movie pitch to a .txt file

Stores the output file path in state

Finally, ADK Dev UI visualizes how agents and tools were executed during the workflow.


🧱 Architecture

1. Root Agent: greeter (LLM Agent)

Welcomes user

Asks for a historical character

Once user responds → triggers the workflow pipeline

Runs until the workflow is complete

2. Workflow Agent: film_concept_team (SequentialAgent)

A pipeline-style agent that forces strict execution order:

researcher → screenwriter → file_writer


Unlike conversational agents, a SequentialAgent does not wait for the user.
It runs each sub-agent automatically, like a backend workflow.

3. Sub-Agents
🕵️ Researcher (LLM Agent + Tools)

Calls wiki_lookup to fetch summaries

Appends results into state["research"]

May call its tool multiple times if required

✍️ Screenwriter (LLM Agent)

Reads accumulated research

Creates a structured movie plot outline

Stores drafts in session state

📁 File Writer (LLM Agent + Tool)

Generates a movie title

Creates a .txt file inside ~/adk_multiagent_systems/movie_pitches

Confirms file creation

<img width="1561" height="565" alt="image" src="https://github.com/user-attachments/assets/736fef39-159c-4c79-a241-943739d3ba99" />


I recently attended the Google Cloud Technical Series 2025, where I had hands-on exposure to Google’s Agent Development Kit (ADK). The sessions were extremely valuable—especially the deep dive into multi-agent architectures, tool integrations, and workflow-driven LLM systems.

As part of the lab, I built a multi-agent system using SequentialAgent, LLM sub-agents, and custom tools that collaborate to research a historical figure, generate a movie concept, and write the final pitch to disk. This project helped me understand real-world patterns like agent orchestration, memory/state management, and tool-powered autonomous workflows.

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/1b21f105-d8d4-4517-b4df-36d64f7bc181" />


<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/3b0a701b-06dc-4a18-9021-0f2ebf7eab0e" />

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/ba942840-b4bb-468f-a17e-c69e90f98534" />
