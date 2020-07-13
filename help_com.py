import discord

char = '-'

help_dict = {
        #'' : '\n{}\n'.format(char),
        # Help
        'help' : "\n**Let Brrt help you talk to Brrt:**\n{}\n".format(char),
        # Documentation
        'source' : "Brrt source code\nOptional arguments:\n**(guts, read, tools)**\n{}\n".format(char),
        'c' : "C docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'c#' : "C# docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'c++' : "C++ docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'java' : "Java docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'javascript' : "Javascript docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'lua' : "Lua docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'perl' : "Perl docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'python' : "Python docs\nOptional arguments:\n**(index, module, glossary)**\n{}\n".format(char),
        'ruby' : "Ruby docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'rust': "Rust docs\nOptional arguments:\n**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n".format(char),
        # Social
        'broadcast' : "Brrt will broadcast a message!\nRequired arguments:\n**(channel, message)**\n{}\n".format(char),
        'embed' : "Brrt will embed a message for you, and even include a target!\nRequired arguments:\n**(target, message)**\n{}\n".format(char),
        'echo' : "Brrt will copy you!\nRequired arguments:\n**(message)**\n{}\n".format(char),
        'banter' : "Brrt will slander you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        'praise' : "Brrt will praise you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        # Voting
        'vote' : 'Brrt will take your vote!\n{}\n'.format(char),
        # Random
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
