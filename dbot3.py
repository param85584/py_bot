import discord
from stackapi import StackAPI
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

SITE = StackAPI('stackoverflow')
SITE.key = "access_key"
SITE.access_token = 'access_token'
users = SITE.fetch('users/{ids}/notifications', ids=[16357192])

user_notify_type=[]
for index,value in enumerate(users['items']):
     user_notify_type.append(users['items'][index]['notification_type'])

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        desc = format(user_notify_type)
        embedVar = discord.Embed(title=client.user, description=desc, color=0x00ff00)
        embedVar.add_field(name="items", value='hi', inline=False)
        embedVar.add_field(name="page", value='fy', inline=False)
        await message.channel.send(embed=embedVar)

client.run('token')