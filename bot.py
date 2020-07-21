#!/usr/bin/python3

import random
from discord.ext import commands
from discord.channel import DMChannel
from discord import Member, Embed, Color, utils, errors
from os import path
from tools import Data, Misc, Vote
from res import illegal, compliment, banter, help_com, welcome, brrt_roles, brrt_image

### Globals ###

voting_data = {}

bot_data = {
        'dir' : 'save.data',
        'owners' : [],
        'secret' : [],
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
        'enabled' : {
            'documentation' : True,
            'moderation' : True,
            'scoring' : True,
            'welcome' : True,
            'random' : True,
            'social' : True,
            'voting' : True,
            'roles' : True
            },
        'points' : 0,
        }

TOKEN, PREFIX, bot_data['owners'], bot_data['introductions'], bot_data['secret'] = Data.pre_start_up()
bot = commands.Bot(command_prefix=PREFIX)



### Helper Functions ###

def save_data():
    D = Data()
    mems = []
    for mem in bot.get_all_members():
        mems.append(str(mem.id))
    print("Saving data...")
    handle_users(mems)
    D.save(bot_data, bot_data['dir'])

def load_data():
    global bot_data
    print("Brrt needs to get ready!\n")
    D = Data()
    temp_data = D.load(bot_data['dir'])
    bot_data['dir'] = temp_data['dir']
    bot_data['owners'] = temp_data['owners']
    bot_data['secret'] = temp_data['secret']
    bot_data['introductions'] = temp_data['introductions']
    bot_data['member_data'] = temp_data['member_data']
    bot_data['playing'] = temp_data['playing']
    bot_data['enabled'] = temp_data['enabled']
    bot_data['points'] = temp_data['points']
    print('Member--------------neg--pos--points-----|---lvl--level up---------experience')
    print('                                         |')
    print("Brrt Points: {}".format(bot_data['points']))
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
load_data()



def helper(a, mode, owner):
    mandatory = ['help', 'documentation', 'moderation', 'scoring', 'welcome', 'random', 'social', 'voting', 'roles']
    owner_only = ['settings', 'disable', 'enable', 'shutdown']
    docs_only = ['api', 'docs', 'source', 'discord', 'godot', 'unity', 'unreal'
            'c', 'c#', 'c++', 'java', 'javascript', 'lua', 'perl', 'python', 'ruby', 'rust']
    social_only = ['broadcast', 'embed', 'echo', 'banter', 'praise']
    playing_only = ['keep-data', 'give', 'stats', 'role', 'balance-karma']
    voting_only = ['vote']
    random_only = ['flip', 'd']
    roles_only = ['role',
            'fresh_meat', 'newb', 'underlind', 'novice', 'regular',
            'gamer', 'game_lord', 'game_addict', 'advanced_user', 'power_user',
            'advanced_power_user', 'junior_veteran', 'veteran', 'veteran_senior', 'veteran_commander',
            'veteran_lord', 'enlightened_one', 'game_buddha']

    color_choice = Misc.rand_hex()
    embed=Embed(title="Brrt {}".format(mode).upper(), url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=color_choice)
    if mode == "api":
        target = help_com.api_dict
    if mode == "docs":
        target = help_com.docs_dict
    if mode == "help":
        target = help_com.help_dict
    if mode == "role":
        target = help_com.role_dict
    if mode == 'settings':
        target = help_com.sets_dict
    try:
        embed.add_field(name=a[0], value=target[a[0]]['detail'], inline=False)
    except:
        if not owner:
            for x in target:
                if ( x in mandatory or
                        (bot_data['enabled']['documentation'] and x in docs_only) or
                        (bot_data['enabled']['social'] and x in social_only) or
                        (bot_data['enabled']['scoring'] and x in playing_only) or
                        (bot_data['enabled']['voting'] and x in voting_only) or
                        (bot_data['enabled']['random'] and x in random_only) or
                        (bot_data['enabled']['roles'] and x in roles_only) or
                        x not in owner_only):
                    embed.add_field(name=x, value=target[x]['concise'], inline=False)
        else:
            for x in target:
                if ( x in mandatory or
                        (bot_data['enabled']['documentation'] and x in docs_only) or
                        (bot_data['enabled']['social'] and x in social_only) or
                        (bot_data['enabled']['scoring'] and x in playing_only) or
                        (bot_data['enabled']['voting'] and x in voting_only) or
                        (bot_data['enabled']['random'] and x in random_only) or
                        (bot_data['enabled']['roles'] and x in roles_only) or
                        x in owner_only):
                    embed.add_field(name=x, value=target[x]['concise'], inline=False)

    
    embed.set_footer(text="Brrt ||")
    return embed



def prune_users(mems):
    to_go = ""
    for mmbr in bot_data['playing']:
        if mmbr not in mems:
            to_go = mmbr
    if to_go != "":
        print("{}: has left the server.  Brrt will remove their data!".format(to_go))
        bot_data['playing'].pop(mmbr)
        bot_data['member_data']['negative'].pop(to_go)
        bot_data['member_data']['positive'].pop(to_go)
        bot_data['member_data']['points'].pop(to_go)
        bot_data['member_data']['level'].pop(to_go)
        bot_data['member_data']['lup'].pop(to_go)
        bot_data['member_data']['exp'].pop(to_go)
        return True
    else:
        return False

def handle_users(mems):
    if bot_data['enabled']['scoring']:
        pruning = True
        while pruning:
            pruning = prune_users(mems)
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
    if bot_data['enabled']['scoring']:
        return bot_data['playing'].get(str(i), True)
    else:
        return False

def has_points(i, val):
    try:
        if bot_data['member_data']['points'][str(i)] - val >= 0:
            return True
        else:
            return False
    except:
        return False

def user_point(i, val):
    global bot_data
    try:
        if bot_data['member_data']['points'][str(i)] + val >= 0:
            bot_data['member_data']['points'][str(i)] += val
    except:
        if val >= 0:
            bot_data['member_data']['points'][str(i)] = val

def user_word(i, val):
    global bot_data
    try:
        if val > 0:
            bot_data['member_data']['negative'][str(i)] += val
        if val <= 0:
            bot_data['member_data']['positive'][str(i)] += abs(val)
    except:
        pass

def user_xp(i, val):
    global bot_data
    leveled_up = False
    ID = str(i)
    try:
        bot_data['member_data']['exp'][ID] += val
        if bot_data['member_data']['exp'][ID] >= bot_data['member_data']['lup'][ID]:
            bot_data['member_data']['exp'][ID] -= bot_data['member_data']['lup'][ID]
            bot_data['member_data']['level'][ID] += 1
            bot_data['member_data']['points'][ID] += int(bot_data['member_data']['lup'][ID] * 0.1)
            bot_data['member_data']['lup'][ID] = int(bot_data['member_data']['lup'][ID] * 1.25)
            leveled_up = True
    except:
        bot_data['member_data']['exp'][ID] = val
    return leveled_up

def level_text(ctx, exp):
    if not excluded(str(ctx.author.id)):
        level_up = user_xp(str(ctx.author.id), exp)
        if level_up:
            level_text = "{} is now level {}!".format(ctx.author.mention, bot_data['member_data']['level'][str(ctx.author.id)])
            ctx.send(level_text)

def user_stats(mmbr):
    _points = '{}'.format(bot_data['member_data']['points'][str(mmbr)])
    _karma = '{}'.format(bot_data['member_data']['positive'][str(mmbr)] - bot_data['member_data']['negative'][str(mmbr)])
    _level = '{}'.format(bot_data['member_data']['level'][str(mmbr)])
    _lup = bot_data['member_data']['lup'][str(mmbr)]
    _exp = bot_data['member_data']['exp'][str(mmbr)]
    embed = Embed(title="Brrt Show Stats!",description="Stats",color=0xFFFFFF)
    embed.set_footer(text="Brrt ||")
    embed.set_thumbnail(url=brrt_image.image['brrt'])
    embed.set_author(name="Brrt", icon_url=brrt_image.image['brrt_mail'])
    embed.add_field(name="Points:", value="**{}**".format(_points), inline=False)
    embed.add_field(name="Karma:", value="**{}**".format(_karma), inline=False)
    embed.add_field(name="Level:", value="**{}**".format(_level), inline=False)
    embed.add_field(name="Next Level:", value="**{}**".format(_lup - _exp), inline=False)
    embed.add_field(name="Experience:", value="**{}**".format(_exp), inline=False)
    return embed



#
###
#### --- Start Async ---
###
#



### Connect ###

@bot.event
async def on_ready():
    print("Brrt Ready!")


### Moderation ###

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    data = {'author':message.author, 'channel':message.channel, 'content':message.content}
    if bot_data['enabled']['moderation']:
        offense = 0
        r, g, b = 0, 255, 0
        if message.author == bot.user:
            return
        if not data['content'].startswith(PREFIX):
            for word in illegal.words:
                if word in data['content'].lower():
                    offense = illegal.words[word]['offense']
                    response = random.choice(illegal.words[word]['warning']).format(data['author'].mention)
                    await ctx.send(response)
                    
                    if illegal.words[word]['offense'] == -10:
                        r, g, b = 0, 0, 255
                    if illegal.words[word]['offense'] == -1:
                        r, g, b = 0, 255, 255
                    if illegal.words[word]['offense'] == 0:
                        r, g, b = 0, 255, 0
                    if illegal.words[word]['offense'] == 1:
                        r, g, b = 255, 255, 0
                    if illegal.words[word]['offense'] == 10:
                        r, g, b, = 255, 0, 0
                        await message.delete()
        else:
            r, g, b = 255, 255, 255
        if not excluded(message.author.id):
            user_word(data['author'].id, offense)
            if offense <= 0:
                user_point(data['author'].id, abs(offense))
            else:
                user_point(data['author'].id, -offense)
            level_text(ctx, 1)

        stats = ""
        if not excluded(message.author.id):
            ID = str(message.author.id)
            stats = "{}: {:04} {:04} {:08}   |   {:04} {:016} {:016}".format(
                ID,
                bot_data['member_data']['negative'][ID],
                bot_data['member_data']['positive'][ID],
                bot_data['member_data']['points'][ID],
                bot_data['member_data']['level'][ID],
                bot_data['member_data']['lup'][ID],
                bot_data['member_data']['exp'][ID]
                )
            print(stats)
        text = "\x1b[{};2;{};{};{}m".format(38, r, g, b) + message.content + '\x1b[0m'
        print("{}: {}".format(message.author.id, text))

        color_tag = Color.from_rgb(r, g, b)
        private_message = Embed(title=message.author.name, color=color_tag)
        try:
            private_message.add_field(name=message.channel.name, value=message.content, inline=False)
            for chnl in message.author.guild.channels:
                if chnl.name in bot_data['secret']:
                    private_channel = bot.get_channel(chnl.id)
                    await private_channel.send(embed=private_message)
        except:
            pass
    else:
        level_text(ctx, 1)

    if type(message.channel) is DMChannel:
        try:
            if message.content[0] == PREFIX:
                if message.author.name not in bot_data['owners']:
                    response = "Halp!  Brrt needs an adult!"
                    await ctx.send(response)
                else:
                    try:
                        await bot.process_commands(message)
                    except errors.CommandInvokeError:
                        pass
        except:
            pass
    else:
        await bot.process_commands(message)


### Member Join ###

@bot.event
async def on_member_join(member):
    if bot_data['enabled']['welcome']:
        response = ""
        for srvr in bot.guilds:
            if srvr == member.guild:
                for chnl in srvr.channels:
                    for valid in bot_data['introductions']:
                        if chnl.name == valid:
                            channel = bot.get_channel(chnl.id)
                            wt = random.choice(welcome.welcome_types)
                            if wt == "ms":
                                response = random.choice(welcome.messages[wt]).format(member.mention, srvr.name)
                            if wt == "sm":
                                response = random.choice(welcome.messages[wt]).format(srvr.name, member.mention)
                            if wt == "m":
                                response = random.choice(welcome.messages[wt]).format(member.mention)
                            await channel.send(response)
        text = "\x1b[{};2;{};{};{}m".format(38, 255, 0, 255) + response + '\x1b[0m'
        print("{}: {}".format(member.id, text))



### Shutdown ###

@bot.command(name='shutdown')
async def shutdown(ctx):
    can_do = False
    response = "You're not my owner!  Only an owner can use that command!"
    if ctx.author.name in bot_data['owners']:
        response = "Okay, {}!  See you soon!".format(ctx.author.name)
        can_do = True
    await ctx.send(response)
    if can_do:
        save_data()
        print("Shutting down...")
        await bot.close()



### Settings ###

@bot.command(name='settings')
async def settings(ctx, *a):
    if ctx.author.name in bot_data['owners']:
        if a:
            if a[0] == 'status':
                color_choice = Misc.rand_hex()
                response = embed=Embed(title="Brrt Settings".upper(), url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=color_choice)
                for ftr in bot_data['enabled']:
                    response.add_field(name=ftr, value=bot_data['enabled'][ftr], inline=False)
        else:
            response=helper(a, 'settings', True)
        await ctx.send(embed=response)
    else:
        response = "You're not my owner!  Only an owner can use that command!"
        await ctx.send(response)

@bot.command(name='enable')
async def enable(ctx, *a):
    global bot_data
    can_do = False
    response = "You're not my owner!  Only an owner can use that command!"
    if ctx.author.name in bot_data['owners']:
        response = "Okay, {}!  I'll enable those features!".format(ctx.author.name)
        can_do = True
    await ctx.send(response)
    if can_do:
        for ftr in a:
            if ftr in bot_data['enabled']:
                bot_data['enabled'][ftr] = True



@bot.command(name='disable')
async def disable(ctx, *a):
    global bot_data
    can_do = False
    response = "You're not my owner!  Only an owner can use that command!"
    if ctx.author.name in bot_data['owners']:
        response = "Okay, {}!  Disable those features!".format(ctx.author.name)
        can_do = True
    await ctx.send(response)
    if can_do:
        for ftr in a:
            if ftr in bot_data['enabled']:
                bot_data['enabled'][ftr] = False



### Data Collection Verification ###

@bot.command(name="keep-data")
async def data_collection(ctx, a):
    global bot_data
    if bot_data['enabled']['scoring']:
        ID = str(ctx.author.id)
        if a == "yes":
            if excluded(ctx.author.id):
                bot_data['member_data']['negative'][ID] = 0
                bot_data['member_data']['positive'][ID] = 0
                bot_data['member_data']['points'][ID] = 0
                bot_data['member_data']['level'][ID] = 0
                bot_data['member_data']['lup'][ID] = 100
                bot_data['member_data']['exp'][ID] = 0
                bot_data['playing'][ID] = False
                response = "Brrt will start giving you points!"
            else:
                response = "You already gave Brrt permission!"
        if a == "no":
            if not excluded(ctx.author.id):
                bot_data['member_data']['negative'].pop(ID)
                bot_data['member_data']['positive'].pop(ID)
                bot_data['member_data']['points'].pop(ID)
                bot_data['member_data']['level'].pop(ID)
                bot_data['member_data']['lup'].pop(ID)
                bot_data['member_data']['exp'].pop(ID)
                bot_data['playing'].pop(ID)
            response = "More points for Brrt!"
        if a == 'status':
            if not excluded(ctx.author.id):
                response = "Brrt has permission to give you points and save data!"
            else:
                response = "Brrt can't save your data."
        await ctx.send(response)



### Help ###

bot.remove_command('help')
@bot.command(name='help')
async def helpBrrt(ctx, *a):
    if ctx.author.name in bot_data['owners']:
        owner = True
    else:
        owner = False
    response=helper(a, 'help', owner)
    await ctx.send(embed=response)



### Documentation ###

@bot.command(name='api')
async def doc_api(ctx, *a):
    if ctx.author.name in bot_data['owners']:
        owner = True
    else:
        owner = False
    if bot_data['enabled']['documentation']:
        if not a:
            response = helper(a, 'api', owner)
            await ctx.send(embed=response)
        else:
            target = str(a[0])
            response = Misc.api(target)
            await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='docs')
async def helpBrrt(ctx, *a):
    if ctx.author.name in bot_data['owners']:
        owner = True
    else:
        owner = False
    if bot_data['enabled']['documentation']:
        response=helper(a, 'docs', owner)
        await ctx.send(embed=response)
        level_text(ctx, 5)

@bot.command(name='source')
async def doc_source(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('source', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='c')
async def doc_c(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('c', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='c#')
async def doc_c_sharp(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('c_sharp', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='c++')
async def doc_c_pp(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('c_pp', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='java')
async def doc_java(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('java', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='javascript')
async def doc_javascript(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('javascript', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='lua')
async def doc_lua(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('lua', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='perl')
async def doc_perl(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('perl', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='python')
async def doc_python(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('python', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='ruby')
async def doc_ruby(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('ruby', *a)
        await ctx.send(response)
        level_text(ctx, 5)

@bot.command(name='rust')
async def doc_rust(ctx, *a):
    if bot_data['enabled']['documentation']:
        response = Misc.get_docs('rust', *a)
        await ctx.send(response)
        level_text(ctx, 5)



### Misc. ###

@bot.command(name='broadcast')
async def broadcast(ctx, channel, *a):
    if bot_data['enabled']['social']:
        if not(type(ctx.message.channel) is DMChannel):
            response = "{} says: ".format(ctx.author.name)
            target = None
            for word in a:
                if word != '@everyone' and word != '@here':
                    response += word+' '
        
            for srvr in bot.guilds:
                if srvr == ctx.author.guild:
                    for chnl in srvr.channels:
                        if chnl.mention == channel:
                            target = bot.get_channel(chnl.id)
                
            if target != None:
                if not response:
                    response = ""
                await target.send(response)
                level_text(ctx, 10)

@bot.command(name='echo')
async def echo(ctx, *a):
    if bot_data['enabled']['social']:
        try:
            response = ""
            for word in a:
                if word != '@everyone' and word != '@here':
                    response += word + " "
            if not response:
                response = "Don't try to trick Brrt!"
            level_text(ctx, 5)
        except:
            response = "Halp!  Brrt needs an adult!"
        await ctx.send(response)

@bot.command(name='embed')
async def embeded(ctx, des, *a):
    if bot_data['enabled']['social']:
        try:
            acceptable = ['.gif', '.jpg', '.jpeg', '.png']
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
                    if word != '@everyone' and word != '@here':
                        response += word+' '
            embed.set_footer(text="Brrt ||")
            if not response:
                response = "Brrt got swindled!"
            embed.set_thumbnail(url=brrt_image.image['brrt'])
            embed.set_author(name="Brrt", icon_url=brrt_image.image['brrt_mail'])
            embed.add_field(name="{} says:".format(ctx.author.name), value="**{}**".format(response), inline=False)
            if not (type(ctx.message.channel) is DMChannel):
                await ctx.message.delete()
            await ctx.send(embed=embed)
            level_text(ctx, 10)
        except:
            response = "Halp!  Brrt needs an adult!"
            await ctx.send(response)

@bot.command(name='banter')
async def brrtBanter(ctx, *a):
    if bot_data['enabled']['social']:
        if not excluded(ctx.author.id) and has_points(ctx.author.id, 1):
            response = ""
            if not a:
                response = random.choice(banter.loose)
            else:
                if not(type(ctx.message.channel) is DMChannel):
                    if a[0] != '@everyone' and a[0] != '@here':
                        response = random.choice(banter.focus).format(a[0])
                else:
                    response = "Halp!  Brrt needs an adult!"
            if not response:
                response = "Don't try to trick Brrt!"
            user_point(ctx.author.id, -1)
        else:
            response = "Sorry, Brrt only do banter if you have points!"
        level_text(ctx, 10)
    await ctx.send(response)

@bot.command(name='praise')
async def brrtPraise(ctx, *a):
    if bot_data['enabled']['social']:
        if not a:
            response = random.choice(compliment.shucks)
            bot_data['points'] += 1
        else:
            if a[0] != ctx.author.mention and a[0] != "@everyone" and a[0] != "@here":
                if not(type(ctx.message.channel) is DMChannel):
                    for mem in bot.get_all_members():
                        if mem.mentioned_in(ctx.message) and not excluded(mem.id):
                            user_point(mem.id, 1)
                    if not excluded(ctx.author.id):
                        user_point(ctx.author.id, 1)
                    response = random.choice(compliment.praise).format(a[0])
                else:
                    response = "Halp!  Brrt needs an adult!"
            elif a[0] == bot.user.mention:
                bot_data['points'] += 1
        level_text(ctx, 10)
        await ctx.send(response)

@bot.command(name='give')
async def give_points(ctx, mmbr, val):
    if bot_data['enabled']['scoring']:
        target = None
        if not(type(ctx.message.channel) is DMChannel):
            if has_points(ctx.author.id, int(val)):
                for mem in bot.get_all_members():
                    if not excluded(mem.id):
                        if mem.mentioned_in(ctx.message) and mmbr != ctx.author.mention:
                            if not excluded(ctx.author.id):
                                if mmbr != '@everyone' and mmbr != '@here':
                                    target = mem
                            else:
                                response = "You haven't given Brrt permission to give you points!"
                        elif mem == bot.user.mention and not excluded(ctx.author.id):
                            bot_data['points'] += int(val)
                            user_point(ctx.author.id, -int(val))
                            response = "{} gave {} {} points!".format(ctx.author.name, mem.name, val)
                    
                        else:
                            response = "Are you trying to trick Brrt?"
                    else:
                        response = "You haven't given Brrt permission to give you points!"
                if target != None:
                    user_point(target.id, int(val))
                    user_point(ctx.author.id, -int(val))
                    response = "{} gave {} {} points!".format(ctx.author.name, target.name, val)
                else:
                    response = "Are you trying to trick Brrt?"
            else:
                response = "You don't have enough points!"
        else:
            response = "Are you trying to trick Brrt?"
        await ctx.send(response)
        level_text(ctx, 10)

@bot.command(name='balance-karma')
async def balance_karma(ctx, *a):
    global bot_data
    if bot_data['enabled']['scoring']:
        response = "Brrt needs permission, first!"
        if ctx.author.name in bot_data['owners']:
            target = None
            if not a:
                target = ctx.author
                response = "Brrt balanced your karma, {}!".format(target.name)

            else:
                for mem in bot.get_all_members():
                    if mem.mentioned_in(ctx.message):
                        if not excluded(mem.id):
                            target = mem
                            response = "Brrt balanced {}'s karma!".format(target.name)
    
        else:
            if not a:
                target = ctx.author
                response = "Brrt balanced your karma, {}!".format(target.name)
        
        ID = str(target.id)
        while bot_data['member_data']['negative'][ID] > 0 and bot_data['member_data']['positive'][ID] > 0:
            bot_data['member_data']['negative'][ID] -= 1
            bot_data['member_data']['positive'][ID] -= 1

        await ctx.send(response)
        level_text(ctx, 10)

@bot.command(name='stats')
async def stats(ctx, *a):
    if bot_data['enabled']['scoring']:
        user_mentn = False
        if not a:
            if not excluded(ctx.author.id):
                embed = user_stats(ctx.author.id)
                await ctx.send(embed=embed)
            if excluded(ctx.author.id):
                response = "Brrt isn't storing your data!"
        else:
            ID = str(ctx.author.id)
            if a[0] == 'points':
                response = "You have {} Brrt points!".format(
                        bot_data['member_data']['points'][ID])
            elif a[0] == 'karma':
                response = "Your karma is {}!".format(
                        bot_data['member_data']['positive'][ID] - bot_data['member_data']['negative'][ID])
            elif a[0] == 'level':
                response = "You're level {}!".format(
                        bot_data['member_data']['level'][ID])
            elif a[0] == 'next':
                response = "You have {} experience to earn until your next level!".format(
                        bot_data['member_data']['lup'][ID]-bot_data['member_data']['exp'][ID])
            elif a[0] == 'exp':
                response = "You have {} experience!".format(
                        bot_data['member_data']['exp'][ID])
            else:
                if not(type(ctx.message.channel) is DMChannel):
                    mem = None
                    backup = None
                    for m in bot.get_all_members():
                        if m.mentioned_in(ctx.message):
                            if not excluded(m.id):
                                mem = m
                            else:
                                backup = m
                    if mem != None:
                        try:
                            embed = user_stats(mem.id)
                            await ctx.send(embed=embed)
                        except:
                            response = "Brrt isn't storing {}'s data!".format(backup.name)
                    else:
                        response = "Brrt needs a user mention for this command!"
                else:
                    response = "Halp!  Brrt needs an adult!"
        try:    
            await ctx.send(response)
        except:
            pass



@bot.command(name='vote')
async def vote(ctx, a):
    if bot_data['enabled']['viting']:
        pass



@bot.command(name='role')
async def role(ctx, *a):
    if bot_data['enabled']['roles']:
        if not(type(ctx.message.channel) is DMChannel):
            text = "Brrt doesn't know about that role! Try `!role` and Brrt will help."
            if not excluded(ctx.author.id):
                sel = None
                if not a:
                    if ctx.author.name in bot_data['owners']:
                        owner = True
                    else:
                        owner = False
                    embed=helper(a, 'role', owner)
                    await ctx.send(embed=embed)
                else:
                    try:
                        for i, role in enumerate(ctx.guild.roles):
                            if ctx.guild.roles[i].name == a[0]:
                                if bot_data['member_data']['level'][str(ctx.author.id)] >= brrt_roles.valid[a[0]]['level']:
                                    sel = role
                                    text = "You've added the role {}!".format(role.name)
                                    break
                                else:
                                    text = "You need to be a higher level to get that role!"

                        if sel != None:
                            await ctx.author.add_roles(sel)
                        response = "{}".format(text)
                        await ctx.send(response)
                    except errors.Forbidden:
                        response = "Brrt doesn't have permission to give that role!"
        else:
            response = "Halp!  Brrt needs an adult!"
        await ctx.send(response)



### Random ###

@bot.command(name='flip')
async def flip(ctx, *a):
    if bot_data['enabled']['random']:
        response = Misc.flip()
        gets_point = False
        embed = Embed(title="Brrt Flip Coin!",description="*flips his lucky coin*",color=0xFFFFFF)
        embed.set_footer(text="Brrt ||")
        if response == "Tails":
            embed.set_image(url=brrt_image.image['brrt_coin_tails'])
        if response == "Heads":
            embed.set_image(url=brrt_image.image['brrt_coin_heads'])
        embed.set_thumbnail(url=brrt_image.image['brrt'])
        embed.set_author(name="Brrt", icon_url=brrt_image.image['brrt_coin_mini'])
        if not a:
            text = "Landed on:"
        else:
            if ((response.lower()[0] == a[0].lower()[0] and len(a[0]) == 1) or
                    (response == "Heads" and a[0].lower()[0] == "1") or
                    (response == "Heads" and a[0].lower() == "true") or
                    (response == "Heads" and a[0].lower() == "heads") or
                    (response == "Tails" and a[0].lower()[0] == "0") or
                    (response == "Tails" and a[0].lower() == "false") or
                    (response == "Tails" and a[0].lower() == "tails")):
                text = "Woo!  You got:"
            else:
                text = "That's a shame, it landed on:"
        embed.add_field(name="{}".format(text), value="**{}**".format(response), inline=False)
        await ctx.send(embed=embed)
        if not excluded(ctx.author.id) and gets_point:
            user_point(ctx.author.id, 1)
        level_text(ctx, 5)

@bot.command(name='d')
async def roll_die(ctx, *a):
    if bot_data['enabled']['random']:
        response = Misc.roll_dice(a)
        await ctx.send(response)
        level_text(ctx, 5)


bot.run(TOKEN)
