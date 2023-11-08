import discord
from discord.ext import commands
import random
import os
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ファイル 'pokemon.json' のパスを修正
# Replit.comではファイルへの直接のファイルパス指定はサポートされていないため、ファイルをアップロードして使用します
# ファイルをアップロードして、ファイル名を 'pokemon.json' に設定してください
file_path = 'pokemon.json'

with open(file_path, encoding='utf-8') as f:
    urls = json.load(f)

@bot.event
async def on_ready():
    print('ログインしました')

@bot.event
async def on_message(message):
    global urls

    weights = [1] * 143 + [0.5] * 7 + [0.3] + [0.1]

    if message.author.bot:
        return
    if message.content == "<:monb:1171846145698431099>" or message.content == "<:pokeball:641273768957968404>" or message.content =="<:monb:641248096495599618>" or message.content =="<:pokemon:677029538554839096>" or message.content == "<:pokeball:657822336510197760>":
        # random.choice() から random.choices() に変更
        url = random.choices(list(urls.values()), weights=weights, k=1)[0]

        await message.channel.send(url)

my_secret = os.environ['DISCORD_TOKEN']
bot.run(my_secret)
