import typer
from rich.console import Console
from rich.table import Table
from todo_cli.saving import *


app = typer.Typer()

console = Console()

@app.command()
def list(show_to_do : Annotated[bool, typer.Option("--todo", "-t", show_default=False,help="shows only todo ")]=False,
         show_in_progress : Annotated[bool, typer.Option("--in-progress", "-p", show_default=False,help="shows only in progress")]=False,
         show_done: Annotated[bool, typer.Option("--done", "-d", show_default=False,help="shows only in done")]=False):
    '''
    gives a list of all tasks , type list --help to see flags
    '''
    tasks = try_read()
    table = Table("ID","TASK","STATUS","CREATED","UPDATED")
    for i in range(0 , len(tasks)) :
        task = tasks[i]
        if show_to_do and task["status"]== Status.TODO:
            table.add_row(str(i),task["name"],task["status"],task["createdAt"],task["updatedAt"])
        elif show_in_progress and task["status"]== Status.INPROGRESS:
            table.add_row(str(i),task["name"],task["status"],task["createdAt"],task["updatedAt"])
        elif show_done and task["status"]== Status.DONE:
            table.add_row(str(i),task["name"],task["status"],task["createdAt"],task["updatedAt"])
        elif not show_to_do and not show_in_progress and not show_done:
            table.add_row(str(i),task["name"],task["status"],task["createdAt"],task["updatedAt"])     
    console.print(table)