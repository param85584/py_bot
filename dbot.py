import os
import discord
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

stack_notify_msg=stack_notify_msg()

@client.event
async def on_message(message):
    if message.content.startswith('stack_notification'):
        desc = format(stack_notify_msg)
        embedVar = discord.Embed(title=client.user, description=desc, color=0x00ff00)
        #embedVar.add_field(name="items", value='hi', inline=False)
        #embedVar.add_field(name="page", value='fy', inline=False)
        await message.channel.send(embed=embedVar)

client.run(TOKEN)
