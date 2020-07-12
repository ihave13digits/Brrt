#!/usr/bin/python3

from discord.ext import commands
from os import path
import json, random
from tools import Data, Misc, Vote, Score
from res import illegal, compliment, banter


TOKEN  = ''

def pre_start_up():
    with open(path.join('res', 'config.json'),"r") as f:
        data = json.loads(f.read())
    
    #print config to log for info purposes
    for key in data:
        print("{}: {}".format(key, data[key]))
    
    TOKEN = data["TOKEN"]
    PREFIX = data["PREFIX"]
    return TOKEN, PREFIX

TOKEN, PREFIX = pre_start_up()
bot = commands.Bot(command_prefix=PREFIX)



### Connect ###
@bot.event
async def on_ready():
    print(f"I'm {bot.user.name}!")

### Message ###

# Needs work

'''
@bot.event
async def on_message(message):
    # Access data
    data = {'author':message.author, 'channel':message.channel, 'content':message.content}
    # Check for plain message
    if not data['content'].startswith("!"):
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
'''


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

@bot.command(name='source')
async def doc_source(ctx, *a):
    if not a:
        response = Misc.source('')
    else:
        response = Misc.source(a[0])
    await ctx.send(response)

@bot.command(name='d')
async def nine_nine(ctx, a:int):
    response = Misc.roll(a)
    await ctx.send(response)

#go to discord developer website make an application select bot from the left side and get the token 
bot.run(TOKEN)
