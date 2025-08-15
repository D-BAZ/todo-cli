import typer
from todo_cli.saving import *
import datetime
from rich.console import Console

app = typer.Typer()
err_console = Console(stderr=True)

@app.command()
def mark(id: Annotated[int, typer.Argument(show_default=False)],status:  Annotated[Status, typer.Argument(show_default=False)]):
    '''
    updates the status of task with given id , type mark --help to see option status 
    '''
    tasks = try_read()
    try:
        task = tasks[id]
        task["status"]=status
        task["updatedAt"]= datetime.datetime.now().strftime("%H:%M:%S %A, %B %d, %Y")
        print(f"Task named : \"{task["name"]}\" marked as {str(task["status"].value)}")
        write(tasks)
    except IndexError:
        err_console.print("No task with this id exists")    
    