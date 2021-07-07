import discord
from stackapi import StackAPI
from discord.ext import commands, tasks


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

SITE = StackAPI('stackoverflow')
SITE.key = "v)UC0zDZ3RYnXd2OpNv)sA(("
SITE.access_token = 'zpDjJVUu0yJh2dkVQ7UWyQ))'



#@client.event
async def on_message(message,*, user_data):
    SITE = StackAPI('stackoverflow')
    SITE.key = "v)UC0zDZ3RYnXd2OpNv)sA(("
    SITE.access_token = 'zpDjJVUu0yJh2dkVQ7UWyQ))'

    '''if arg1 or arg2 is None:
        client.send_message(ctx.message.channel, "=cw <Carte> <Heure>")
    else:'''
    if message.content == "$msg":
        users = SITE.fetch('users/{ids}/notifications', ids=[16357192])
        user_data = str(users)
        #em = discord.Embed(title= SITE, description=user_data, color=0xEE8700)
        await message.channel.send(user_data)

'''
@client.event
async def on_message(message, *user_msg):
    if message.content == "$msg":
        users = SITE.fetch('users/{ids}/notifications', ids=[16357192])
        user_msg = str(users)
        await message.send("Data fetch -->" + user_msg)
'''
client.run('ODYwMTE4Mzc5OTY4MjAwNzA0.YN2lqg._bs_fEJE4o3V-7fZiXhbytMfuo0')