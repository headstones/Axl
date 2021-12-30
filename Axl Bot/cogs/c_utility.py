import discord, datetime
from discord.ext import commands
e_color = 0x292929



class utility(commands.Cog):
    def __innit__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(bot):
        print('c_utility is online.')







def setup(bot):
    bot.add_cog(utility(bot))
