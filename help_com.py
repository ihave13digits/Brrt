import discord

all_commands = [
        'banter, ','banter <>\n\n',
        'praise, ', 'praise <>\n\n',
        'd\n\n',
        'source, ', 'source guts, ', 'source read, ', 'source tools\n\n',
        'python, ', 'python index, ', 'python module, ', 'python glossary\n\n',
        ]

help_dict={

    "help":"Displays this message",
    "rust":"Links to rust docs, accepts (mod, error, rustc, edition, rustdoc, foreword, standard) as optional args",
    "python":"Links to python docs, accepts **(index, module, glossary)** as optional args",
    "source": "Links the bot source code, accepts **(guts, read, tools)** as optional args",
    "banter":"banter_ext",
    "praise":"praise_ext"
}



def helper(a):
    embed=discord.Embed(title="Brrt Help", url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=0xd421c8)
    try:
        arg1= a[0]
        print(arg1)
        embed.add_field(name=arg1, value=help_dict[arg1], inline=False)
    except:
        for x in help_dict:
            embed.add_field(name=x, value=help_dict[x], inline=False)
    
    embed.set_footer(text="Brrt ||")
    return embed
