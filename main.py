import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_redy():
    print(f'We have logged in as {client.user}')



client.run()