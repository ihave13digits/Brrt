import discord

all_commands = [
        'banter, ','banter <>\n\n',
        'praise, ', 'praise <>\n\n',
        'd\n\n',
        'source, ', 'source guts, ', 'source read, ', 'source tools\n\n',
        'python, ', 'python index, ', 'python module, ', 'python glossary\n\n',
        'rust, ', 'rust mod, ', 'rust error, ', 'rust rustc,\n', 'rust edition, ', 'rust rustdoc, ', 'rust foreword, ', 'rust standard\n\n'
        ]

help_dict={
    #"help":"Displays this message"
        ### All ###
        'help' : str(all_commands),
        ### Misc. ###

        # Banter
        'banter' : "",
        'banter ' : "",
        # Praise
        'praise' : "",
        'praise ' : "",
        # Roll Die
        'd' : "",

        ### Docs. ###

        # Source
        'source' : "",
        'source guts' : "",
        'source read' : "",
        'source tools' : "",
        # Python
        'python' : "",
        'python index' : "",
        'python module' : "",
        'python glossary' : "",
        # Rust
        'rust' : "",
        'rust mod' : "",
        'rust error' : "",
        'rust rustc' : "",
        'rust edition' : "",
        'rust rustdoc' : "",
        'rust foreword' : "",
        'rust standard' : "",
    }



def helper(a):
    embed=discord.Embed(title="Brrt Help", url="https://github.com/ihave13digits/Brrt/blob/master/README.md", color=0xd421c8)
    try:
        arg1= a[0]
        embed.add_field(name=a, value=help_dict[a], inline=False)
    except:
        for x in help_dict:
            embed.add_field(name=x, value=help_dict[x], inline=False)
    
    embed.set_footer(text="Brrt ||")
    return embed
