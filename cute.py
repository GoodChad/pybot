import os, discord;
from discord.ext import commands;
from dotenv import load_dotenv
intents = discord.Intents.all()
intents.members = True
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client(intents = intents)

print("Mirty is throwing the bot together... discord.py ver is: " + str(discord.__version__))


@client.event
async def on_ready():
    
    print(f'{client.user} has connected to discord')
    for guild in client.guilds:
        if guild.name == GUILD:
            break;
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )



@client.event
async def on_member_join(member):
    print(f"member joined {member.name}");
    coolchannel = client.get_channel(912760101851500567);
    await coolchannel.send(f"{member.name} joined, I'll assign them a role");
    role = discord.utils.get(member.guild.roles, name="METS FAN")
    await member.add_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content == "bruh"):
        await message.channel.send('bruh')
        join('bruh');




client.run(TOKEN)