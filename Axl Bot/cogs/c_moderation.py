import os
from asyncio.subprocess import Process
import discord, datetime, time
import asyncio as asyncio
from discord.errors import Forbidden
from discord.ext import commands
from discord.ext.commands import Bot, cog
from asyncio import sleep
from discord import __version__ as discord_version
import re
import string
from platform import python_version
import random
start_time = time.time()
utctime = datetime.datetime.utcnow()

class utility(commands.Cog):
    def __innit__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(bot):
        print('c_moderation is online.')

    #kick member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')

def setup(bot):
    bot.add_cog(utility(bot))