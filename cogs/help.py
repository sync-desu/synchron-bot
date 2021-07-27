import discord
from discord.ext import commands
import json
from utils.checks import bot_checks


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        client.remove_command("help")

    
#------------------------------------------------------MAIN HELP GROUP
    @commands.group(name="help", invoke_without_command=True)
    @bot_checks.embed_check()
    async def helping(self, ctx):
        """

        Help command group.

        """
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed = discord.Embed(description=f"Type `{pfx}help <command_or_category>` for more information.", color=0x5474b4)
        embed.add_field(name="😏 | Fun", value=f"`{pfx}help fun`\n[Fun Commands](https://www.dictionary.com/browse/help)")
        embed.add_field(name="📷 | Image", value=f"`{pfx}help image`\n[Image Commands](https://www.dictionary.com/browse/help)")
        embed.add_field(name="🛠️ | Utility", value=f"`{pfx}help utility`\n[Utility Commands](https://www.dictionary.com/browse/help)")
        embed.add_field(name="🔴 | Misc", value=f"`{pfx}help misc`\n[Misc Commands](https://www.dictionary.com/browse/help)")
        embed.set_author(name="SyNchr0n Help Menu", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f'SyNchr0n by ឵sync឵#9074')
        return await ctx.send(embed=embed)


#------------------------------------------------------HELP CATEGORIES
    @helping.command()
    @bot_checks.embed_check()
    async def fun(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"Type `{pfx}help <command>` for more information.", color=0x5474b4)
        embed.add_field(name="Roleplay:", value=f"[Interact with others!](https://www.dictionary.com/browse/help)\n`{pfx}hug`, `{pfx}cuddle`, `{pfx}pat`, `{pfx}poke`, `{pfx}slap`, `{pfx}spank`, `{pfx}kiss`, `{pfx}lick`, `{pfx}fuck`")
        embed.add_field(name="Actions:", value=f"[Express your emotions!](https://www.dictionary.com/browse/help)\n`{pfx}cry`, `{pfx}laugh`, `{pfx}smile`, `{pfx}stare`, `{pfx}lewd`, `{pfx}smug`", inline=False)
        embed.add_field(name="Other:", value=f"[Other fun commands!](https://www.dictionary.com/browse/help)\n`{pfx}owoify`", inline=False)
        embed.set_author(name="Fun Commands", icon_url=self.client.user.avatar_url)
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.send(embed=embed)


    @helping.command(aliases=["imgen", "img"])
    @bot_checks.embed_check()
    async def image(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"Type `{pfx}help <command>` for more information.", color=0x5474b4)
        embed.add_field(name="Imgen:", value=f"[Image generation/manipulation!](https://www.dictionary.com/browse/help)\n`{pfx}deepfry`, `{pfx}magik`, `{pfx}posterize`, `{pfx}jail`, `{pfx}trigger`", inline=False)
        embed.add_field(name="Animals:", value=f"[Animals/Pets images!](https://www.dictionary.com/browse/help)\n`{pfx}cat`, `{pfx}birb`, `{pfx}dog`", inline=False)
        embed.add_field(name="Degenerate shit:", value=f"[Catgirl/Foxgirl images!](https://www.dictionary.com/browse/help)\n`{pfx}neko`, `{pfx}kitsune`", inline=False)
        embed.set_author(name="Image commands", icon_url=self.client.user.avatar_url)
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.send(embed=embed)
    

    @helping.command(aliases=["utils"])
    @bot_checks.embed_check()
    async def utility(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"Type `{pfx}help <command>` for more information.", color=0x5474b4)
        embed.add_field(name="Informative:", value=f"[Informative commands!](https://www.dictionary.com/browse/help)\n`{pfx}avatar`, `{pfx}userinfo`, `{pfx}roleinfo`")
        embed.set_author(name="Utility commands", icon_url=self.client.user.avatar_url)
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.send(embed=embed)


    @helping.command()
    @bot_checks.embed_check()
    async def misc(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"Type `{pfx}help <command>` for more information.", color=0x5474b4)
        embed.add_field(name="Uncategorized:", value=f"[Uncategorized commands!](https://www.dictionary.com/browse/help)\n`{pfx}ping`")
        embed.set_author(name="Misc Commands", icon_url=self.client.user.avatar_url)
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.send(embed=embed)


#------------------------------------------------------


#FUN CATEGORY


#------------------------------------------------------
    @helping.command()
    @bot_checks.embed_check()
    async def hug(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}hug <member>```\n**[Hug somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def cuddle(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}cuddle <member>```\n**[Cuddle somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["headpat"])
    @bot_checks.embed_check()
    async def pat(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}pat <member>\nAliases: headpat```\n**[Pat somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def poke(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}poke <member>```\n**[Poke somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def slap(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}slap <member>```\n**[Slap somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def spank(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}spank <member>```\n**[Spank somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def kiss(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}kiss <member>```\n**[Kiss somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def lick(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}lick <member>```\n**[Discord predator simulator!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["frick"])
    @bot_checks.embed_check()
    async def fuck(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}fuck <member>\nAliases: frick```\n**[Perform unholy acts with somebody!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def cry(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}cry```\n**[Cry when you are sad!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def laugh(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}laugh```\n**[Laugh at something funny!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def smile(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}smile```\n**[Smile when you are happy!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def stare(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}stare```\n**[Stare when you see something sus!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["shy", "flushed", "fluster"])
    @bot_checks.embed_check()
    async def lewd(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}lewd\nAliases: shy, flushed, fluster```\n**[Lewd when you are embarassed!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def smug(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}smug```\n**[Smug when you feel satisfied!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["owofy", "owo"])
    @bot_checks.embed_check()
    async def owoify(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}owoify <argument>\nAliases: owofy, owo```\n**[Owoify your sentences!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`, Bot: `send_messages`", inline=False)
        embed.set_author(name="Fun commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


#------------------------------------------------------


#IMAGE CATEGORY


#------------------------------------------------------
    @helping.command()
    @bot_checks.embed_check()
    async def deepfry(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}deepfry <member>```\n**[Deepfry filter on someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)
        

    @helping.command()
    @bot_checks.embed_check()
    async def magik(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}magik <member>```\n**[Magik filter on someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["poster"])
    @bot_checks.embed_check()
    async def posterize(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}posterize <member>\nAliases: poster```\n**[Poster filter on someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def jail(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}jail <member>```\n**[Jail bars overlay on someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["triggered"])
    @bot_checks.embed_check()
    async def trigger(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}trigger <member>\nAliases: triggered```\n**[Triggered filter on someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def denoise(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}denoise <member>```\n**[Improve quality of someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def cat(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}cat```\n**[Generates random cat images!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["bird"])
    @bot_checks.embed_check()
    async def birb(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}birb\nAliases: bird```\n**[Generates random bird images!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command()
    @bot_checks.embed_check()
    async def dog(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}dog```\n**[Generates random dog images!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["catgirl"])
    @bot_checks.embed_check()
    async def neko(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}neko\nAliases: catgirl```\n**[Generates random neko images!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["foxgirl"])
    @bot_checks.embed_check()
    async def kitsune(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}kitsune```\n**[Generates random kitsune image!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


#------------------------------------------------------


#UTILITY


#------------------------------------------------------
    @helping.command(aliases=["av"])
    @bot_checks.embed_check()
    async def avatar(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}avatar <member>\nAliases: av```\n**[Display someone's avatar!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **3 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`, `Attach Files`", inline=False)
        embed.set_author(name="Utility commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["ui", "whois", "wi"])
    @bot_checks.embed_check()
    async def userinfo(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}userinfo <member>\nAliases: whois, wi, ui```\n**[Get information about someone's account!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **10 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Utility commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


    @helping.command(aliases=["ri"])
    @bot_checks.embed_check()
    async def roleinfo(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}roleinfo <member>\nAliases: ri```\n**[Get information about a role!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Utility commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


#MISC


    @helping.command()
    @bot_checks.embed_check()
    async def ping(self, ctx):
        server = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
        pfx = server["prefix"]

        embed=discord.Embed(description=f"```fix\nSyntax: {pfx}ping```\n**[Shows bot latency!](https://www.dictionary.com/browse/help)**\n\u200b", color=0x5474b4)
        embed.add_field(name="Cooldown(s)", value="Can be used once every **5 seconds** per user")
        embed.add_field(name="Permissions(s)", value="Member: `None`\nBot: `Embed Links`", inline=False)
        embed.set_author(name="Image commands", icon_url=f"{self.client.user.avatar_url}")
        embed.set_footer(text='SyNchr0n by ឵sync឵#9074')
        return await ctx.reply(embed=embed, mention_author=False)


def setup(client):
    client.add_cog(Help(client))