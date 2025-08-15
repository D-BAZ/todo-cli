import typer
from todo_cli.saving import *
import datetime
from rich.console import Console

app = typer.Typer()
err_console = Console(stderr=True)

@app.command()
def update(id: Annotated[int, typer.Argument(show_default=False)], new_name: Annotated[str, typer.Argument(show_default=False)]):
    '''
    updates the name of task with given id 
    '''
    tasks = try_read()
    try:
        task = tasks[id]
        print(f"Task named : \"{task["name"]}\" renamed as : \"{new_name}\"")
        task["name"] = new_name
        task["updatedAt"]= datetime.datetime.now().strftime("%H:%M:%S %A, %B %d, %Y")
        write(tasks)
    except IndexError:
        err_console.print("No task with this id exists")    