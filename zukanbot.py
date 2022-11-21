import discord
import random
import os
import json


with open('pokemon.json', encoding='utf-8') as f:
    urls = json.load(f)

print(len(urls))
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    global urls

    weights = [1] * 143 + [1] * 7 + [0.3] + [0.3]

    if message.author.bot:
        return
    if message.content == "<:monb:641248096495599618>" or message.content =="<:monb:1044153325723058186>":
        url = random.choices(list(urls.values()), weights=weights)[0]

        await message.channel.send(url)



        #await message.channel.send(urls["120 ヒトデマン"])



client.run(os.environ["NjM2NTYwMTA4Nzc5ODY0MDk1.GFtfA_.1xfB1x7fJ4tOOKqvhEWf2Z1pJf3uld70MFs-y0"])
