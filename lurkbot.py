import discord
from discord.ext import commands
from discord.ext.commands import Bot
#from discord.ext.commands import Command_Prefix
import asyncio
client = discord.Client()
#bot = commands.Bot(command_prefix('.'))

@client.event
async def on_ready():
    print("Bot Online") 
    await client.change_presence(game=discord.Game(name="In the Shadows..."))
    #await client.send_message(discord.Object(id='CHANNELID'), "**You feel an evil presence watching you...**")

#test command
#@bot.command()
#async def ping():
    #await bot.say("what is it?")

#Basic Hello World style message
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content == "habla":
        await client.send_message(message.channel, "habla")
    if message.content == "hello":
        await client.send_message(message.channel, "world")
    if message.content == "shut up":
        await client.send_message(message.channel, "you shut up")
    if message.content == "no u":
        await client.send_message(message.channel, "no u")


#bot token - do not leak
client.run("BOTTOKENGOESHERE")