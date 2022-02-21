#Discord.py is currently deprecated. Update before April 2022

import discord
import os

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(my_secret)
