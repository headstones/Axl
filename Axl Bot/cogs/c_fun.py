import discord, datetime, time
from discord.ext import commands
import random
from aiohttp import ClientSession
import asyncio
from dotenv import load_dotenv
import os
start_time = time.time()
utctime = datetime.datetime.utcnow()
e_color = 0x292929
load_dotenv()
API_KEY = os.getenv('API_KEY')


class utility(commands.Cog):
    def __innit__(ctx, bot):
        ctx.bot = bot

    # cog online msg
    @commands.Cog.listener()
    async def on_ready(bot):
        print('c_fun is online.')
    
    # random number generator
    @commands.command(name='random', aliases=['rand', 'rng'], case_insensitive=True)
    async def random(self, ctx, min: int, max: int):
        await ctx.send(random.randint(min, max))

    # coinflip
    @commands.command(name='coinflip', aliases=['cf'], case_insensitive=True)
    async def coinflip(self, ctx):
        await ctx.send(random.choice(['heads', 'tails']))
        
    #dice roll
    @commands.command(name='roll', aliases=['dice'])
    async def roll(self, ctx, sides: int):
        await ctx.send(random.randint(1, sides))

    #urban dictionary
    @commands.command(name='urban', aliases=['ud'], case_insensitive=True)
    async def urbandictionary(self, ctx, *args):
        term = " ".join(args[0:len(args)])
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term}

        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as response:
                data = await response.json()
                if data['list'] == []:
                    await ctx.send(f'No results found for {term}')
                else:
                    embed = discord.Embed(title=f'{term}', description=data['list'][0]['definition'], color=e_color)
                    embed.set_footer(text=f'{data["list"][0]["example"]}')
                    await ctx.reply(embed=embed, mention_author=False)
    #send dm to user
    @commands.command(name='dm', aliases=['dms', 'mail', 'dmuser'], case_insensitive=True)
    async def dm(self, ctx, user: discord.Member, *, message):
        await user.send(message)
        await ctx.reply(f'Message sent to {user}.', mention_author=False)

def setup(bot):
    bot.add_cog(utility(bot))
