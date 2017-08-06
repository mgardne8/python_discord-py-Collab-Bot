import discord

client = discord.Client()

token = input('gib token')

rude_people = [122122926760656896, 103675685343612928] # devon and borked

@client.event
async def on_message(message):
    await message.channel.send(f'fuck you {message.author.mention}')

    if message.author.id in rude_people:
        await message.channel.send('double fuck you')

client.run(token)
