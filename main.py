import os
import json
from rich.console import Console
from rich.table import Table
import typer
from typing_extensions import Annotated

app = typer.Typer()
console = Console()
tasks: list[str] = []


def print_tasks():
    table = Table("index", "tasks", "state",
                  caption_justify="center", highlight=True)
    with open("todo.md", encoding="UTF-8") as f:
        for x in f:
            line = json.loads(x)
            state: str
            if line["state"]:
                state = "  :white_heavy_check_mark:"
            else:
                state = "  :x:"
            table.add_row(" " + str(line["index"]),
                          line["task"], state)
    console.print(table)


@app.command()
def create():
    repeat_confirmation = True
    while repeat_confirmation:
        task = typer.prompt("Ingresa la tarea que desear agregar")
        if len(tasks) > 0:
            index = tasks[-1]["index"] + 1
        else:
            index = 1
        state = False
        temp = {"index": index, "task": task, "state": state}
        line = json.dumps(temp)
        try:
            with open("todo.md", "a") as f:
                f.write(str(line) + "\n")
            tasks.append(temp)
            console.print("[bold green]Tarea creada con exito![/bold green]")
            repeat_confirmation = typer.confirm(
                "Quieres crear otra tarea?")
        except SystemError:
            raise Exception("Error al crear la tarea")


def update_tasks_file():
    with open("todo.md", "w") as f:
        for x in tasks:
            temp = json.dumps(x)
            f.write(str(temp)+"\n")


@app.command()
def delete():
    print_tasks()
    repeat_confirmation = True
    while repeat_confirmation:
        index = typer.prompt(
            "Escribe el indice de la tarea que quieres eliminar")
        if is_numeric_string(index):
            task = index_exist(int(index))
            if task:
                tasks.pop(task["index"]-1)
                update_tasks_file()
                console.print("[bold green]Lista actializada[/bold green]")
                print_tasks()
                repeat_confirmation = typer.confirm(
                    "Quieres eliminar otra tarea?")
            else:
                console.print(
                    "[bold red]Error el indice ingresado no existe[/bold red]")
        else:
            console.print(
                "[bold red]Error el indice ingresado no es valido[/bold red]")


def index_exist(index: int):
    for x in tasks:
        if x["index"] == index:
            return x
    return None


def is_numeric_string(variable: str | int):
    if isinstance(variable, str):
        return variable.isdigit() or variable.isnumeric()
    return False


@app.command()
def check():
    print_tasks()
    repeat_confirmation = True
    while repeat_confirmation:
        index = typer.prompt(
            "Ingresa el index de la tarea que quieres cambiar de estado")
        if is_numeric_string(index):
            task = index_exist(int(index))
            if task:
                task["state"] = not task["state"]
                tasks[task["index"]-1] = task
                update_tasks_file()
                console.print("[bold green]Lista actializada[/bold green]")
                print_tasks()
                repeat_confirmation = typer.confirm(
                    "Quieres cambiar el estado de otra tarea?")
            else:
                console.print(
                    "[bold red]Error el indice ingresado no existe[/bold red]")
        else:
            console.print(
                "[bold red]Error el indice ingresado no es valido[/bold red]")


@app.command()
def list(
    # task: Annotated[str, typer.Option(help="Tarea que se desea ingresar")],
    # name: Annotated[str | None, typer.Argument()] = None
):
    print_tasks()
    console.print("Para agregar una tarea usa el comando [bold green]create[/bold green]\n" +
                  "Para eliminar una tarea usa el comando [bold red]delete[/bold red]\n" +
                  "Para cambiar el estado de una tarea usa [bold blue]check[/bold blue]\n")


@app.command()
def reset(confirmation: Annotated[bool,
          typer.Option(prompt="Estas seguro de eliminar toda la lista?")]):
    with open("todo.md", "w") as f:
        f.write("")
        console.print("[bold red]Lista eliminada[/bold red]")


if __name__ == '__main__':
    if not os.path.exists("todo.md"):
        with open("todo.md", "x"):
            print("Archivo todo.md creado con exito!")
    else:
        with open("todo.md") as f:
            for x in f:
                line = json.loads(x)
                tasks.append(line)
    app()
