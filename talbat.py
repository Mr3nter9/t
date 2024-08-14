from telethon import TelegramClient
from telethon.sync import TelegramClient, events
import asyncio
import re, requests, os ,json
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest
channel = 'rrcyi'
n=0
client = TelegramClient('m1', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
client.start()
i = 6134236708
json_file = 'dex.json'
mem = []

def load_replied_users():
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            return json.load(f)
    return {}

# وظيفة لحفظ البيانات إلى ملف JSON
def save_replied_user(id, chan):
    replied_users = load_replied_users()
    replied_users[str(id)] = chan
    with open(json_file, 'w') as f:
        json.dump(replied_users, f)

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
    try:
        global n , channel , mem
        if event.is_group:
            if event.message.is_reply:
                original_message = await event.message.get_reply_message()
                if original_message.sender_id == i:
                    id = event.from_id.user_id
                    url = f'https://api.telegram.org/bot6170076995:AAEiU_ATKKzWi1F-G0dxxSZR4vK443GTpGg/getchatmember?chat_id=@{channel}&user_id={id}'
                    req = requests.get(url)
                    if 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
                        try:
                            replied_users = load_replied_users()
                            l2 = event.message.message
                            if "@" in l2:
                                if str(id) in replied_users:
                                    pass
                                else:
                                    nk = re.search(r'@(\w+)(.*)', l2).group(1)
                                    await client(JoinChannelRequest('https://t.me/' + nk))
                                    sleep(3)
                                    await event.reply('تم لا تغادر وتفاعل🙉')
                                    print(f'-{n}')
                                    n += 1
                                    save_replied_user(id, nk)
                            elif "https://t.me/" in l2:
                                if str(id) in replied_users:
                                    pass
                                else:
                                    nk = re.search(r'https://t.me/(\w+)(.*)', l2).group(1)
                                    if 'Preview channel' in requests.get('https://t.me/' + nk).text:
                                        await client(JoinChannelRequest('https://t.me/' + nk))
                                        sleep(3)
                                        await event.reply('تم لا تغادر وتفاعل🙉')
                                        print(f'-{n}')
                                        n += 1
                                        save_replied_user(id, nk)
                            else:
                                if not id in mem:
                                    if str(id) in replied_users:
                                        pass
                                    else:
                                        sleep(3)
                                        await event.reply('دز قناتك')
                                        mem.append(id)
                        except:pass
                    else:
                        sleep(4)
                        await event.reply(f'تبادل ، انضم اول شي @{channel} ودز قناتك، تبادل قنوات فقط')
        elif event.is_private:
            id = event.peer_id.user_id
            url = f'https://api.telegram.org/bot6170076995:AAEiU_ATKKzWi1F-G0dxxSZR4vK443GTpGg/getchatmember?chat_id=@{channel}&user_id={id}'
            req = requests.get(url)
            if 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
                try:
                    replied_users = load_replied_users()
                    l2 = event.message.message
                    if "@" in l2:
                        if str(id) in replied_users:
                            pass
                        else:
                            nk = re.search(r'@(\w+)(.*)', l2).group(1)
                            await client(JoinChannelRequest('https://t.me/' + nk))
                            await event.message.mark_read()
                            sleep(3)
                            await event.reply('تم لا تغادر وتفاعل🙉')
                            print(f'-{n}')
                            n += 1
                            save_replied_user(id, nk)
                    elif "https://t.me/" in l2:
                        if str(id) in replied_users:
                            pass
                        else:
                            nk = re.search(r'https://t.me/(\w+)(.*)', l2).group(1)
                            if 'Preview channel' in requests.get('https://t.me/' + nk).text:
                                await client(JoinChannelRequest('https://t.me/' + nk))
                                await event.message.mark_read()
                                sleep(3)
                                await event.reply('تم لا تغادر وتفاعل🙉')
                                print(f'-{n}')
                                n += 1
                                save_replied_user(id, nk)
                    else:
                        if not id in mem:
                            if str(id) in replied_users:
                                pass
                            else:
                                await event.message.mark_read()
                                sleep(4)
                                await event.reply('دز قناتك')
                                mem.append(id)
                except Exception as er:
                    print(er)
            else:
                if not id in mem:
                    sleep(4)
                    await event.message.mark_read()
                    await event.reply(f'تبادل ، انضم اول شي @{channel} ودز قناتك')
                    mem.append(id)
                    print(mem)
    except :pass




client.run_until_disconnected()
