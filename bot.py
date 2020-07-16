#!/usr/bin/python3

import json, random
from discord.ext import commands
from discord.utils import escape_mentions
from discord import Member, Embed, utils
from os import path
from tools import Data, Misc, Vote
from res import illegal, compliment, banter, help_com

### Globals ###

bot_data = {
        'dir' : 'save.data',
        'owners' : [],
        'introductions' : [],
        'member_data' : {
            'negative' : {},
            'positive' : {},
            'rewards' : {},
            'points' : {},
            'level' : {},
            'lup' : {},
            'exp' : {}
            },
        'playing' : {},
        'points' : 0,
        }

TOKEN, PREFIX, bot_data['owners'] = Data.pre_start_up()
bot = commands.Bot(command_prefix=PREFIX)
print("Brrt needs to get ready!\n")



### Helper Functions ###

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



def handle_users():
    print('Member--------------neg--pos--points-----|---lvl--level up---------experience')
    print('                                         |')
    for mmbr in bot_data['member_data']['points']:
        print("{}: {:04} {:04} {:08}   |   {:04} {:016} {:016}".format(
            mmbr,
            bot_data['member_data']['negative'][mmbr],
            bot_data['member_data']['positive'][mmbr],
            bot_data['member_data']['points'][mmbr],
            bot_data['member_data']['level'][mmbr],
            bot_data['member_data']['lup'][mmbr],
            bot_data['member_data']['exp'][mmbr]
            ))
    print("Brrt Points:        {}".format(bot_data['points']))



def excluded(i):
    return bot_data['playing'].get(i, True)



def has_points(i, val):
    try:
        if bot_data['member_data']['points'][i] - val >= 0:
            return True
        else:
            return False
    except:
        return False

def user_point(i, val):
    global bot_data
    try:
        if bot_data['member_data']['points'][i] + val >= 0:
            bot_data['member_data']['points'][i] += val
    except:
        if val >= 0:
            bot_data['member_data']['points'][i] = val



def user_word(i, val):
    global bot_data
    try:
        if val > 0:
            bot_data['member_data']['negative'][i] += val
        if val <= 0:
            bot_data['member_data']['positive'][i] += abs(val)
    except:
        pass



def user_xp(i, val):
    global bot_data
    try:
        bot_data['member_data']['exp'][i] += val
        if bot_data['member_data']['exp'][i] >= bot_data['member_data']['lup'][i]:
            bot_data['member_data']['exp'][i] -= bot_data['member_data']['lup'][i]
            bot_data['member_data']['level'][i] += 1
            bot_data['member_data']['points'][i] += int(bot_data['member_data']['lup'][i] * 0.1)
            bot_data['member_data']['lup'][i] = int(bot_data['member_data']['lup'][i] * 1.25)
    except:
        bot_data['member_data']['exp'][i] = val



#
### Start Async  ###
#



### Connect ###

@bot.event
async def on_ready():
    global bot_data
    D = Data()
    p = bot_data
    temp_data = D.load(p)
    for t in temp_data:
        for key in bot_data:
            if key == t:
                bot_data[key] = temp_data[t]
    
    print('Member--------------neg--pos--points-----|---lvl--level up---------experience')
    print('                                         |')
    for mmbr in bot_data['member_data']['points']:
        print("{}: {:04} {:04} {:08}   |   {:04} {:016} {:016}".format(
            mmbr,
            bot_data['member_data']['negative'][mmbr],
            bot_data['member_data']['positive'][mmbr],
            bot_data['member_data']['points'][mmbr],
            bot_data['member_data']['level'][mmbr],
            bot_data['member_data']['lup'][mmbr],
            bot_data['member_data']['exp'][mmbr]
            ))
    print("Brrt Points:        {}".format(bot_data['points']))

    print("\n\nBrrt ready now!")



### Moderation ###

@bot.event
async def on_message(message):
    offense = 0
    r, g, b = 0, 255, 0
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
                offense = illegal.words[word]['offense']
                # Get message context
                ctx = await bot.get_context(message)
                # Scold user
                response = random.choice(illegal.words[word]['warning']).format(data['author'].mention)
                await ctx.send(response)
                # Check severity of offense
                if illegal.words[word]['offense'] < 0:
                    #if not excluded(str(data['author'].id)):
                        #user_point(str(data['author'].id), abs(illegal.words[word]['offense']))
                    r, g, b = 0, 255, 255
                elif illegal.words[word]['offense'] == 0:
                    pass
                elif illegal.words[word]['offense'] == 1:
                    #user_point(str(data['author'].id), -1)
                    r, g, b = 255, 255, 0
                elif illegal.words[word]['offense'] > 1:
                    r, g, b, = 255, 0, 0
                    #user_point(str(data['author'].id), -10)
                    await message.delete()
    else:
        r, g, b = 255, 255, 255
    if not excluded(str(message.author.id)):
        user_xp(str(message.author.id), 1)
        user_word(str(data['author'].id), offense)
        user_point(str(data['author'].id), offense)
    await bot.process_commands(message)

    if not excluded(str(message.author.id)):
        print("{}: {:04} {:04} {:08}   |   {:04} {:016} {:016}".format(
            str(message.author.id),
            bot_data['member_data']['negative'][str(message.author.id)],
            bot_data['member_data']['positive'][str(message.author.id)],
            bot_data['member_data']['points'][str(message.author.id)],
            bot_data['member_data']['level'][str(message.author.id)],
            bot_data['member_data']['lup'][str(message.author.id)],
            bot_data['member_data']['exp'][str(message.author.id)]
            ))
            
    text = "\x1b[{};2;{};{};{}m".format(38, r, g, b) + message.content + '\x1b[0m'
    print("{}: {}".format(message.author.id, text))


@bot.event
async def on_member_join(member):
    c = None
    for srvr in bot.guilds:
        if srvr == member.guild:
            server = srvr
    
    for chnl in server.channels:
        for valid in bot_data['introductions']:
            if chnl.name == valid:
                c = chnl
    
    if c != None:
        channel = bot.get_channel(c.id)
        response = "{} just got a new member!  Come and introduce yourself, {}".format(server.name, member.mention)
        await channel.send(response)



### Shutdown ###

@bot.command(name='shutdown')
async def shutdown(ctx):
    can_do = False
    response = "You're not my owner!  Only an owner can use that command!"
    for owner in bot_data['owners']:
        if ctx.author.name == owner:
            response = "Okay, {}!  See you soon!".format(owner)
            can_do = True
    await ctx.send(response)
    if can_do:
        D = Data()
        print("Saving data...")
        handle_users()
        D.save(bot_data)
        print("Shutting down...")
        await bot.close()



### Data Collection Verification ###

@bot.command(name="keep-data")
async def data_collection(ctx, a):
    '''
    Allow/Disallow data collection
    '''
    global bot_data
    if a == "yes":
        if excluded(str(ctx.author.id)):
            bot_data['member_data']['negative'][str(ctx.author.id)] = 0
            bot_data['member_data']['positive'][str(ctx.author.id)] = 0
            bot_data['member_data']['points'][str(ctx.author.id)] = 0
            bot_data['member_data']['level'][str(ctx.author.id)] = 0
            bot_data['member_data']['lup'][str(ctx.author.id)] = 100
            bot_data['member_data']['exp'][str(ctx.author.id)] = 0
            bot_data['playing'][str(ctx.author.id)] = False
            response = "Brrt will start giving you points!"
        else:
            response = "You already gave Brrt permission!"
    if a == "no":
        if not excluded(str(ctx.author.id)):
            bot_data['member_data']['points'].pop(str(ctx.author.id))
            bot_data['playing'].pop(str(ctx.author.id))
        response = "More points for Brrt!"
    if a == 'status':
        if not excluded(str(ctx.author.id)):
            response = "Brrt has permission to give you points and save data!"
        else:
            response = "Brrt can't save your data."
    await ctx.send(response)



### Help ###

bot.remove_command('help')
@bot.command(name='help')
async def helpBrrt(ctx, *a):
    '''
    Override !help
    '''
    response=helper(a, 'help')
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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

@bot.command(name='docs')
async def helpBrrt(ctx, *a):
    response=helper(a, 'docs')
    await ctx.send(embed=response)
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)



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
    await chnl.send(escape_mentions(response))
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 10)

@bot.command(name='echo')
async def echo(ctx, *a):
    '''
    Echo a message
    '''
    response = ""
    for word in a:
        response += word + " "
    if not response:
        response = "Don't try to trick Brrt!"
    await ctx.send(escape_mentions(response))
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 1)

@bot.command(name='embed')
async def embeded(ctx, des, *a):
    '''
    Embed message
    '''
    acceptable = ['.gif', '.png', '.jpg', '.jpeg']
    has_img = False
    index = -1
    response = ""
    embed = Embed(title="Brrt Have Message!",description=des,color=0xFFFFFF)
    for i, word in enumerate(a):
        for img in acceptable:
            if img in word and i > 0:
                embed.set_image(url=word)
                has_img = True
                index = i
    for i, word in enumerate(a):
        if i != index:
            response += word+' '
    embed.set_footer(text="Brrt ||")
    #if not has_img:
    #    embed.set_image(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMail.png')
    embed.set_thumbnail(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/Brrt.png')
    embed.set_author(name="Brrt", icon_url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMiniMail.png')
    embed.add_field(name="{} says:".format(ctx.author.name), value="**{}**".format(escape_mentions(response)), inline=False)
    await ctx.message.delete()
    await ctx.send(embed=embed)
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 10)

@bot.command(name='banter')
async def banterBrrt(ctx, *a):
    '''
    Banter command, accepts (arg)
    '''
    if not excluded(str(ctx.author.id)) and has_points(str(ctx.author.id), 1):
        response = ""
        if not a:
            response = random.choice(banter.loose)
        else:
            response = random.choice(banter.focus).format(a[0])
                
        if not response:
            response = "Don't try to trick Brrt!"
        user_xp(str(ctx.author.id), 1)
        user_point(str(ctx.author.id), -1)
    else:
        response = "Sorry, Brrt only do banter if you have points!"
    await ctx.send(escape_mentions(response))

@bot.command(name='praise')
async def praiseBrrt(ctx, *a):
    '''
    Praise People or Brrt
    '''
    if not a:
        response = random.choice(compliment.shucks)
        bot_data['points'] += 1
    else:
        if a[0] != ctx.author.mention and a[0] != "@everyone" and a[0] != "@here":
            for mem in bot.get_all_members():
                if mem.mentioned_in(ctx.message) and not excluded(str(mem.id)):
                    user_point(str(mem.id), 1)
            if not excluded(str(ctx.author.id)):
                user_point(str(ctx.author.id), 1)
        if a[0] == bot.user.mention and a[0] != "@everyone" and a[0] != "@here":
            bot_data['points'] += 1
        response = random.choice(compliment.praise).format(a[0])
    await ctx.send(escape_mentions(response))
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 10)

@bot.command(name='give')
async def give_points(ctx, mmbr, val):
    '''
    Give a member points
    '''
    target = None
    if has_points(str(ctx.author.id), int(val)):
        for mem in bot.get_all_members():
            if mem.mentioned_in(ctx.message) and mmbr != ctx.author.mention:
                if not excluded(str(mem.id)):
                    if not excluded(str(ctx.author.id)):
                        target = mem
                    else:
                        response = "You haven't given Brrt permission to give you points!"
                else:
                    response = "{} hasn't give Brrt permission to give them points!".format(mem.name)
            elif mem == bot.user.mention and not excluded(str(ctx.author.id)):
                bot_data['points'] += int(val)
                user_point(str(ctx.author.id), -int(val))
                response = "{} gave {} {} points!".format(ctx.author.name, mem.name, val)
            else:
                response = "Are you trying to trick Brrt?"
        if target != None:
            user_xp(str(ctx.author.id), int(val))
            user_point(str(target.id), int(val))
            user_point(str(ctx.author.id), -int(val))
            response = "{} gave {} {} points!".format(ctx.author.name, target.name, val)
        else:
            response = "Are you trying to trick Brrt?"
    else:
        response = "You don't have enough points!"
    await ctx.send(escape_mentions(response))

@bot.command(name='balance-karma')
async def stats(ctx, *a):
    global bot_data
    target = None
    if not a:
        target = ctx.author
    else:
        for mem in bot.get_all_members():
            if mem.mentioned_in(ctx.message):
                if not excluded(str(mem.id)):
                    target = mem
    
    while bot_data['member_data']['negative'][str(target.id)] > 0 and bot_data['member_data']['positive'][str(target.id)] > 0:
        bot_data['member_data']['negative'][str(target.id)] -= 1
        bot_data['member_data']['positive'][str(target.id)] -= 1

@bot.command(name='stats')
async def stats(ctx, *a):
    '''
    Get User Stats
    '''
    user_mentn = False
    if not a:
        if not excluded(str(ctx.author.id)):
            _points = '{}'.format(bot_data['member_data']['points'][str(ctx.author.id)])
            _karma = '{}'.format(bot_data['member_data']['positive'][str(ctx.author.id)] - bot_data['member_data']['negative'][str(ctx.author.id)])
            _level = '{}'.format(bot_data['member_data']['level'][str(ctx.author.id)])
            _lup = '{}'.format(bot_data['member_data']['lup'][str(ctx.author.id)])
            _exp = '{}'.format(bot_data['member_data']['exp'][str(ctx.author.id)])

            embed = Embed(title="Brrt Show Stats!",description="Stats",color=0xFFFFFF)
            embed.set_footer(text="Brrt ||")
            embed.set_thumbnail(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/Brrt.png')
            embed.set_author(name="Brrt", icon_url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMiniMail.png')
            embed.add_field(name="Points:", value="**{}**".format(_points), inline=False)
            embed.add_field(name="Karma:", value="**{}**".format(_karma), inline=False)
            embed.add_field(name="Level:", value="**{}**".format(_level), inline=False)
            embed.add_field(name="Next Level:", value="**{}**".format(_lup), inline=False)
            embed.add_field(name="Experience:", value="**{}**".format(_exp), inline=False)
            await ctx.send(embed=embed)
        if excluded(str(ctx.author.id)):
            response = "Brrt isn't storing your data!"
    else:
        if a[0] == 'points':
            response = "You have {} Brrt points!".format(bot_data['member_data']['points'][str(ctx.author.id)])
        elif a[0] == 'level':
            response = "Your karma is {}!".format(bot_data['member_data']['positive'][str(ctx.author.id)] - bot_data['member_data']['negative'][str(ctx.author.id)])
        elif a[0] == 'level':
            response = "You're level {}!".format(bot_data['member_data']['level'][str(ctx.author.id)])
        elif a[0] == 'next':
            response = "You have {} experience to earn until your next level!".format(bot_data['member_data']['lup'][str(ctx.author.id)])
        elif a[0] == 'exp':
            response = "You have {} experience!".format(bot_data['member_data']['exp'][str(ctx.author.id)])
        else:
            mem = None
            backup = None
            for m in bot.get_all_members():
                if m.mentioned_in(ctx.message):
                    if not excluded(str(m.id)):
                        mem = m
                    else:
                        backup = m
            try:
                _points = '{}'.format(bot_data['member_data']['points'][str(mem.id)])
                _level = '{}'.format(bot_data['member_data']['level'][str(mem.id)])
                _lup = '{}'.format(bot_data['member_data']['lup'][str(mem.id)])
                _exp = '{}'.format(bot_data['member_data']['exp'][str(mem.id)])

                embed = Embed(title="Brrt Show Stats!",description="Stats",color=0xFFFFFF)
                embed.set_footer(text="Brrt ||")
                embed.set_thumbnail(url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/Brrt.png')
                embed.set_author(name="Brrt", icon_url='https://raw.githubusercontent.com/ihave13digits/Brrt/master/img/BrrtMiniMail.png')
                embed.add_field(name="Points:", value="**{}**".format(_points), inline=False)
                embed.add_field(name="Level:", value="**{}**".format(_level), inline=False)
                embed.add_field(name="Next Level:", value="**{}**".format(_lup), inline=False)
                embed.add_field(name="Experience:", value="**{}**".format(_exp), inline=False)
                await ctx.send(embed=embed)
            except:
                response = "Brrt isn't storing {}'s data!".format(backup.name)
    try:
        await ctx.send(response)
    except:
        pass
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 1)



### Random ###

@bot.command(name='flip')
async def flip(ctx, *a):
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
    if not a:
        text = "Landed on:"
    else:
        if response.lower()[0] == a[0].lower()[0]:
            text = "Woo!  You got:"
            if not excluded(str(ctx.author.id)):
                user_point(str(ctx.author.id), 1)
        else:
            text = "That's a shame, it landed on:"
    embed.add_field(name="{}".format(text), value="**{}**".format(response), inline=False)
    await ctx.send(embed=embed)
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)

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
    if not excluded(str(ctx.author.id)):
        user_xp(str(ctx.author.id), 5)



bot.run(TOKEN)
