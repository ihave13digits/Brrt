#!/usr/bin/python3

from discord.ext import commands
from os import path
import json, random
from tools import Data, Misc, Vote, Score
from res import illegal, compliment, banter
import help_com

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

### Help ###

# Override !help
bot.remove_command('help')
@bot.command(name='help')
async def helpBrrt(ctx, *a):
    response=help_com.helper(a)
    await ctx.send(embed=response)



### Documentation ###

@bot.command(name='source')
async def doc_source(ctx, *a):
    '''
    Fetch the git link to src
    '''
    if not a:
        response = Misc.source('')
    else:
        target = str(a[0])
        response = Misc.source(target)
    await ctx.send(response)

@bot.command(name='python')
async def doc_python(ctx, *a):
    '''
    Python Docs
    '''
    if not a:
        response = Misc.python('')
    else:
        target = str(a[0])
        response = Misc.python(target)
    await ctx.send(response)

@bot.command(name='rust')
async def doc_rust(ctx, *a):
    '''
    Rust docs
    '''
    if not a:
        response = Misc.rust('')
    else:
        target = str(a[0])
        response = Misc.rust(target)
    await ctx.send(response)



### Misc. ###

@bot.command(name='broadcast')
async def broadcast(ctx, msg, channel):
    response = msg
    c = channel
    chnl = bot.get_channel(c)
    await chnl.send(response)

@bot.command(name='echo')
async def speak(ctx, *a):
    response = ""
    for word in a:
        response += word + " "
    await ctx.send(response)

@bot.command(name='banter')
async def banterBrrt(ctx, *a):
    '''
    Banter command, accepts (arg)
    '''
    if not a:
        response = random.choice(banter.loose)
    else:
        response = random.choice(banter.focus).format(a[0])
    await ctx.send(response)

@bot.command(name='praise')
async def praiseBrrt(ctx, *a):
    '''
    Praise People or Brrt
    '''
    if not a:
        response = random.choice(compliment.shucks)
    else:
        response = random.choice(compliment.praise).format(a[0])
    await ctx.send(response)

@bot.command(name='d')
async def roll_die(ctx, *a):
    '''
    roll an X sided dice where X is a number <= 1000
    '''
    response = ""
    value = 6
    lmt = 1
    if not a:
        value = 6
        lmt = 1
    else:
        value = a[0]
        if type(value) != int:
            value = 6
        if value <= 1:
            value = 2

        if len(a) > 1:
            lmt = a[1]
        if type(lmt) != int:
            lmt = 1
        if lmt > 20:
            die_choice = ['dies', 'dices']
            word = random.choice(die_choice)
            response = "Brrt only roll 20 {} at a time.\n\n".format(word)
            lmt = 20
        elif lmt < 1:
            lmt = 1
    for rolls in range(lmt):
        response += str(Misc.roll(value))+"\n"
    await ctx.send(response)



bot.run(TOKEN)
