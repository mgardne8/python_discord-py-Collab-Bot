import discord
from discord.ext import commands

# For future use
# Do not modify unless you understand
# startup_extensions = []

# useless comment for a useless push

# Make sure we have an overused and annoying prefix
# Add useless description
client = commands.Bot(command_prefix="", description="Hi! I'm a bot.")

# Unnecessary, we have a token. See bottom.
# token = input('gib token')

# Agreed
rude_people = [122122926760656896, 103675685343612928] # devon and borked

# You must always be willing to lay your law down
@client.event
async def on_message(message):
    await message.channel.send(f'fuck you {message.author.mention}')

    if message.author.id in rude_people:
        # Seriously, fuck you
        await message.channel.send('double fuck you')

# Obligatory Load Command that gives no feedback
@client.command()
async def load(ctx, what : str):
    """Load a Module"""
    try:
        bot.load_extension(what)
    except ImportError as e:
        pass

# Obligatory Unload Command that gives no feedback
@client.command()
async def unload(ctx, what : str):
    """Unload Modules"""
    bot.unload_extension(what)

# Everyone needs a command to disconnect their bot, let's make ours frustrating
@client.command()
async def hidethepainharoldandkillyourself(ctx):
    """Kill the selfbot and potentially end harold's suffering"""
    await bot.logout()

# Obligatory status editing command
@client.command()
async def status(ctx, what : str):
    """Set status"""
    await ctx.message.delete()
    if bot.is_ready():
        await bot.change_presence(game=discord.Game(name=what))

# Obligatory on ready, make sure this gives a super inane message
@client.event
async def on_ready():
    print("Yo boi! We up in dis, fam!")

# Obligatory notice when command not found
@client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandNotFound):
        await ctx.send(f'{ctx.invoked_with} is not a valid command.')

# Unnecessary namespace comparison for future use
# Definitely do not edit if unsure of purpose
if __name__ == "__main__":
    pass

    # Obligatory token inclusion
    # Is this a real token?
    # I don't know, who is going to actually try it out?
    client.run("W10xv01289Gqw01tVas078510vASG07vb123tVa0sg701gv13t07va")
