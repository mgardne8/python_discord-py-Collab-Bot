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

rude_people = [122122926760656896, 103675685343612928] # devon and borked

@client.event
async def on_message(message):
        """
        Just fuck everything
        
        Note
        ----
            Seriously fuck devon and borked
        
        """
    await message.channel.send(f'fuck you {message.author.mention}')

    if message.author.id in rude_people:
        await message.channel.send('double fuck you')

@client.command()
async def load(ctx, what : str):
        """
        Load the given module as a cog
         
        Parameters
        ----------
        what : str
            Thing cog you are trying to load
        
        Note
        ----
            Exception handling not included
        
        Todo
        -------
            Implement Error Handling
        """
    try:
        bot.load_extension(what)
    except ImportError as e:
        pass

    
@client.command()
async def unload(ctx, what : str):
        """
        Unload the given cog
        
        Parameters
        ----------
        what : str
            Thing cog you are trying to unload
        
        Note
        ----
            Exception handling not included
        
        Todo
        -------
            Make this not shit
        """
    bot.unload_extension(what)

@client.command()
async def hidethepainharoldandkillyourself(ctx):
        """
        Kill the bot and possibly harold
        
        Note
        ----
            May or may not kill Harold also
        
        Todo
        -------
            Make this only kill harold, not the bot
        """
    await bot.logout()

@client.command()
async def status(ctx, what : str):
        """
        Set the bots status to the given thing
        
        Parameters
        ----------
        what : str
            Thing you are setting as your bots new status
        
        Note
        ----
            Exception handling not included
        
        Todo
        -------
            Make this not shit
        """
    await ctx.message.delete()
    if bot.is_ready():
        await bot.change_presence(game=discord.Game(name=what))

@client.event
async def on_ready():
    """"Runs when the bot is ready and notifies you of said readyness in whatever you have set as your standard output"""
    print("Yo boi! We up in dis, fam!")

@client.event
async def on_command_error(ctx, err):
    """Notifies you when you attempt to run an invalid command"""
    if isinstance(err, commands.CommandNotFound):
        await ctx.send(f'{ctx.invoked_with} is not a valid command.')

if __name__ == "__main__":
    """Unnecessary namespace comparison for future use"""

    client.run("W10xv01289Gqw01tVas078510vASG07vb123tVa0sg701gv13t07va")
    """
    Is this a real token? 
    I don't know, who is going to actually try it out?
    """
