import typer
from models import create_tables
from commands import inventory

app = typer.Typer()
app.add_typer(inventory.app, name="inventory")

        

if __name__ == "__main__":


    
    create_tables()
    app()