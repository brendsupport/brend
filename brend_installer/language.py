from json import loads
from rich.prompt import Prompt
from . import logo, console, bilgi

def importlang ():
    console.clear()
    logo()
    bilgi("\n\[1] Azərbaycanca\n\[2] Türkcə\n\[3] English")
    Dil = Prompt.ask("[bold yellow]Zəhmət olmasa 1 dil seçin / Please select a language[/]", choices=["1", "2", "3"], default="1")

    if Dil == "1":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "Az"
        TZ = "Asia/Baku"
    elif Dil == "2":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Europe/London"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./brend_installer/language/{LANGUAGE}.brendjson", "r").read())["STRINGS"]
