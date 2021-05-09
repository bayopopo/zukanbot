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

    weights = [1] * 143 + [0.5] * 7 + [0.3] + [0.1]

    if message.author.bot:
        return
    if message.content == "<:pokeball:657822336510197760>" or message.content == "<:monb:641248096495599618>" or message.content =="<:monb:828193362981027880>" or message.content =="<:pokemon:677029538554839096>" or message.content == "<:monb:840951864127651871>"or message.content == "<:monb:830720172762333236>":
        url = random.choices(list(urls.values()), weights=weights)[0]:
        url = random.choices(list(urls.values()), weights=weights)[0]

        await message.channel.send(url)



        #await message.channel.send(urls["120 ヒトデマン"])



client.run(os.environ["DISCORD_TOKEN"])
