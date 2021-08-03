from discord.ext import commands


class Errors(commands.Cog):
    """
    Global error handlers.
    """
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Error listener.
        """
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.CheckFailure):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.reply(f"You are on cooldown! You can use `{ctx.command.name}` command after \
                {round(error.retry_after)} second(s).", delete_after=round(error.retry_after))

        elif isinstance(error, commands.BotMissingPermissions):
            missing = [
                perm.replace('_', ' ').replace('guild', 'server').title() 
                for perm in error.missing_perms
                ]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)
            return await ctx.send(f"Looks like I am missing **{fmt}** permission(s).")

        elif isinstance(error, commands.BadArgument):
            if isinstance(error, commands.UserNotFound):
                return await ctx.reply("I was unable to find that user.")
            elif isinstance(error, commands.MemberNotFound):
                return await ctx.reply("I was unable to find that member.")
            elif isinstance(error, commands.RoleNotFound):
                return await ctx.reply("I was unable to find that role.")
            elif isinstance(error, commands.BadUnionArgument):
                return await ctx.reply("Bad arguments passed.")
            else:
                return await ctx.reply("Bad arguments passed.")

        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.reply(f"Missing required argument(s): `{error.param.name}`")





def setup(client):
    client.add_cog(Errors(client))