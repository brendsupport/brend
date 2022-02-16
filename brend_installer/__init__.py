from rich.console import Console
from rich.panel import Panel
from rich.live_render import LiveRender
import sys
import os, shutil
console = Console()

def xeta (text):
   console.print(text, style="bold red")
def bilgi (text):
   console.print(text, style="blue")
def ela (text):
   console.print(f"[bold green]{text}[/]")
def vacib (text):
   console.print(text, style="bold cyan")
def sual (soru):
   return console.input(f"[bold yellow]{soru}[/]")
def logo (dil = "None"):
   versiya = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold blue]⚡️ 𝙱𝚛彡𝚗𝚍 Installer ⚡️[/]\n\n[bold cyan]Version: [/][i]5.5[/]\n[bold cyan]Python: [/][i]{versiya}[/]\n[bold cyan]Dil: [/][i]{dil}[/]"), justify="center")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]✓ Qurulum bitdi!\n[i]UserBot {round(saniye)} saniyə ərzində quruldu.[/]\n\n[bold green]🕐 Bir dəqiqə sonra telegramda .alive yazaraq yoxlaya bilərsiniz.\nXeyirli olsun, Bizi Seçdiyiniz üçün təşəkkürlər:)[/]"), justify="center")                         
                   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)
