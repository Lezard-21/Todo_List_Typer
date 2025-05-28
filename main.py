import os
import random as ra
import json
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
import typer

app = typer.Typer()
console = Console()


class list_item():
    def __init__(self, task: str):
        self.task = task

    def __str__(self):
        return "{" + f'"task":"{self.task}"' + "}"


tasks = []


def print_tasks():
    table = Table("index", "tasks", "state")
    # temp = '{"sadsa":"sadas", "asdasd":23132312, "asdasdsa":"qwewqeqw"}'
    with open("todo.md", encoding="UTF-8") as f:
        for x in f:
            line = json.loads(x)
            # console.print_json(data=line)
            table.add_row(line["index"], line["tascks"], str(line["state"]))
    console.print(table)


@app.command()
def create():
    pass


@app.command()
def delete():
    pass


@app.command()
def check():
    pass


@app.command()
def list(
    # task: Annotated[str, typer.Option(help="Tarea que se desea ingresar")],
    # name: Annotated[str | None, typer.Argument()] = None
):
    # index = ra.random()
    print_tasks()


if __name__ == '__main__':
    if not os.path.exists("todo.md"):
        with open("todo.md", "x") as f:
            f.write("")
    # else:
    #     with open("todo.txt") as f:
    #         for x in f:
    #             console.print("[red]"+x+"[/red]")
    app()
