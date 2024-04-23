
import discord
from discord.ext import commands
from discord.utils import get 
import asyncio
import os
import googletrans 
from googletrans import Translator

BotToken = " " #hidden because public file
ChannelID = 1052761133846630491


bot = commands.Bot(command_prefix = "g", intents = discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True


#do stuff
@bot.event
async def on_ready():  #BOT ONLINE
    print("wassup")
    channel = bot.get_channel(ChannelID)
    await channel.send("Wassup Beetches")

@bot.command()         # BOT SAY HAI
async def hello(ctx):
    await ctx.send("Hai :3")

@bot.command()       #bot add numbers
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)

    await ctx.send(result)

@bot.command()     #telling my friend kurumi to shut up <3 
async def kurumi(ctx):
    await ctx.send("Shut up Kurumi")

@bot.command()     #displays all commands so far
async def commands(ctx):
    await ctx.send("add (numbers), hello, kurumi, translate (language) (text)")

translator = googletrans.Translator()

@bot.command() #IT WORKS I AM SO HAPPY
async def translate(ctx, lang, *, text):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    await ctx.send(translation.text)
    
        
    
bot.run(BotToken)
