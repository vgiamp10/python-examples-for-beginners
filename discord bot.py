#start bot
import discord
from discord.ext import commands
from yarl import URL
import youtube_dl
import random
import os

client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    print(f"the bot is connected")


#commands
#hello
@client.command()
async def Hello(ctx):
    await ctx.send("Hello world!")
#Laugh
@client.command()
async def Laugh(ctx):
    await ctx.send("😂😁😀😂😂😂😂")
#if you are using this py file as a template, remember to move the client.run at the bottom of the script
client.run("YOUR_BOT_TOKEN")