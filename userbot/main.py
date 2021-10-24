# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

# NeonUserBot
# TheOksigen
# esebj 


import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, NEON_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.qaleriya_sql as QALERIYA_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

DIZCILIK_STR = [
    "**Stickeri əkişdirdim...** 😅",
    "__Sticker paketə əlavə edilir...__ ✨",
    "**Bu sticker artıq mənimdir!** 👀",
    "**Bunu stickerlərimə əlavə etməliyəm...** 🤏🏻",
    "`Sticker həps edilir...` 🥴",
    "`Mən bir sticker oğrusuyam stickerin məndədi ;D!`",
    "**Nə gözəl stickerdi bu!** 😍"
]

KICKMESTR = [
    "**Mənim sahibim {title} qrupunu bəyənmədi və getdi.** 🚶🏻",
    "__Sağ olun! Sahibim buranı tərk etdi. 👀 Sizə xoş söhbətlər.__ ",
    "**Sahibim N Σ O N ilə {title} qrupunu tərk etdi...**",
    "`Sağ-salamat. Mən getdim.` 👋🏻"
    ]

AFKSTR = [
    "__İndi burda deyiləm. Gələndə yazaram.__",
    "**Sahibim burda deyil. Gözlə gələndə yazar.**",
    "`Zəng etdiyiniz şəxsə zəng çatmır. ❌ Telefon ya söndürülüb yada əhatə dairəsi xaricindədir xaiş olunur daha sonra təkrar cəhd edin.`"
    "__Salam mən sahibimin meneceriyəm\nBuyurun istəklərinizi mənə deyə bilərsiz. Sizin üçün sahibimə çatdıraram.__",
    "🔹 **Mən sahibimin xüsusi botuyam!\nO bura gələnə qədər mənimlə tanış ola bilərsiniz.\nSizdə bot istəyirsizsə: @NeonSUP**",
    "`Hal hazırda burdan çoox uzaqdayam. 🙂\nQışqırsan bəlkə eşitdim.`",
    "`Sahibim burada deyil mazqimi xarab eləmə.\nGələndə özünə yazarsan` 😒",
    "__Sahibimə mesaj atmaq üçün zəhmət olmasa aşağıdakıları yazın:__ ⤵️\n🔸 **Adınız:\n🔸 Soyadınız:\n🔸 İsdifadəçi Adınız:**\n\nℹ️ __Əgər yuxarıadakıları düzgün yazdızsa sahibim ən qısa zamanda sizə yazacaq.__",
    "**Göruldü :)**"]

ALIVE_MESAJLAR = [
    "**Sənin sevgilin səni tək qoydu amma mən hər zaman yanındayam.** ❤️",
    "__Heç narahat olma @NeonUserBot Userbot işləyir kef elə. Səni sevirəm__",
    "🎆 **Hay can burdayam! Səni tək qoymaram. @NeonUserBot `userbot işləyir.**",
    "⛈️ **Əlimdən gələnin ən yaxşısını eləməyə hazıram**",
    "✨ `N Σ O N botun sahibinin əmirlərinə hazırdı...`",
    "**Sən bu dəqiqə dunyanın ən panyatkalı UserBotunu işlədirsən.** 😎",
    "`Hay can!` `Məni çağırdın⁉️ Arada imkan ver zoğallı çayımı içim.`",
    "`Hokus Pokus 🔮! Narahat olma buralardayam. Nəsə olsa Fədai gilin PS4 oturmuşam.`",
    "`Mənə zəng eləmişdin ❓ Çayçıdayam oturmuşam birazdan gələcəm`"
]

UNAPPROVED_MSG = ("__Salam__ {mention} __, necəsən?__\n"
    "__Mən__ N Σ O N __UserBotam__ 🙃\n"
    "__Sahibim hal-hazırda burada deyil.__\n"
    "__Mən bildiyim qədəri ilə 🙄 o çox vaxt PM-ləri qəbul edir və mənim sahibim sənə PM atma icazəsi verməyib__ 🤔\n"
    "__Əgər sən yazmağa davam etsən, mən səni əngəlləməyə məcbur qalacam.__ 🥴\n"
    "__Lakin,__ 😔 __məndən incimə bu sahibimin əmridir.__")


DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nXETA: Yazılan telefon nömresi keçersizdir' \
             '\n  Meslehet: Ölke kodundan isdifade etmekle nömreni yazın' \
             '\n       Telefon nömrenizi yeniden yoxlayın.'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komandaları alırıq #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # Neon
            Neonpy = re.search('\"\"\"NeonPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Neonpy == None:
                Neonpy = Neonpy.group(0)
                for Satir in Neonpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin xaricden yüklenmişdir. Her hansı bir açıqlama yoxdur.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    neonbl = requests.get('https://raw.githubusercontent.com/TheOksigen/neon_userbot/main/neonblacklist.json').json()
    if idim in neonbl:
        bot.disconnect()

    # ChromeDriver'ı Ayarlayaq #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Qaleriya üçün deyerler
    QALERIYA = {}

    # PLUGIN MESAJLARINI AYARLAYAQ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MESAJLAR))}", "afk": f"{str(choice(AFKSTR))}", "kickme": f"{str(choice(KICKMESTR))}", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, banlandı!`", "mute": "{mention}`, səssizləşdirildi!`", "approve": "{mention}`, mənə mesaj yazmağın üçün icazə verildi", "disapprove": "{mention}`, artıq mənə yaza bilməssən!`", "block": "{mention}`Bloklandın!🥰"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("Pluginler Yüklenir...")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Onsuzda Yüklənib😌 " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Yükləmə Uğursuz! Plugin xətalıdır❌.\n\nHata: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Zehmet olmasa pluginlerin qalıcı olması üçün PLUGIN_CHANNEL_ID'i ayarlayın.🥸(əgər bilmirsiz sə @NeonSUP qrupuna gelin`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = QALERIYA_SQL.TUM_QALERIYA[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Botunuz işleyir!✅ Hansısa söhbete  .alive yazaraq Test ede bilersiz!👍."
          " Kömeye ehtiyacınız varsa, destek qrupuna gelin: t.me/NeonSup")
LOGS.info(f"Bot versiyası: N Σ O N {NEON_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
