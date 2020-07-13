from discord import Embed

char = '-'

docs_dict = {
        #'' : '\n{}\n'.format(char),
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
        }

help_dict = {
        #'' : '\n{}\n'.format(char),
        # Help
        'help' : "\nLet Brrt help you talk to Brrt.\n{}\n".format(char),
        'docs' : "\nLet Brrt help you find documentation.\n{}\n".format(char),
        # Social
        'broadcast' : "Brrt will broadcast a message!\nRequired arguments:\n**(channel, message)**\n{}\n".format(char),
        'embed' : "Brrt will embed a message for you, and even include a target!\nRequired arguments:\n**(target, message)**\n{}\n".format(char),
        'echo' : "Brrt will copy you!\nRequired arguments:\n**(message)**\n{}\n".format(char),
        'banter' : "Brrt will slander you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        'praise' : "Brrt will praise you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        # Voting
        'vote' : 'Brrt will take your vote!\n{}\n'.format(char),
        # Random
        'flip' : "Brrt will flip his lucky coin for you!\n{}\n".format(char),
        'd' : "Brrt will roll dice for you!\nOptional arguments:\n**(arg1=die sides, arg2=roll count)**\n{}\n".format(char),
        }



def helper(a, mode):
    embed=Embed(title="Brrt {}".format(mode).upper(), url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=0xd421c8)
    if mode == "docs":
        target = docs_dict
    if mode == "help":
        target = help_dict
    try:
        embed.add_field(name=a[0], value=target[a[0]], inline=False)
    except:
        for x in target:
            embed.add_field(name=x, value=target[x], inline=False)
    
    embed.set_footer(text="Brrt ||")
    return embed
