import discord
from discord.ext import commands
import random
import os
import json

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

with open('pokemon.json', encoding='utf-8') as f:
    urls = json.load(f)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    global urls

    weights = [1] * 143 + [0.5] * 7 + [0.3] + [0.1]

    if message.author.bot:
        return
    if message.content == "<:monb:1171846145698431099>" or message.content == "<:pokeball:641273768957968404>" or message.content =="<:monb:641248096495599618>" or message.content =="<:pokemon:677029538554839096>" or message.content == "<:pokeball:657822336510197760>":
        url = random.choice(list(urls.values()), weights=weights)[0]

        await message.channel.send(url)

my_secret = 'YOUR_BOT_TOKEN'
client.run(my_secret)
