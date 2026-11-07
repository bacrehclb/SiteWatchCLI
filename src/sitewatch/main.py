import typer



app = typer.Typer()

@app.command()
def greet(name, times=1):
    for _ in range(times):
        typer.echo(f"Hello {name}!")



if __name__ == "__main__":
    app()