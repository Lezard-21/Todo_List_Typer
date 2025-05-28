import os
import random as ra
import json
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
import typer

app = typer.Typer()
console = Console()
tasks: list[str] = []
current_action: str = "none"


class list_item():
    def __init__(self, task: str):
        self.task = task

    def __str__(self):
        return "{" + f'"task":"{self.task}"' + "}"


def print_tasks():
    table = Table("index", "tasks", "state")
    with open("todo.md", encoding="UTF-8") as f:
        for x in f:
            line = json.loads(x)
            table.add_row(str(line["index"]),
                          line["task"], str(line["state"]))
    console.print(table)


def repeat_question(confirmation: Annotated[bool, typer.Option(
    prompt=f"Qieres {current_action} otra tarea")]
):
    pass


@app.command()
def create():
    repeat_confirmation = True
    while repeat_confirmation:
        task = typer.prompt("Ingresa la tarea que desear agregar")
        index = len(tasks) + 1
        state = False
        temp = {"index": index, "task": task, "state": state}
        line = json.dumps(temp)
        try:
            with open("todo.md", "a") as f:
                f.write(str(line) + "\n")
            tasks.append(line)
            console.print("[bold green]Tarea creada con exito![/bold green]")
            repeat_confirmation = typer.confirm(
                "Quieres crear otra tarea?")
        except SystemError:
            raise Exception("Error al crear la tarea")


def delete():
    pass


@app.command()
def check():
    print_tasks()
    repeat_confirmation = True
    while repeat_confirmation:
        index = typer.prompt(
            "Ingresa el index de la tarea que quieres cambiar de estado")


@app.command()
def list(
    # task: Annotated[str, typer.Option(help="Tarea que se desea ingresar")],
    # name: Annotated[str | None, typer.Argument()] = None
):
    print_tasks()
    console.print("Para agregar una tarea usa el comando [bold green]create[/bold green]\n" +
                  "Para eliminar una tarea usa el comando [bold red]delete[/bold red]\n" +
                  "Para cambiar el estado de una tarea usa [bold blue]check[/bold blue]\n")


if __name__ == '__main__':
    if not os.path.exists("todo.md"):
        with open("todo.md", "x"):
            print("Archivo todo.md creado con exito!")
    else:
        with open("todo.md") as f:
            for x in f:
                line = json.loads(x)
                tasks.append(line)
    # else:
    #     with open("todo.txt") as f:
    #         for x in f:
    #             console.print("[red]"+x+"[/red]")
    app()
