import discord
from discord.ext import commands
from time import monotonic
from utils.checks import bot_checks


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def ping(self, ctx):
        """
        Displays client and message latency.
        """
        embed1=discord.Embed(color=discord.Color.default(), title='Bot Latency', description='Pinging...')
        start = monotonic()
        message = await ctx.reply(embed=embed1)
        end = monotonic()
        ping = (end-start)*1000
        embed2=discord.Embed(color=ctx.author.color, title='Bot Latency')
        embed2.add_field(name='Discord Latency', value=f'```\n{round(self.client.latency * 1000)}\n```')
        embed2.add_field(name='Message Latency', value=f'```\n{round(ping)}\n```')
        return await message.edit(embed=embed2)





def setup(client):
    client.add_cog(Misc(client))