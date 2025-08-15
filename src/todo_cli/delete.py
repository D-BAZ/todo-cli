import typer
from todo_cli.saving import *
from rich.console import Console

app = typer.Typer()
err_console = Console(stderr=True)



@app.command()
def delete(id: Annotated[int, typer.Argument(show_default=False)]):
    '''
    deletes task with given id
    '''
    tasks = try_read()
    try:
        print(f"Task named : \"{tasks[id]["name"]}\" deleted")
        tasks.pop(id)
        write(tasks)
    except IndexError:
        err_console.print("No task with this id exists")