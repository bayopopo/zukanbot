import discord
from discord.ext import commands
import random
import os
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

with open('pokemon.json', encoding='utf-8') as f:
    urls = json.load(f)

@bot.event
async def on_ready():
    print('Logged in as', bot.user)

@bot.slash_command(name="pokemon", description="Send a random Pokémon picture")
async def send_random_pokemon(interaction):
    global urls

    weights = [1] * 143 + [0.5] * 7 + [0.3] + [0.1]

    url = random.choice(list(urls.values()), weights=weights)[0]
    await interaction.response.send_message(url)

my_secret = os.getenv('DISCORD_TOKEN')
if my_secret is None:
    print("DISCORD_TOKEN is not set.")
else:
    bot.run(my_secret)

