import discord, datetime, time
from discord.ext import commands
e_color = 0x292929
class error(commands.Cog):
    def __innit__(self, bot):
        self.bot = bot

    # bot online msg
    @commands.Cog.listener()
    async def on_ready(bot):
        print('c_error is online.')
    #error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title="Command Error.", color=e_color, description= f"{str(error)}")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/917586758080790538/923809793641173003/tvsad.png")
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(error(bot))