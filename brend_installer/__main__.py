import heroku3
from time import time
import random
import requests
from git import Repo
from brend_installer import *
from .bstring import main
import os
from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
#from asyncio import get_event_loop
from .language import LANG, COUNTRY, LANGUAGE, TZ
from rich.prompt import Prompt, Confirm

LANG = LANG['MAIN']

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "brend" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit (connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace("https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app

#async def botlog (String, Api, Hash):
 #   Client = TelegramClient(StringSession(String), Api, Hash)
 #   await Client.start()

 #   KanalId = await Client(CreateChannelRequest(title='⚡️ 𝙱𝚛彡𝚗𝚍 𝙱𝚘𝚝𝚕𝚘𝚐​', about=LANG['AUTO_BOTLOG'], megagroup=True))
 #   KanalId = KanalId.chats[0].id

 #   Photo = await Client.upload_file(file='brendlogo.jpg')
 #   await Client(EditPhotoRequest(channel=KanalId, photo=Photo))
 #   msg = await Client.send_message(KanalId, LANG['DONT_LEAVE'])
 #   await msg.pin()

 #   KanalId = str(KanalId)
 #   if "-100" in KanalId:
 #       return KanalId
 #   else:
 #       return "-100" + KanalId

if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])

    # Telegram Prosesləri #
    onemli(LANG['GETTING_STRING_SESSION'])
    stri, aid, ahash = main()
    basarili(LANG['SUCCESS_STRING'])
    baslangic = time()

    # Heroku Prosesləri #
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    basarili(LANG['SUCCESS_APP'])
    onemli(LANG['DOWNLOADING'])

    #Əkənin varyoxunu sikim peyser ble
    #It is forbidden to copy this code
    if os.path.isdir("./brenduserbot/"):
        rm_r("./brenduserbot/")
    repo = eval('Repo.clone_from("https://github.com/brendsupport/brenduserbot", "./brenduserbot/", branch="master")')
    basarili(LANG['DOWNLOADED'])
    onemli(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()

    onemli(LANG['WRITING_CONFIG'])

    config['API_HASH'] = ahash
    config['API_KEY'] = str(aid)
    config['COUNTRY'] = COUNTRY
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = stri
    config['LANGUAGE'] = LANGUAGE

    basarili(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])

    try:
        app.process_formation()["worker"].scale(1)
    except:
        hata(LANG['ERROR_DYNO'])
        exit(1)

 #   bilgi(LANG['OPENING_BOTLOG'])
 #   KanalId = loop.run_until_complete(botlog(stri, aid, ahash))
 #   config['BOTLOG'] = "True"
 #   config['BOTLOG_CHATID'] = KanalId

 #   basarili(LANG['OPENED_BOTLOG'])
 #   BotLog = True

    basarili(LANG['OPENED_DYNO'])
    basarili(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)

    Sonra = Confirm.ask(f"[bold yellow]{LANG['AFTERDEPLOY']}[/]", default=True)
    if Sonra == True:
        Cevap = ""
        while not Cevap == "3":
            if Cevap == "1":
                config['LOGSPAMMER'] = "True"
                basarili(LANG['SUCCESS_LOG'])
            elif Cevap == "2":
                helpbot = str(soru(LANG['BOT_TOKENI']))
                config['BOT_TOKEN'] = helpbot
                basarili(LANG['BOT_SUCCESFULY'])
                botusername = str(soru(LANG['BOT_USERNAMESI']))
                config['BOT_USERNAME'] = botusername
                basarili(LANG['HELP_BOT_SUCCESFULY'])


            bilgi(f"\[1] {LANG['NO_LOG']}\n\[2] {LANG['HELP_BOT']}\n\[3] {LANG['CLOSE']}")
            
            Cevap = Prompt.ask(f"[bold yellow]{LANG['WHAT_YOU_WANT']}[/]", choices=["1", "2", "3"], default="3")
        basarili("Brend Userbot qurulumu bitdi Görüşənədək!")
