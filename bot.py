#!/usr/bin/python3

import discord, random
from discord.ext import commands
from os import path

from tools import Misc
from res import illegal, compliment, banter

TOKEN  = ''
with open(path.join('res', 'token.txt')) as f:
    TOKEN = f.read().strip()


bot = commands.Bot(command_prefix='!')


### Connect ###

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



### Message ###

#@bot.event
async def on_message(message):
    # Access data
    data = {'author':message.author, 'channel':message.channel, 'content':message.content}
    # Check for offenses
    for word in illegal.words:
        if word in data['content'].lower():
            # Get message context
            ctx = await bot.get_context(message)
            # Scold user
            response = illegal.words[word]['warning'].format(data['author'])
            await ctx.send(response)
            # Remove offense if serious
            if illegal.words[word]['offense'] > 0:
                await message.delete()



### Misc. ###

@bot.command(name='banter')
async def banterBrrt(ctx, *a):
    if not a:
        response = random.choice(banter.loose)
    else:
        response = random.choice(banter.focus).format(a[0])
    await ctx.send(response)

@bot.command(name='praise')
async def praiseBrrt(ctx, *a):
    if not a:
        response = random.choice(compliment.shucks)
    else:
        response = random.choice(compliment.praise).format(a[0])
    await ctx.send(response)

@bot.command(name='python')
async def doc_python(ctx, *a):
    if not a:
        response = Misc.python('')
    else:
        response = Misc.python(a[0])
    await ctx.send(response)

@bot.command(name='rust')
async def doc_rust(ctx, *a):
    if not a:
        response = Misc.rust('')
    else:
        response = Misc.rust(a[0])
    await ctx.send(response)

@bot.command(name='d')
async def nine_nine(ctx, a:int):
    response = Misc.roll(a)
    await ctx.send(response)

#got to discord developer website make an application select bot from the left side and get the token 
bot.run(TOKEN)
