helper2 = {
        ### All ###
        '' : 'banter, banter <>\npraise, praise <>\nd <>\n',
        ### Misc. ###
        
        # Banter
        'banter' : "",
        'banter <>' : "",
        # Praise
        'praise' : "",
        'praise <>' : "",
        # Roll Die
        'd <>' : "",

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
    embed=discord.Embed(title="Brrt Help", url="https://github.com/ihave13digits/Brrt/blob/master/README.md")
    embed.add_field(name="undefined", value="undefined", inline=False)
    return embed
    