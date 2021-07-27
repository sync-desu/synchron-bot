import discord
from discord.ext import commands
import datetime
from utils.checks import bot_checks


class Utility(commands.Cog):
    def __init__(self, client):        
        self.client = client


#------------------------------------------------------AVATAR Command
    @commands.command(aliases=['av'])
    @bot_checks.attachment_embed_check()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def avatar(self, ctx, member:discord.Member=None):
        """
        Display a member's avatar.
        """
        if not member:
            member = ctx.author
        av_jpg = str(member.avatar_url_as(static_format="jpg", size=1024))
        av_webp = str(member.avatar_url_as(static_format="webp", size=1024))
        av_png = str(member.avatar_url_as(static_format="png", size=1024))
        embed=discord.Embed(color=0x5474b4, title=f'Avatar for {member}', description=f"**Other format**:\n[png]({av_png}) | [jpg]({av_jpg}) | [webp]({av_webp})")
        embed.set_image(url=f'{member.avatar_url}')
        if member == ctx.author:
            pass
        else:
            embed.set_footer(text=f'Requested by {ctx.author}')
        return await ctx.reply(embed=embed, mention_author=False)

    @avatar.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            self.avatar.reset_cooldown(ctx)
            return await ctx.reply('I was unable to find that member.')


#------------------------------------------------------USERINFO Command
    @commands.command(aliases=['ui', 'whois', 'wi'])
    @bot_checks.embed_check()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def userinfo(self, ctx, user:discord.User=None):
        """
        Display information about a user's discord account.
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
        embed.add_field(name='Basic Information', value=f'**Username**: `{user}`\n**User ID**: `{user.id}`\n**Avatar Link**: [Click here]({user.avatar_url})', inline=False)
        guild = self.client.get_guild(ctx.guild.id)
        
        if guild.get_member(user.id) is not None:
            join_date = guild.get_member(user.id).joined_at.date()
            join_date_strf = join_date.strftime('%B %d, %Y')
            daes = today-join_date
            embed.add_field(name='Other Information', value=f'✅ **Is a member of this server**\n**Created At**: `{total_days.days} day(s) ago` {create_date_strf}\n**Joined At**: `{daes.days} day(s) ago` {join_date_strf}')
        else:
            embed.add_field(name='Other Information', value=f'❌ **Not a member of this server**\n**Created At**: `{total_days.days} day(s) ago` {create_date_strf}')
        return await ctx.reply(embed=embed, mention_author=False)

    @userinfo.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            self.userinfo.reset_cooldown(ctx)
            return await ctx.reply('I was unable to find that user.')


#------------------------------------------------------ROLEINFO Command
    @commands.command(aliases=['ri'])
    @bot_checks.embed_check()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def roleinfo(self, ctx, role:discord.Role):
        """
        Display info of a discord role.
        """
        today = datetime.date.today()
        created_date = role.created_at.date()
        total_days = today - created_date

        list = role.members
        total_members = len(list)
        embed=discord.Embed(color=role.color, title='Role Info', description=f'Name: {role.name}\nColor: {role.color}\nMembers: {total_members}\nCreated `{total_days.days}` day(s) ago')
        embed.set_footer(text=f'ID: {role.id}')
        return await ctx.reply(embed=embed, mention_author=False)

    @roleinfo.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            self.roleinfo.reset_cooldown(ctx)
            return await ctx.reply('I was unable to find that role.')
        
        elif isinstance(error, commands.MissingRequiredArgument):
            self.roleinfo.reset_cooldown(ctx)
            return await ctx.reply("You need to specify a role..")


def setup(client):
    client.add_cog(Utility(client))