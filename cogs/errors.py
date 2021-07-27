from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client


#--------------------------------------------------------ERORRS
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Global error handlers.
        """
        if isinstance(error, commands.CommandNotFound): #Ignoring command not found error
            return


        elif isinstance(error, commands.CommandOnCooldown): 
            return await ctx.reply(f"You are on cooldown! You can use `{ctx.command.name}` command after {round(error.retry_after)} second(s).", delete_after=round(error.retry_after))


        elif isinstance(error, commands.BotMissingPermissions): #I did not copy this from stackoverflow.
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)
            return await ctx.reply(f"Looks like I am missing **{fmt}** permission(s).")


        elif hasattr(ctx.command, 'on_command_error'):
            return


        elif isinstance(error, commands.BadArgument):
            return await ctx.reply("Bad arguments passed.")


        elif isinstance(error, commands.CheckFailure):
            return


def setup(client):
    client.add_cog(Errors(client))