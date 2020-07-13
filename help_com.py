import discord

char = '-'

help_dict = {
        'help' : "\n**Let Brrt help you talk to Brrt:**\n{}\n".format(char),
        #
        'source' : "Brrt source code\nOptional arguments:\n**(guts, read, tools)**\n{}\n".format(char),
        'c' : "C docs\nOption arguments:\n**()**\n{}\n".format(char),
        'c#' : "C# docs\nOption arguments:\n**()**\n{}\n".format(char),
        'c++' : "C++ docs\nOption arguments:\n**()**\n{}\n".format(char),
        'java' : "Java docs\nOption arguments:\n**()**\n{}\n".format(char),
        'javascript' : "Javascript docs\nOption arguments:\n**()**\n{}\n".format(char),
        'lua' : "Lua docs\nOption arguments:\n**()**\n{}\n".format(char),
        'perl' : "Perl docs\nOption arguments:\n**()**\n{}\n".format(char),
        'python' : "Python docs\nOptional arguments:\n**(index, module, glossary)**\n{}\n".format(char),
        'ruby' : "Ruby docs\nOption arguments:\n**()**\n{}\n".format(char),
        'rust': "Rust docs\nOptional arguments:\n**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n".format(char),
        # Fun
        'banter' : "Brrt will slander you or your entry!\n{}\n".format(char),
        'praise' : "Brrt will praise you or your entry!\n{}\n".format(char),
        #
        'd' : "Brrt will roll dice for you!\nOptional arguments:\n**(arg1=die sides, arg2=roll count)**\n{}\n".format(char),
        }



def helper(a):
    embed=discord.Embed(title="Brrt Help", url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=0xd421c8)
    try:
        embed.add_field(name=a[0], value=help_dict[a[0]], inline=False)
    except:
        for x in help_dict:
            embed.add_field(name=x, value=help_dict[x], inline=False)
    
    embed.set_footer(text="Brrt ||")
    return embed
