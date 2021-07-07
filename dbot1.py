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
users = SITE.fetch('users/{ids}/notifications', ids=[16357192])


@client.event
async def on_message(message, arg1, arg2):
    '''if arg1 or arg2 is None:
        client.send_message(ctx.message.channel, "=cw <Carte> <Heure>")
    else:'''

        desc = "{}{}".format(arg1,arg2)
        em = discord.Embed(title= users, description=desc, colorsys=0x57FE01)
    
        if message.content == "$msg":
            await message.channel.send(client.get_channel(860120820532510752), embed=em)


client.run('ODYwMTE4Mzc5OTY4MjAwNzA0.YN2lqg.vjGJMNbmlc43a_I7xQUcx6V0J3s')