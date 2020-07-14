#!/usr/bin/python3

import json, random
from discord.ext import commands
from discord import Embed, utils
from os import path
from tools import Data, Misc, Vote, Score
from res import illegal, compliment, banter, help_com

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
bot_data = {
        'dir' : 'test.data',
        'owners' : ['ihave13digits', 'AbleTheAbove'],
        'member_points' : {}
        }



def helper(a, mode):
    color_choice = Misc.rand_hex()
    embed=Embed(title="Brrt {}".format(mode).upper(), url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=color_choice)
    if mode == "api":
        target = help_com.api_dict
    if mode == "docs":
        target = help_com.docs_dict
    if mode == "help":
        target = help_com.help_dict
    try:
        embed.add_field(name=a[0], value=target[a[0]], inline=False)
    except:
        for x in target:
            embed.add_field(name=x, value=target[x], inline=False)
    
    embed.set_footer(text="Brrt ||")
    return embed



### Connect ###
@bot.event
async def on_ready():
    global bot_data
    print("Brrt needs to get ready!")
    D = Data()
    p = bot_data
    bot_data = D.load(p)
    print("Brrt ready now!")

### Moderation ###

@bot.event
async def on_message(message):
    # Check if not self
    if message.author == bot.user:
        return
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
                response = illegal.words[word]['warning'].format(data['author'].mention)
                await ctx.send(response)
                # Remove offense if serious
                if illegal.words[word]['offense'] > 0:
                    await message.delete()
    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    server = None
    c = None
    for srvr in bot.guilds:
        if srvr.name == "the_lab":
            server = srvr
    if server != None:
        for chnl in server.channels:
            if chnl.name == "introductions":
                c = chnl
    if c != None:
        channel = bot.get_channel(c.id)
        response = "{} just got a new member!  Come and introduce yourself, {}".format(server.name, member.mention)
        await channel.send(response)

### Shutdown ###

@bot.command(name='shutdown')
async def shutdown(ctx):
    for owner in bot_data['owners']:
        if ctx.author.name == owner:
            D = Data()
            print("Saving data...")
            D.save(bot_data)
            print("Shutting down...")
            exit()

### Help ###

# Override !help
bot.remove_command('help')
@bot.command(name='help')
async def helpBrrt(ctx, *a):
    response=helper(a, 'help')
    await ctx.send(embed=response)

@bot.command(name='docs')
async def helpBrrt(ctx, *a):
    response=helper(a, 'docs')
    await ctx.send(embed=response)



### Documentation ###

@bot.command(name='api')
async def doc_api(ctx, *a):
    '''
    Fetch APIs
    '''
    if not a:
        response = helper(a, 'api')
        await ctx.send(embed=response)
    else:
        target = str(a[0])
        response = Misc.api(target)
        await ctx.send(response)

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

@bot.command(name='c')
async def doc_c(ctx, *a):
    '''
    C docs
    '''
    if not a:
        response = Misc.c('')
    else:
        target = str(a[0])
        response = Misc.c(target)
    await ctx.send(response)

@bot.command(name='c#')
async def doc_c_sharp(ctx, *a):
    '''
    C# docs
    '''
    if not a:
        response = Misc.c_sharp('')
    else:
        target = str(a[0])
        response = Misc.c_sharp(target)
    await ctx.send(response)

@bot.command(name='c++')
async def doc_c_pp(ctx, *a):
    '''
    C++ docs
    '''
    if not a:
        response = Misc.c_pp('')
    else:
        target = str(a[0])
        response = Misc.c_pp(target)
    await ctx.send(response)

@bot.command(name='java')
async def doc_java(ctx, *a):
    '''
    Java docs
    '''
    if not a:
        response = Misc.java('')
    else:
        target = str(a[0])
        response = Misc.java(target)
    await ctx.send(response)

@bot.command(name='javascript')
async def doc_javascript(ctx, *a):
    '''
    Javascript docs
    '''
    if not a:
        response = Misc.javascript('')
    else:
        target = str(a[0])
        response = Misc.javascript(target)
    await ctx.send(response)

@bot.command(name='lua')
async def doc_lua(ctx, *a):
    '''
    Lua docs
    '''
    if not a:
        response = Misc.lua('')
    else:
        target = str(a[0])
        response = Misc.lua(target)
    await ctx.send(response)

@bot.command(name='perl')
async def doc_perl(ctx, *a):
    '''
    Perl docs
    '''
    if not a:
        response = Misc.perl('')
    else:
        target = str(a[0])
        response = Misc.perl(target)
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

@bot.command(name='ruby')
async def doc_ruby(ctx, *a):
    '''
    Ruby docs
    '''
    if not a:
        response = Misc.ruby('')
    else:
        target = str(a[0])
        response = Misc.ruby(target)
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
async def broadcast(ctx, channel, *a):
    '''
    Broadcast a message
    '''
    response = ""
    for word in a:
        response += word+' '
    c = channel
    chnl = bot.get_channel(c)
    await chnl.send(response)

@bot.command(name='echo')
async def echo(ctx, *a):
    '''
    Echo a message
    '''
    response = ""
    for word in a:
        response += word + " "
    await ctx.send(response)

@bot.command(name='embed')
async def embeded(ctx, des, *a):
    '''
    Embed message
    '''
    response = ""
    for word in a:
        response += word+' '
    embed = Embed(title="Brrt Have Message!",description=des,color=0xFFFFFF)
    embed.set_footer(text="Brrt ||")
    embed.set_image(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMail.png')
    embed.set_thumbnail(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/Brrt.png')
    embed.set_author(name="Brrt", icon_url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMiniMail.png')
    embed.add_field(name="message:", value="**{}**".format(response), inline=False)
    await ctx.send(embed=embed)

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
        print(ctx.author)
        response = random.choice(compliment.praise).format(a[0])
    await ctx.send(response)

@bot.command(name='flip')
async def flip(ctx):
    '''
    Flip a coin
    '''
    response = Misc.flip()
    embed = Embed(title="Brrt Flip Coin!",description="*flips his lucky coin*",color=0xFFFFFF)
    embed.set_footer(text="Brrt ||")
    if response == "Tails":
        embed.set_image(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtCoinTails.png')
    if response == "Heads":
        embed.set_image(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtCoinHeads.png')
    embed.set_thumbnail(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/Brrt.png')
    embed.set_author(name="Brrt", icon_url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMiniCoin.png')
    embed.add_field(name="Landed on:", value="**{}**".format(response), inline=False)
    await ctx.send(embed=embed)

@bot.command(name='d')
async def roll_die(ctx, *a):
    '''
    Roll an X sided die where X is a number <= 1000
    '''
    response = ""
    lmt = 1
    if not a:
        value = 6
    else:
        # get value
        try:
            value = int(a[0])
        except:
            value = 6
        value = abs(value)
        # check if workable
        if value > 1000:
            value = 1000
            response += "Brrt only roll up to 1,000.\n\n"
        if value <= 2:
            value = 2
        # get limit
        if len(a) > 1:
            try:
                lmt = int(a[1])
            except:
                lmt = 1
        # check if workable
        if lmt > 20 or lmt < 1:
            lmt = abs(lmt)
            die_choice = ['dies', 'dices']
            word = random.choice(die_choice)
            response += "Brrt only roll 1 to 20 {} at a time.\n\n".format(word)
        if lmt > 20:
            lmt = 20
        elif lmt < 1:
            lmt = 1
    for rolls in range(lmt):
        response += str(Misc.roll(value))+"\n"
    await ctx.send(response)



bot.run(TOKEN)
