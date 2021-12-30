import os
import discord, datetime, time
from discord.ext import commands, tasks
from asyncio import sleep
from discord import __version__ as discord_version
from platform import python_version
import sys
from discord.flags import Intents
from dotenv import load_dotenv
import random
import asyncio
start_time = time.time()
utctime = datetime.datetime.utcnow()
logchannelid = 901885377772650526
guildid = 783068110134837295
bot = commands.Bot(command_prefix = "-", case_Insensitive=True)
bot.remove_command('help')

# load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#unload cog
@bot.command(name='unload', aliases=['unloadcog'], case_insensitive=True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'{extension} unloaded.')
    await ctx.send(f'Unloaded {extension}')

#load cog
@bot.command(name='load', aliases=['loadcog'], case_insensitive=True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f"Loaded {extension}.")
    await ctx.send(f'Loaded {extension}')

#reload cog
@bot.command(name='reload', aliases=['reloadcog'], case_insensitive=True)
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    print(f"Reloaded {extension}.")
    await ctx.send(f'Reloaded {extension}')

#reload all cogs
@bot.command(name='reloadall', aliases=['reloadallcogs', 'somethingbrokeplsfix', 'update'], case_insensitive=True)
@commands.is_owner()
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            print(f"Reloaded {filename[:-3]}.")
    await ctx.send(f'Reloaded all cogs.')

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("Discord.py version: " + discord_version)
    print("Python version: " + python_version())
    print("-----------------------------------------------------")

# status rotator
async def ch_pr():
    await bot.wait_until_ready()
    statuses = ["with my code.", "with your toes.", "with Russian nuke codes."]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(15)
bot.loop.create_task(ch_pr())

load_dotenv()
token = os.getenv('BOT_KEY')
bot.run(token)