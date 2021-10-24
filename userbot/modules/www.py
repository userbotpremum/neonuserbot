# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Neon  17.03    10.08.2021

from datetime import datetime

#from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("www")

# ████████████████████████████████ #
"""
@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):

    await spd.edit(LANG['SPEED'])
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    result = test.results.dict()

    await spd.edit("`"
                   f"{LANG['STARTED_TIME']}"
                   f"{result['timestamp']} \n\n"
                   f"{LANG['DOWNLOAD_SPEED']}"
                   f"{speed_convert(result['download'])} \n"
                   f"{LANG['UPLOAD_SPEED']}"
                   f"{speed_convert(result['upload'])} \n"
                   "Pinginiz: "
                   f"{result['ping']} \n"
                   f"{LANG['ISP']}"
                   f"{result['client']['isp']}"
                   "`")

"""


@register(outgoing=True, pattern="^.data$")
async def neardc(event):
    """ .dc """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Şəhər : `{result.country}`\n"
                     f"Ən yaxın datacenter : `{result.nearest_dc}`\n"
                     f"İndiki datacenter : `{result.this_dc}`")


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ .ping  """
    start = datetime.now()
    await pong.edit("`Pinginiz!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pinginiz!\n%sms`" % (duration))

CmdHelp('www').add_command(
    'speed', None, 'Bir speedtest tətbiq edər və nəticəni göstərər.'
).add_command(
    'dc', None, 'Serverinizə ən yaxın datacenter\'ı göstərər.'
).add_command(
    'ping', None, 'Botun ping dəyərini göstərər.'
).add_command(
    'data', None, 'Sizə yaxın olan dataceneri göstərər'
).add()

      
