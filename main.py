#Discord.py is currently deprecated. Update before April 2022

import discord
import os
import requests
import json

def get_price():
  response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD')
  #response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  price = str(json_data['bitcoin']['usd'])
  price_response = "Bitcoin's Price is: " + price + " USD"
  return(price_response)

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$btc'):
    price = get_price()
    await message.channel.send(price)
  

client.run(my_secret)
