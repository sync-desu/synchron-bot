from discord.ext import commands

from discord.ext.commands.core import guild_only
from utils.checks import user_checks


class Prefixes(commands.Cog):
    def __init__(self, client):
        self.client = client


#--------------------------------------------------LISTENERS        
    @commands.Cog.listener()
    async def on_ready(self):
        """
        Creates a table if that table does not exist in the database.
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


#------------------------------------------------------PREFIX COMMAND
    @commands.command()
    @user_checks.server_manager()
    async def prefix(self, ctx, *, pref:str = None):
        """
        View server prefix or set prefix for the server (requires manage_server or admin permissions of course).
        """
        if not pref:
            guild_prefix = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
            prefix = guild_prefix["prefix"]
            return await ctx.reply(f"The prefix of this server is `{prefix}`")
        else:
            await self.client.db.execute("UPDATE prefixes SET prefix = $1 WHERE guild_id = $2", pref, ctx.guild.id)
            return await ctx.reply(f"Prefix successfully updated to `{pref}`", mention_author=False)

    @prefix.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            guild_prefix = await self.client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", ctx.guild.id)
            prefix = guild_prefix["prefix"]
            return await ctx.reply(f"The prefix of this server is `{prefix}`")


def setup(client):
    client.add_cog(Prefixes(client))