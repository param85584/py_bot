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
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')
        def check(m):
            return m.content == 'hello' and m.channel == channel
        users_msg = str(users)
        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.users_msg}!')

        
client.run('ODYwMTE4Mzc5OTY4MjAwNzA0.YN2lqg.QG2ZjeCOG1-D302VgW14e81a1kg ')