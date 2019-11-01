import discord
import random
import os
print(os.environ)

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    print(message.content)
    if message.author.bot:
        return

    urls = [
        'https://video.twimg.com/ext_tw_video/1187855831120797696/pu/vid/480x270/nKLEosGb1heLdTsO.mp4',
        'https://video.twimg.com/ext_tw_video/1187855984695185408/pu/vid/480x270/qgArYEMw62I1C8EW.mp4',
        'https://video.twimg.com/ext_tw_video/1187857564089741312/pu/vid/480x270/FAhUNtfcRI4_57tf.mp4',
        'https://video.twimg.com/ext_tw_video/1187862525116727296/pu/vid/480x270/3hWWvEOF9XDzOX6O.mp4',
        'https://video.twimg.com/ext_tw_video/1187862625306079232/pu/vid/480x270/qRCwpN6YXYdncVVQ.mp4',
        'https://video.twimg.com/ext_tw_video/1187862705127870464/pu/vid/480x270/8IjqeB_4ZadR9rjk.mp4',
        'https://video.twimg.com/ext_tw_video/1187926073893253120/pu/vid/480x270/HTe4bCU8oy6cHjDe.mp4',
        'https://video.twimg.com/ext_tw_video/1187926195729395712/pu/vid/480x270/TNSMF_sz1s8GwA37.mp4',
        'https://video.twimg.com/ext_tw_video/1187926297244102656/pu/vid/480x270/oYdQCGQ-gIwxnnyG.mp4'

    ]


    if message.content == "<:monb:636725781749301250>":
        number = random.randint(0, 8)
        await message.channel.send(urls[number])

client.run(os.environ["DISCORD_TOKEN"])