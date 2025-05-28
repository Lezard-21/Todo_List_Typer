import os
import random as ra
import json
from typing_extensions import Annotated
from rich.console import Console
import typer

app = typer.Typer()
console = Console()


class list_item():
    def __init__(self, task: str):
        self.task = task

    def __str__(self):
        return "{" + f'"task":"{self.task}"' + "}"


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
    task: Annotated[str, typer.Option(help="Tarea que se desea ingresar")],
    name: Annotated[str | None, typer.Argument()] = None
):
    print("Todo list")
    index = ra.random()
    print(index)
    if not os.path.exists("todo.txt"):
        with open("todo.txt", "x") as f:
            f.write("no existe")
    else:
        with open("todo.txt") as f:
            for x in f:
                console.print("[red]"+x+"[/red]")


if __name__ == '__main__':
    app()
