import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_redy():
    print(f'We have logged in as {client.user}')


client.run('MTAxMTk4MjIyNjI3NzI5MDA0NA.GYaokW.OMoc3TtSxnEiJjDC-vQvw5fqr6_L4mqvCfrCRM')