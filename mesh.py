"""mesh — Multi-agent AI coordination in your terminal."""

import sys

from rich.console import Console

import orchestrator

console = Console()


def main() -> None:
    """Entry point: parse CLI args and run the orchestration loop."""
    if len(sys.argv) < 2:
        console.print("[bold]Usage:[/] python mesh.py [cyan]\"your task here\"[/cyan]")
        console.print()
        console.print("Example:")
        console.print('  python mesh.py "plan a weekend trip to Tokyo"')
        raise SystemExit(1)

    task = " ".join(sys.argv[1:])
    orchestrator.run(task)


if __name__ == "__main__":
    main()
