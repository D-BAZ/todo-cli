import typer
import datetime
from todo_cli.saving import *

app = typer.Typer()


@app.command()
def clear():
    '''
    deletes all tasks 
    '''
    write([])
