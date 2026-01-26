# mesh

Multi-agent AI coordination in your terminal.

![demo](demo.gif)

## What is this?

mesh is a terminal-based demo that shows multiple AI agents collaborating on a task together. Instead of one AI doing everything, three specialized agents — Researcher, Planner, and Critic — work together through visible conversation rounds to produce a better result.

This demonstrates **multi-agent coordination**: AI collaboration, not replacement.

## Install

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Anthropic API key to .env
```

## Usage

```bash
python mesh.py "plan a weekend trip to Tokyo"
```

```bash
python mesh.py "compare React vs Svelte for a small project"
```

```bash
python mesh.py "design a morning routine for productivity"
```

## How it works

1. You provide a task as a CLI argument
2. Three agents activate, each with a distinct role:
   - **Researcher** (cyan) — gathers information, surfaces key facts
   - **Planner** (green) — organizes and structures the output
   - **Critic** (yellow) — reviews, finds gaps, suggests improvements
3. Agents take turns in rounds, each seeing the full conversation history
4. An orchestrator decides when the task is sufficiently addressed (or after 10 rounds max)
5. A final consolidated output synthesizes the best of all contributions

## Requirements

- Python 3.11+
- Anthropic API key
