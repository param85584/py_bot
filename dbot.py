import os
import discord
import random
from stackapi import StackAPI
from discord.ext import commands, tasks
from fetch_notifications import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

response=stack_notify_msg()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'NSO':
        await message.channel.send(response)

client.run(TOKEN)
