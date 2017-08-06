import discord

client = discord.Client()

token = input('gib token')

@client.event
async def on_message(message):
    await message.channel.send(f'fuck you {message.author.mention}')

client.run(token)