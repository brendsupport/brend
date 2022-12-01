import os, heroku3, random, requests
from time import time
from git import Repo
from brend_installer import *
from .bstring import main
from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from .language import LANG, LANGUAGE

LANG = LANG['MAIN']

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        xeta(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "brend" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        xeta(LANG['MOST_APP'])
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
        xeta(LANG['ERROR'] + str(e))
    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    ela(LANG['SUCCESS_POSTGRE'])
    return app


if __name__ == "__main__":
    logo(LANGUAGE)
    api = sual(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    ela(LANG['LOGGED'])

    # Telegram Prosesləri #
    vacib(LANG['GETTING_STRING_SESSION'])
    stri = sual("Stringinizi yazın")
    ela(LANG['SUCCESS_STRING'])
    baslangic = time()

    # Heroku Prosesləri #
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    ela(LANG['SUCCESS_APP'])
    vacib(LANG['DOWNLOADING'])

    #Əkənin varyoxunu sikim peyser ble
    #It is forbidden to copy this code
    if os.path.isdir("./brenduserbot/"):
        rm_r("./brenduserbot/")
    repo = eval('Repo.clone_from("https://github.com/brendsupport/brenduserbot", "./brenduserbot/", branch="master")')
    ela(LANG['DOWNLOADED'])
    vacib(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()

    vacib(LANG['WRITING_CONFIG'])

    config['API_HASH'] = ahash
    config['API_KEY'] = str(aid)
    config['COUNTRY'] = COUNTRY
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = stri
    config['LANGUAGE'] = LANGUAGE

    ela(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])

    try:
        app.process_formation()["worker"].scale(1)
    except:
        xeta(LANG['ERROR_DYNO'])
        exit(1)
    ela(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)
