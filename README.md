# Goal-Driven AI Task Agent (Local & Open-Source)

An autonomous AI agent that interprets high-level goals, plans actions, executes tools, and tracks state. **Built entirely with free and open-source tools.**

## Features
 - Goal interpretation and step-by-step planning
 - Autonomous agent loop (plan → act → observe → repeat)
 - Tool-based execution (filesystem + text processing)
 - Persistent memory and state tracking
 - Real artifacts (markdown summaries saved to disk)
 - Safety controls (directory sandboxing, tool whitelisting)
 - Fully local LLM (no paid APIs)

## Example Goal

```text
"Organize my notes and summaries them"

Agent behavior:
    1. Scans a notes directory
    2. Reads text files
    3. Summarizes content using a local LLM
    4. Saves summaries as Markdown files
    5. Terminates autonomously when done
```

## Project Structure
```powershell
ai-text-agent/
|
├── app.py                  # Entry point
├── requirements.txt
│
├── data/
│   ├── notes/              # Input files
│   └── summaries/          # Generated summaries
│
├── src/
│   ├── agent.py            # Agent loop (orchestration)
│   ├── planner.py          # Deterministic planning logic
│   ├── executor.py         # Tool execution
│   ├── tools.py            # Filesystem & text tools
│   ├── memory.py           # Agent state
│
└── README.md
```

## Tech Stack
- Python 3.10+
- Ollama (local LLM runtime)
- Mistral (open-source LLM)
- Standard Python libraries

No Cloud APIs, no paid services.

## Setup Instructions
1. Install Ollama (https://ollama.com)      
    ```bash
    ollama pull mistral
    ```
2. Create virtual environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate # Windows: .venv\Scripts\activate
    ```
3. Install dependencies
    ```bash
    pip install ollama
    ```
4. Run the agent
    ```bash
    python app.py
    ```

## Design Principles
 - Deterministic planning (LLMs do NOT control logic)
 - One-step-at-a-time execution
 - Explicit state management
 - Strict tool boundaries
 - Human-readable outputs

This design avoids common agent failures such as:
- Infinite loops
- Tool halucinations
- Hidden state
- Unsafe file access

## Safety & Control
- Filesystem access restricted to `/data`
- Tool whitelist enforced
- No dynamic code execution
- No uncontrolled loops

## Future Improvements
- Multi-agent collaboration
- LangChain / LangGraph integration
- WebUI

This is a sample line being added here to test the GitHub Actions YML file added in main branch.

This is added to test the Signed Commit Logic.