import discord
from discord.ext import commands
import random
import aiohttp
import json
from urllib.parse import quote

from utils.checks import *


api_key = "YOUR TENOR API KEY"


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        # Most of the commands in this cog were similar so i removed most of them lol.


#------------------------------------------------------HUG Command
    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def hug(self, ctx, user:discord.Member):
        """
        Fetches a gif from Tenor api.
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.hug.reset_cooldown(ctx) #Cooldown reset
                return await ctx.reply("You hugged yourself. You should feel better now~")

            response = await session.get(f"https://g.tenor.com/v1/search?q=anime+hug&key={api_key}&limit=15&media_filter=basic") # Base request url. You can add more queries with `&query`.
            
            if response.status != 200:
                self.hug.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                gifs = await response.json()
                r_gif = random.choice(gifs["results"])
                m_gif = r_gif["media"]
                gif = list(map(lambda d: d['gif'], m_gif)) # You can also use for statements instead of map and lambda
                url = list(map(lambda d: d['url'], gif))
                
                embed = discord.Embed(title=f"{ctx.author} gives a warm hug to {user}!", url=str(url[0]), color=0x5474b4)
                embed.set_image(url=str(url[0]))
                embed.set_footer(text="Powered by tenor.com")
                return await ctx.send(embed=embed)
    
    @hug.error                                   #Hug error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            self.hug.reset_cooldown(ctx)
            return await ctx.reply("You forgot to mention somebody..")


#------------------------------------------------------CRY Command
    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cry(self, ctx):
        """
        Fetches a gif from Tenor api.
        """
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"https://g.tenor.com/v1/search?q=anime+crying&key={api_key}&limit=15&media_filter=basic")
            if response.status != 200:
                self.cry.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                gifs = json.loads(await response.text())
                r_gif = random.choice(gifs["results"])
                m_gif = r_gif["media"]
                gif = list(map(lambda d: d['gif'], m_gif))
                url = list(map(lambda d: d['url'], gif))
                
                embed = discord.Embed(title=f"{ctx.author} is crying ;-;", url=str(url[0]), color=0x5474b4)
                embed.set_image(url=str(url[0]))
                embed.set_footer(text="Powered by tenor.com")
                return await ctx.send(embed=embed)


#------------------------------------------------------OWOIFY
    @commands.command(aliases=["owo", "owofy"])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def owoify(self, ctx, *, args: str):
        """

        Owoify your sentences.

        """
        async with aiohttp.ClientSession() as session:
            enc_arg = quote(args)
            res = await session.get(f"https://www.nekos.life/api/v2/owoify?text={enc_arg}") #nekos.life api
            if res.status != 200:
                self.owoify.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                reply = await res.json()
                return await ctx.reply(reply["owo"], mention_author=False)

    @owoify.error                                #Owoify error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            self.owoify.reset_cooldown(ctx)
            return await ctx.reply("What do you want me to owoify, hmph!!")

            


def setup(client):
    client.add_cog(Fun(client))