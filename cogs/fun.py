import discord
from discord.ext import commands
import aiohttp
from utils.checks import *


base = "https://api.waifu.pics/sfw/"


class Roleplay(commands.Cog):
    """
    Roleplay commands!
    """
    def __init__(self, client):
        self.client = client
        self.emoji = "💃"


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def wave(self, ctx, user: discord.Member):
        """
        Wave at someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.wave.reset_cooldown(ctx)
                return await ctx.reply("You wave at yourself.")
            res = await session.get(base + "wave")
            if res.status != 200:
                self.wave.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} waves at {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def wink(self, ctx, user: discord.Member):
        """
        Wink at someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.wink.reset_cooldown(ctx)
                return await ctx.reply("You wink at yourself.")
            res = await session.get(base + "wink")
            if res.status != 200:
                self.wink.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} winks at {user}. Such a sussy baka!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def hug(self, ctx, user: discord.Member):
        """
        Give a hug to someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.hug.reset_cooldown(ctx)
                return await ctx.reply("You hug yourself.")
            res = await session.get(base + "hug")
            if res.status != 200:
                self.hug.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} gives a hug to {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cuddle(self, ctx, user: discord.Member):
        """
        Cuddle with someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.cuddle.reset_cooldown(ctx)
                return await ctx.reply("You cuddle with yourself.")
            res = await session.get(base + "cuddle")
            if res.status != 200:
                self.cuddle.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} cuddles with {user}!!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["headpat"])
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def pat(self, ctx, user: discord.Member):
        """
        Give a pat to someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.pat.reset_cooldown(ctx)
                return await ctx.reply("You pat yourself.")
            res = await session.get(base + "pat")
            if res.status != 200:
                self.pat.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} pats {user}. So cute!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def poke(self, ctx, user: discord.Member):
        """
        Poke someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.poke.reset_cooldown(ctx)
                return await ctx.reply("You poke yourself.")
            res = await session.get(base + "poke")
            if res.status != 200:
                self.poke.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} pokes {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def slap(self, ctx, user: discord.Member):
        """
        Slap someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.slap.reset_cooldown(ctx)
                return await ctx.reply("You slap yourself.")
            res = await session.get(base + "slap")
            if res.status != 200:
                self.slap.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} slaps {user}! Nani?!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def bonk(self, ctx, user: discord.Member):
        """
        Bonk someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.bonk.reset_cooldown(ctx)
                return await ctx.reply("You bonk yourself.")
            res = await session.get(base + "bonk")
            if res.status != 200:
                self.bonk.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} bonks {user}. Yamete!!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def nom(self, ctx, user: discord.Member):
        """
        Nom someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.nom.reset_cooldown(ctx)
                return await ctx.reply("You nom yourself.")
            res = await session.get(base + "nom")
            if res.status != 200:
                self.nom.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} noms {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def bite(self, ctx, user: discord.Member):
        """
        Bite someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.bite.reset_cooldown(ctx)
                return await ctx.reply("You bite yourself.")
            res = await session.get(base + "bite")
            if res.status != 200:
                self.bite.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} bites {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def kick(self, ctx, user: discord.Member):
        """
        Kick someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.kick.reset_cooldown(ctx)
                return await ctx.reply("You kick yourself.")
            res = await session.get(base + "kick")
            if res.status != 200:
                self.kick.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} kicks {user}!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def yeet(self, ctx, user: discord.Member):
        """
        Yeet someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.yeet.reset_cooldown(ctx)
                return await ctx.reply("You yeet yourself.")
            res = await session.get(base + "yeet")
            if res.status != 200:
                self.yeet.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} yeets {user}!!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def bully(self, ctx, user: discord.Member):
        """
        Bully someone! (not recommended)
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.bully.reset_cooldown(ctx)
                return await ctx.reply("You bully yourself.")
            res = await session.get(base + "bully")
            if res.status != 200:
                self.bully.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} bullies {user}. Stop it!!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def kiss(self, ctx, user: discord.Member):
        """
        Give a kiss to someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.kiss.reset_cooldown(ctx)
                return await ctx.reply("You kiss yourself.")
            res = await session.get(base + "kiss")
            if res.status != 200:
                self.kiss.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} gives a kiss to {user}! 😳😳", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def lick(self, ctx, user: discord.Member):
        """
        Lick someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.lick.reset_cooldown(ctx)
                return await ctx.reply("You lick yourself.")
            res = await session.get(base + "lick")
            if res.status != 200:
                self.lick.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} licks {user}. Gross!!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["frick"])
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def fuck(self, ctx, user: discord.Member):
        """
        Perform unholy acts with someone!
        """
        async with aiohttp.ClientSession() as session:
            if user.id == ctx.author.id:
                self.fuck.reset_cooldown(ctx)
                return await ctx.reply("You fuck yourself.")
            res = await session.get(base + "handhold")
            if res.status != 200:
                self.fuck.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} performs unholy acts with {user}.. Get a room!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)



class Action(commands.Cog):
    """
    Action commands!
    """
    def __init__(self, client):
        self.client = client
        self.emoji = "😳"


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cry(self, ctx):
        """
        Cry when you feel sad!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(base + "cry")
            if res.status != 200:
                self.cry.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} is crying. So sad!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def smile(self, ctx):
        """
        Smile when you are happy!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(base + "smile")
            if res.status != 200:
                self.smile.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} is smiling!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["lewd"])
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def blush(self, ctx):
        """
        Blush when you are shy!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(base + "blush")
            if res.status != 200:
                self.blush.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} is blushing. OwO!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def smug(self, ctx):
        """
        Smug when you feel satisfied!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(base + "smug")
            if res.status != 200:
                self.smug.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} is being smug!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cringe(self, ctx):
        """
        Cringe at someting unusual!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(base + "cringe")
            if res.status != 200:
                self.cringe.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                gif = res_json["url"]
                embed = discord.Embed(title=f"{ctx.author} is cringing!", url=gif, color=0x5474b4)
                embed.set_image(url=gif)
                return await ctx.send(embed=embed)





def setup(client):
    client.add_cog(Roleplay(client))
    client.add_cog(Action(client))