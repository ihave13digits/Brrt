import discord

help_dict={
    "help":"Displays this message"
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