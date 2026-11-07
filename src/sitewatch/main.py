from typer import Typer, echo

app = Typer()

@app.command()
def greet(name: str, times=1):
    for i in range(times):
        echo(f"Hello {name}!")



if __name__ == "__main__":
    app()