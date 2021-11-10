from json import loads
from rich.prompt import Prompt
from . import logo, console, bilgi

def importlang ():
    console.clear()
    logo()
    bilgi("\n\[1] Azərbaycanca\n\[2] Türkçe")
    Dil = Prompt.ask("[bold yellow]Dil seçin[/]", choices=["1", "2"], default="1")

    if Dil == "1":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "2":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./brend_installer/language/{LANGUAGE}.brendjson", "r").read())["STRINGS"]
