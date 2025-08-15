import typer
from todo_cli.list import app as ls_app
from todo_cli.add import app as add_app
from todo_cli.delete import app as delete_app
from todo_cli.clear import app as clear_app
from todo_cli.mark import app as mark_app
from todo_cli.update import app as update_app

app = typer.Typer()

app.add_typer(add_app)
app.add_typer(delete_app)
app.add_typer(ls_app)
app.add_typer(mark_app)
app.add_typer(update_app)
app.add_typer(clear_app)



if __name__ == "__main__":
    '''
    Small todo list app inside your terminal
    My first CLI , have fun ! <3
    '''
    app()