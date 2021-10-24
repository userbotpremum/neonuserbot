#Neon UserBot

from userbot import CMD_HELP
from userbot.events import register
from PIL import Image
import io
import os
import asyncio
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("cevir")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.çevir ?(ses|gif|ses)? ?(.*)")
@register(outgoing=True, pattern="^.cevir ?(ses|gif|ses)? ?(.*)")
@register(outgoing=True, pattern="^.convt ?(gif|voice|sound)? ?(.*)")
async def cevir(event):
    islem = event.pattern_match.group(1)
    try:
        if len(islem) < 1:
            await event.edit(
                "**Bilinməyən əmr.** ❌\n**Hazırda olan əmrlər siyahısı:** `ses/gif`"
            )
            return
    except:
        await event.edit(LANG['INVALID_COMMAND'])
        return
    if islem == "ses" or islem == "voice": # -filter_complex "areverse" #
        EFEKTLER = ["ters", "donma", "robot", "earrape", "parazit"]
        # https://www.vacing.com/ffmpeg_audio_filters/index.html #
        KOMUT = {"ters": ' -filter_complex "areverse"', "donma": ' -filter_complex "deesser=i=1:s=e[a];[a]aeval=val(ch)*10:c=same"', "robot": '-filter_complex "afftfilt=real=\'hypot(re,im)*sin(0)\':imag=\'hypot(re,im)*cos(0)\':win_size=512:overlap=0.75"', "earrape": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"', "suretli": "-filter_complex \"rubberband=tempo=1.5\"", "parazit": '-filter_complex "afftfilt=real=\'hypot(re,im)*cos((random(0)*2-1)*2*3.14)\':imag=\'hypot(re,im)*sin((random(1)*2-1)*2*3.14)\':win_size=128:overlap=0.8"', "yangi": "-filter_complex \"aecho=0.8:0.9:500|1000:0.2|0.1\""}
        efekt = event.pattern_match.group(2)

        if len(efekt) < 1:
            await event.edit(LANG['NEED_EFECT'])
            return

        rep_msg = await event.get_reply_message()

        if not event.is_reply or not (rep_msg.voice or rep_msg.audio):
            await event.edit(LANG['NEED_SOUND'])
            return

        await event.edit(LANG['EFECTING'])
        if efekt in EFEKTLER:
            indir = await rep_msg.download_media()
            ses = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' {KOMUT[efekt]} output.mp3")
            await ses.communicate()
            await event.client.send_file(event.chat_id, "output.mp3", reply_to=rep_msg, caption="@NeonUserBot `ilə effekt tətbiq edildi.`")
            
            await event.delete()
            os.remove(indir)
            os.remove("output.mp3")
        else:
            await event.edit(LANG['NOT_FOUND_EFECT'])
    elif islem == "gif":
        rep_msg = await event.get_reply_message()

        if not event.is_reply or (not rep_msg.video) and (not rep_msg.document.mime_type == 'application/x-tgsticker'):
            await event.edit(LANG['NEED_VIDEO'])
            return

        await event.edit(LANG['CONVERTING_TO_GIF'])
        video = io.BytesIO()
        video = await event.client.download_media(rep_msg)
        if rep_msg.document.mime_type == 'application/x-tgsticker':
            print(f"lottie_convert.py '{video}' out.gif")
            gif = await asyncio.create_subprocess_shell(f"lottie_convert.py '{video}' out.gif")
        else:
            gif = await asyncio.create_subprocess_shell(f"ffmpeg -i '{video}' -filter_complex 'fps=20,scale=320:-1:flags=lanczos,split [o1] [o2];[o1] palettegen [p]; [o2] fifo [o3];[o3] [p] paletteuse' out.gif")
        await gif.communicate()
        await event.edit(f"`{LANG['UPLOADING_GIF']}`")

        try:
            await event.client.send_file(event.chat_id, "out.gif",reply_to=rep_msg, caption=LANG['WITH_NEON_GIF'])
        except:
            await event.edit(LANG['ERROR'])
            await event.delete()
            os.remove("out.gif")
            os.remove(video)
        finally:
            await event.delete()
            os.remove("out.gif")
            os.remove(video)
    elif islem == "sound" or islem == "ses":
        rep_msg = await event.get_reply_message()
        if not event.is_reply or not rep_msg.video:
            await event.edit(LANG['NEED_VIDEO'])
            return
        await event.edit(LANG['CONVERTING_TO_SOUND'])
        video = io.BytesIO()
        video = await event.client.download_media(rep_msg.video)
        gif = await asyncio.create_subprocess_shell(f"ffmpeg -vn -sn -dn -i {video} -codec:a libmp3lame -qscale:a 4 out.mp3")
        await gif.communicate()
        await event.edit(LANG['UPLOADING_SOUND'])
        try:
            await event.client.send_file(event.chat_id, "out.mp3",reply_to=rep_msg, caption=LANG['WITH_NEON_SOUND'])
        except:
            await event.edit(LANG['ERROR'])
            await event.delete()
            os.remove("out.mp3")
            os.remove(video)
        finally:
            await event.delete()
            os.remove("out.mp3")
            os.remove(video)

    else:
        await event.edit(LANG['INVALID_COMMAND'])
        return

CmdHelp('cevir').add_command(
    'çevir gif', None, 'Videonu vəya animasyonlu Stickeri GiFə çevirər.'
).add_command(
    'çevir ses', '<donma/robot/earrape/parazit>', 'Səsə efekt verər.'
).add()
