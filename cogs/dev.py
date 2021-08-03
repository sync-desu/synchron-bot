import discord
from discord.ext import commands
from copy import copy
from utils.checks import *


class Dev(commands.Cog):
    """
    Dev commands!
    """
    def __init__(self, client):
        self.client = client
        self.emoji = "🖊️"


#--------------------------------------------------LISTENERS        
    @commands.Cog.listener()
    async def on_ready(self):
        """
        Creates a table if that table does not exist in the database.
        """
        await self.client.db.execute("CREATE TABLE IF NOT EXISTS users (user_id BIGINT NOT NULL PRIMARY KEY, status CHARACTER VARYING NOT NULL)")
        await self.client.db.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS user_id BIGINT NOT NULL PRIMARY KEY")
        await self.client.db.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS status CHARACTER VARYING NOT NULL")


#--------------------------------------------------WHITELIST
    @commands.command(aliases=["wl"])
    @user_checks.my_owner()
    async def whitelist(self, ctx, user: discord.User):
        """
        Adds the specified user into the users table.
        """
        if user.bot:
            await ctx.reply("You can not perform this action on Bots.", delete_after=1)

        user_status = await self.client.db.fetchrow("SELECT status FROM users WHERE user_id = $1", user.id)
        if not user_status:
            wl = "whitelist"
            await self.client.db.execute("INSERT INTO users (user_id, status) VALUES($1, $2)", user.id, wl)
            await ctx.reply(f"Successfully whitelisted {user}", delete_after=1)
        elif user_status["status"] == "blacklist":
            await ctx.reply("You can not whitelist a blacklisted user.", delete_after=1)
        elif user_status["status"] == "whitelist":
            await ctx.reply("That user is already whitelited.", delete_after=1)
        return await bot_checks.message_delete(ctx)


    @commands.command(aliases=["unwl"])
    @user_checks.my_owner()
    async def unwhitelist(self, ctx, user: discord.User):
        """
        
        Removes the specified user from the users table if they exist in the table.

        """
        if user.bot:
            await ctx.reply("You can not perform this action on Bots.", delete_after=1)
        
        user_status = await self.client.db.fetchrow("SELECT status FROM users WHERE user_id = $1", user.id)
        if not user_status:
            await ctx.reply("That user is not whitelisted.", delete_after=1)
        elif user_status["status"] == "whitelist":
            await self.client.db.execute("DELETE FROM users WHERE user_id = $1", user.id)
            await ctx.reply(f"Successfully un-whitelisted {user}.", delete_after=1)
        else:
            return
        return await bot_checks.message_delete(ctx)

    @whitelist.error                             #Whitelist command error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You forgot to mention the user you want to whitelist.", delete_after=1)
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Bad Arguments Passed.", delete_after=1)
        return await bot_checks.message_delete(ctx)

    @unwhitelist.error                           #Un-whitelist command error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You forgot to mention the user you want to un-whitelist.", delete_after=1)
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Bad Arguments Passed.", delete_after=1)
        return await bot_checks.message_delete(ctx)


#--------------------------------------------------BLACKLIST
    @commands.command(aliases=["bl"])
    @user_checks.my_owner()
    async def blacklist(self, ctx, user: discord.User):
        """

        Adds the specified user into the blacklisted database.

        """
        if user.bot:
            await ctx.reply("You can not perform this action on Bots.", delete_after=1)

        user_status = await self.client.db.fetchrow("SELECT status FROM users WHERE user_id = $1", user.id)
        if not user_status:
            bl = "blacklist"
            await self.client.db.execute("INSERT INTO users (user_id, status) VALUES($1, $2)", user.id, bl)
            await ctx.reply(f"Successfully blacklisted {user}", delete_after=1)
        elif user_status["status"] == "blacklist":
            await ctx.reply("That user is already blacklisted.", delete_after=1)
        elif user_status["status"] == "whitelist":
            await ctx.reply("You can not blacklist a whitelisted user.", delete_after=1)
        return await bot_checks.message_delete(ctx)


    @commands.command(aliases=["unbl"])
    @user_checks.my_owner()
    async def unblacklist(self, ctx, user: discord.User):
        """

        Removes the specified user from the blacklist database if they exist in the database.

        """
        if user.bot:
            await ctx.reply("You can not perform this action on Bots.", delete_after=1)
            
        user_status = await self.client.db.fetchrow("SELECT status FROM users WHERE user_id = $1", user.id)
        if not user_status:
            await ctx.reply("That user is not blacklisted.", delete_after=1)
        elif user_status["status"] == "blacklist":
            await self.client.db.execute("DELETE FROM users WHERE user_id = $1", user.id)
            await ctx.reply(f"Successfully un-blacklisted {user}.", delete_after=1)
        else:
            return
        return await bot_checks.message_delete(ctx)


    @blacklist.error                             #Blacklist error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You forgot to mention the user you want to blacklist.", delete_after=1)
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Bad Arguments Passed.", delete_after=1)
        return await bot_checks.message_delete(ctx)

    @unblacklist.error                           #Unblacklist error handler
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("You forgot to mention the user you want to un-blacklist.", delete_after=1)
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Bad Arguments Passed.", delete_after=1)
        return await bot_checks.message_delete(ctx)


#--------------------------------------------------------MOCK Command
    @commands.command()
    @user_checks.my_owner()
    async def mock(self, ctx, user: discord.Member, *, command):
        """

        Instead of asking your friend "Hey! Can you run this command for me so I can test if it works?", make them do it forcefully.

        """
        msg = copy(ctx.message)
        msg.author = user
        msg.content = ctx.prefix + command
        ctx.bot.dispatch("message", msg)


def setup(client):
    client.add_cog(Dev(client))