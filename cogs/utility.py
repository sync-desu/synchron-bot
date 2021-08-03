import discord
from discord.ext import commands
import datetime
from utils.checks import bot_checks, user_checks


class Utility(commands.Cog):
    """
    Utility commands!
    """
    def __init__(self, client):        
        self.client = client
        self.emoji = "🛠️"


    @commands.Cog.listener()
    async def on_ready(self):
        """        
        Creates a table for prefixes if that table does not exist in the database.
        """
        await self.client.db.execute("CREATE TABLE IF NOT EXISTS prefixes (guild_id BIGINT NOT NULL PRIMARY KEY, prefix CHARACTER VARYING NOT NULL)")
        await self.client.db.execute("ALTER TABLE prefixes ADD COLUMN IF NOT EXISTS guild_id BIGINT NOT NULL PRIMARY KEY")
        await self.client.db.execute("ALTER TABLE prefixes ADD COLUMN IF NOT EXISTS prefix CHARACTER VARYING NOT NULL")


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Adds a default prefix on joining a guild if it does not exist in the database.
        """
        prefixes = await self.client.db.fetchrow("SELECT FROM prefixes WHERE guild_id = $1", guild.id)
        if not prefixes:
            default_prefix = "s?"
            await self.client.db.execute("INSERT INTO prefixes (guild_id, prefix) VALUES($1, $2)", guild.id, default_prefix)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Removes the prefix from the database upon leaving the server.
        """
        prefixes = await self.client.db.fetchrow("SELECT FROM prefixes WHERE guild_id = $1", guild.id)
        if not prefixes:
            return
        else:
            await self.client.db.execute("DELETE FROM prefixes WHERE guild_id = $1", guild.id)


    @commands.command(aliases=['av'])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def avatar(self, ctx, member:discord.Member=None):
        """
        Display someone's avatar!
        """
        if not member:
            member = ctx.author
        av_jpg = str(member.avatar_url_as(static_format="jpg", size=1024))
        av_webp = str(member.avatar_url_as(static_format="webp", size=1024))
        av_png = str(member.avatar_url_as(static_format="png", size=1024))
        embed=discord.Embed(
            color=0x5474b4, title=f'Avatar for {member}', 
            description=f"**Other format**:\n[png]({av_png}) | [jpg]({av_jpg}) | [webp]({av_webp})"
            )
        embed.set_image(url=f'{member.avatar_url}')
        if member == ctx.author:
            pass
        else:
            embed.set_footer(text=f'Requested by {ctx.author}')
        return await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=['whois'])
    @bot_checks.embed_check()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def userinfo(self, ctx, user:discord.User=None):
        """
        Display a member's user information!
        """
        if not user:
            user = ctx.author
        today = datetime.date.today()
        create_date = user.created_at.date()
        create_date_strf = create_date.strftime('%B %d, %Y')
        total_days = today-create_date

        embed=discord.Embed(color=0x5474b4, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{user} - {user.id}', icon_url=f'{user.avatar_url}')
        embed.set_thumbnail(url=f'{user.avatar_url}')
        embed.add_field(
            name='Basic Information', 
            value=f'**Username**: `{user}`\n**User ID**: `{user.id}`\n**Avatar Link**: [Click here]({user.avatar_url})', 
            inline=False
            )
        guild = self.client.get_guild(ctx.guild.id)
        if guild.get_member(user.id) is not None:
            join_date = guild.get_member(user.id).joined_at.date()
            join_date_strf = join_date.strftime('%B %d, %Y')
            daes = today-join_date
            embed.add_field(
                name='Other Information', 
                value=f'✅ **Is a member of this server**\n**Created At**: `{total_days.days} day(s) ago` \
                {create_date_strf}\n**Joined At**: `{daes.days} day(s) ago` {join_date_strf}'
                )
        else:
            embed.add_field(
                name='Other Information', 
                value=f'❌ **Not a member of this server**\n**Created At**: `{total_days.days} day(s) ago` \
                {create_date_strf}'
                )
        return await ctx.reply(embed=embed, mention_author=False)


    @commands.command()
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def roleinfo(self, ctx, role: discord.Role = None):
        """
        Display information about a role!
        """
        if not role:
            return await ctx.reply("You forgot to specify a role.")
        today = datetime.date.today()
        created_date = role.created_at.date()
        total_days = today - created_date
        list = role.members
        total_members = len(list)
        embed=discord.Embed(
            color=role.color, 
            title='Role Info', 
            description=f'Name: {role.name}\nColor: {role.color}\nMembers: {total_members}\nCreated `{total_days.days}` day(s) ago'
            )
        embed.set_footer(text=f'ID: {role.id}')
        return await ctx.reply(embed=embed, mention_author=False)


    @commands.command()
    @user_checks.server_manager()
    async def prefix(self, ctx, *, pref:str = None):
        """
        View server prefix or set prefix for the server (requires permissions of course).
        """
        if not pref:
            guild_prefix = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
            prefix = guild_prefix["prefix"]
            return await ctx.reply(f"The prefix of this server is `{prefix}`")
        else:
            await self.client.db.execute("UPDATE prefixes SET prefix = $1 WHERE guild_id = $2", pref, ctx.guild.id)
            return await ctx.reply(f"Prefix successfully updated to `{pref}`", mention_author=False)

    @prefix.error                                #Prefix error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            guild_prefix = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
            prefix = guild_prefix["prefix"]
            return await ctx.reply(f"The prefix of this server is `{prefix}`")





def setup(client):
    client.add_cog(Utility(client))