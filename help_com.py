import discord

char = '-'

help_dict = {
        "help":"\n{}\n**Let Brrt help you talk to Brrt:**\n{}\n{}\n{}".format(char, char, char, char),
        "rust":"Rust docs\n{}\nOptional arguments:\n**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n{}\n{}".format(char, char, char, char),
        "python":"Python docs\n{}\nOptional arguments:\n**(index, module, glossary)**\n{}\n{}\n{}".format(char, char, char, char),
        "source": "Brrt source code\n{}\nOptional arguments:\n**(guts, read, tools)**\n{}\n{}\n{}".format(char, char, char, char),
        "banter":"Brrt will slander you or your entry!\n{}\n{}\n{}".format(char, char, char),
        "praise":"Brrt will praise you or your entry!\n{}\n{}\n{}".format(char, char, char)
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
