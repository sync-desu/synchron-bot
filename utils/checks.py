from discord.ext import commands

class bot_checks:
    """
    
    Custom checks in this class will be used to check if client.user has required permissions.

    """
    def embed_check():
        """
        Checks if the bot has embed links permission.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.me.guild_permissions.embed_links
        return commands.check(predicate)


    def attachment_check():
        """
        Checks if the bot has attach files permission.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.me.guild_permissions.attach_files
        return commands.check(predicate)


    def attachment_embed_check():
        """
        Checks if the bot has both embed links and attach files permission.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.me.guild_permissions.embed_links \
                and ctx.me.guild_permissions.attach_files
        return commands.check(predicate)


    def manage_msg_check():
        """
        Checks if the bot has manage messages permission.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.me.guild_permissions.manage_messages
        return commands.check(predicate)


    async def message_delete(ctx):
        """
        An asynchronous function that deletes command invoke message.
        """
        try:
            await ctx.message.delete()
        except:
            return


class user_checks:
    """
    Custom checks in this class will be used to check if discord.user has required permissions.
    """
    def my_owner():
        """
        Checks if the owner is the one running the command.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.author.id == 688917796943560734
        return commands.check(predicate)


    def server_manager():
        """
        Checks if invoker has manage_guild permissions.
        """
        async def predicate(ctx):
            return ctx.guild is not None and ctx.me.guild_permissions.read_messages \
                and ctx.author.guild_permissions.manage_guild \
                or ctx.author.guild_permissions.administrator
        return commands.check(predicate)