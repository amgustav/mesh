# mesh

Multi-agent AI coordination in your terminal.

![demo](demo.gif)

## What is this?

mesh is a terminal-based demo that shows multiple AI agents collaborating on a task together. Instead of one AI doing everything, three specialized agents — Researcher, Planner, and Critic — work together through visible conversation rounds to produce a better result.

This demonstrates **multi-agent coordination**: AI collaboration, not replacement.

## Project structure

```
mesh/
├── src/
│   ├── __init__.py
│   ├── mesh.py          # CLI entry point
│   ├── agents.py        # Agent definitions
│   ├── orchestrator.py  # Coordination logic
│   └── config.py        # Configuration
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   └── test_orchestrator.py
├── requirements.txt
├── .env.example
└── README.md
```

## Install

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Anthropic API key to .env
```

## Usage

```bash
python3 -m src.mesh "plan a weekend trip to Tokyo"
```

```bash
python3 -m src.mesh "compare React vs Svelte for a small project"
```

```bash
python3 -m src.mesh "design a morning routine for productivity"
```

## Running tests

```bash
python3 -m pytest tests/
```

## How it works

1. You provide a task as a CLI argument
2. Three agents activate, each with a distinct role:
   - **Researcher** (cyan) — gathers information, surfaces key facts
   - **Planner** (green) — organizes and structures the output
   - **Critic** (yellow) — reviews, finds gaps, suggests improvements
3. Agents take turns over 2 rounds, each seeing the full conversation history
4. A final consolidated output synthesizes the best of all contributions

## Requirements

- Python 3.11+
- Anthropic API key
