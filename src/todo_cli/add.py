import typer
import datetime
from todo_cli.saving import *

app = typer.Typer()


@app.command()
def add(task_name:  Annotated[str, typer.Argument(show_default=False)]):
    '''
    creates new task 
    '''
    list = try_read()
    list.append({"name": task_name,"status":Status.TODO,"createdAt":datetime.datetime.now().strftime("%H:%M:%S %A, %B %d, %Y"),"updatedAt":datetime.datetime.now().strftime("%H:%M:%S %A, %B %d, %Y")})
    write(list)
    print(f"Task named : \"{task_name}\" under id {len(list)-1} added")
