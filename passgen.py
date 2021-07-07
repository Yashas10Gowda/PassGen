from typing import Optional
import typer
import pyperclip
from password import PassWord 

app = typer.Typer(add_completion=False)

def version_callback(called):
    if called:
        version = typer.style('1.0.0',fg=typer.colors.YELLOW,bold=True)
        typer.echo(f'PassGen CLI version: {version}')
        raise typer.Exit()

@app.command()
def passgen(length: int = typer.Option(8,'--length','-l',help="length of password"),
            numbers: bool = typer.Option(True,'--no-numbers','-nn',help="remove numbers",show_default=False),
            symbols: bool = typer.Option(True,'--no-symbols','-ns',help="remove symbols",show_default=False),
            save: bool = typer.Option(False,'--save','-s',help="save password to password.txt",show_default=False),
            version: Optional[bool] = typer.Option(None,'--version','-V',help="version number",show_default=False,callback=version_callback)):
    
    """A Simple Password Generator."""

    password = PassWord(length=length, symbols=symbols, numbers=numbers)
    password = password.generate()
    pyperclip.copy(password)

    starting = typer.style("Generated Password:", fg=typer.colors.CYAN)
    passwording = typer.style(password, fg=typer.colors.GREEN, bold=True)
    ending = typer.style("Password copied to clipboard", fg=typer.colors.YELLOW)
    saving = ''

    if save:
        with open('saved-passwords.txt','a') as f:
            f.write(f'\n{password}')
        saving = typer.style("Password saved to password.txt", fg=typer.colors.GREEN)
        
    typer.echo(f"{starting} {passwording}\n{ending}\n{saving}")

if __name__ == "__main__":
    app()