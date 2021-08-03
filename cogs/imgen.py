import discord
from discord.ext import commands
import alexflipnote
import aiohttp
from io import BytesIO
import os
from utils.checks import bot_checks


alex_api = alexflipnote.Client(os.environ["alexflipnote_api"]) # ENV Variable in heroku
random_api = os.environ["some_random_api"] # ENV Variable in heroku
dagpi_api = os.environ["dagpi_api"] # ENV Variable in heroku
deep_api = os.environ["deep_api"] # ENV Variable in heroku


class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.emoji = "📷"


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def deepfry(self, ctx, member: discord.Member = None):
        """
        Apply deepfry filter on someone's avatar! [GIF Support]
        """
        msg = await ctx.reply("This might take a while..")
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url
            filename = "None"
            if ".gif" in str(url):
                filename = "gif"
                pass
            elif ".webp" in str(url):
                url = str(url).replace(".webp", ".png")
                filename = "png"
            else:
                filename = "png"
                pass
            res = await session.get(f"https://api.dagpi.xyz/image/deepfry/?url={str(url)}", headers={"Authorization": f"{dagpi_api}"})
            if res.status != 200:
                self.deepfry.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = BytesIO(await res.read())
                await ctx.reply(file = discord.File(img, f"deepfry.{filename}"), mention_author=False)
                return await msg.delete()


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def magik(self, ctx, member: discord.Member = None):
        """
        Apply magik filter on someone's avatar! [GIF Support]
        """
        msg = await ctx.reply("This might take a while..")
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url
            filename = "None"
            if ".gif" in str(url):
                filename = "gif"
                pass
            elif ".webp" in str(url):
                url = str(url).replace(".webp", ".png")
                filename = "png"
            else:
                filename = "png"
                pass
            res = await session.get(f"https://api.dagpi.xyz/image/magik/?url={str(url)}", headers={"Authorization": f"{dagpi_api}"})
            if res.status != 200:
                self.magik.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = BytesIO(await res.read())
                await ctx.reply(file = discord.File(img, f"magik.{filename}"), mention_author=False)
                return await msg.delete()


    @commands.command(aliases=["poster"])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def posterize(self, ctx, member:discord.Member=None):
        """
        Apply poster filter on someone's avatar! [GIF Support]
        """
        msg = await ctx.reply("This might take a while..")
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url
            filename = "None"
            if ".gif" in str(url):
                filename = "gif"
                pass
            elif ".webp" in str(url):
                url = str(url).replace(".webp", ".png")
                filename = "png"
            else:
                filename = "png"
                pass
            res = await session.get(f"https://api.dagpi.xyz/image/poster/?url={str(url)}", headers={"Authorization": f"{dagpi_api}"})
            if res.status != 200:
                self.posterize.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = BytesIO(await res.read())
                await ctx.reply(file = discord.File(img, f"poster.{filename}"), mention_author=False)
                return await msg.delete()


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def jail(self, ctx, member:discord.Member=None):
        """
        Apply jail filter on someone's avatar! [GIF Support]
        """
        msg = await ctx.reply("This might take a while..")
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url
            filename = "None"
            if ".gif" in str(url):
                filename = "gif"
                pass
            elif ".webp" in str(url):
                url = str(url).replace(".webp", ".png")
                filename = "png"
            else:
                filename = "png"
                pass
            res = await session.get(f"https://api.dagpi.xyz/image/jail/?url={url}", headers={"Authorization": f"{dagpi_api}"})
            if res.status != 200:
                self.jail.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = BytesIO(await res.read())
                await ctx.reply(file = discord.File(img, f"jail.{filename}"), mention_author=False)
                return await msg.delete()


    @commands.command(aliases=["triggered"])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def trigger(self, ctx, member:discord.Member=None):
        """
        Apply trigger filter on someone's avatar! [No GIF Support]
        """
        msg = await ctx.reply("This might take a while..")
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url_as(format="png", size=1024)
            res = await session.get(f"https://api.dagpi.xyz/image/triggered/?url={url}", headers={"Authorization": f"{dagpi_api}"})
            if res.status != 200:
                self.trigger.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = BytesIO(await res.read())
                await ctx.reply(file = discord.File(img, f"poster.gif"), mention_author=False)
                return await msg.delete()


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def denoise(self, ctx, member:discord.Member=None):
        """
        Remove noise from someone's avatar! [No GIF Support]
        """
        async with aiohttp.ClientSession() as session:
            if not member:
                member = ctx.author
            url = member.avatar_url_as(format="png", size=1024)
            res = await session.post("https://api.deepai.org/api/waifu2x", data={'image': str(url)}, headers={'api-key': f'{deep_api}'})
            if res.status != 200:
                self.denoise.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                new_url = res_json["output_url"]
                return await ctx.send(new_url)


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cat(self, ctx):
        """
        Random cat image!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get("https://cataas.com/cat/cute?json=true")
            if res.status != 200:
                self.cat.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = await res.json()
                img_id = img["id"]
                url = f"https://cataas.com/cat/{img_id}"
                embed = discord.Embed(title="Cattos!", url=url, color=0x5474b4)
                embed.set_image(url=url)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["bird"])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def birb(self, ctx):
        """
        Random bird image!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get(f"https://some-random-api.ml/img/birb?key={random_api}")
            if res.status != 200:
                self.bird.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                img = await res.json()
                embed = discord.Embed(title="Birbs!", url=img["link"], color=0x5474b4)
                embed.set_image(url=img["link"])
                return await ctx.send(embed=embed)


    @commands.command()
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def dog(self, ctx):
        """
        Random dog image!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get("https://dog.ceo/api/breeds/image/random")
            img = await res.json()
            if res.status != 200:
                self.dog.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                url = img["message"]
                embed = discord.Embed(title="Doggo!", url=url, color=0x5474b4)
                embed.set_image(url=url)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["catgirl"])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def neko(self, ctx):
        """
        Random cat-girl image!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get("https://neko-love.xyz/api/v1/neko")
            if res.status != 200:
                self.neko.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                url = res_json["url"]
                embed = discord.Embed(title="Cute and friendly nekos~", url=url, color=0x5474b4)
                embed.set_image(url=url)
                return await ctx.send(embed=embed)


    @commands.command(aliases=["foxgirl"])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def kitsune(self, ctx):
        """
        Random fox-girl image!
        """
        async with aiohttp.ClientSession() as session:
            res = await session.get("https://neko-love.xyz/api/v1/kitsune")
            if res.status != 200:
                self.kitsune.reset_cooldown(ctx)
                return await ctx.reply("Something went wrong..", delete_after=5)
            else:
                res_json = await res.json()
                url = res_json["url"]
                embed = discord.Embed(title="Cute and friendly kitsunes~", url=url, color=0x5474b4)
                embed.set_image(url=url)
                return await ctx.send(embed=embed)





def setup(client):
    client.add_cog(Image(client))