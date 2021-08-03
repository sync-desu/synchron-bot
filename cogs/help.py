import discord
from discord.ext import commands


class MyHelpCommand(commands.HelpCommand):
    """
    Help command by subclassing commands.HelpCommand.
    """
    def get_command_signature(self, command):
        """
        Overwrites existing get_command_signature function.
        """
        return f"{self.clean_prefix}{command.qualified_name} {command.signature}"


    async def send_bot_help(self, mapping):
        """
        Bot help.
        """
        embed = discord.Embed(color=0x5474b4, description=f"Type `{self.clean_prefix}help <command_or_category>` for more information on a command or category.")
        embed.set_author(name="SyNchr0n Help", icon_url=self.context.bot.user.avatar_url)
        embed.set_footer(text="SyNchron by sync#9074")
        for cog, commands in mapping.items():
            if cog is not None:
                filtered = await self.filter_commands(commands)
                if filtered:
                    cog_name = getattr(cog, "qualified_name")
                    cog_emoji = getattr(cog, "emoji", "🔴")
                    embed.add_field(name=f"{cog_emoji} | {cog_name}", value=f"`{self.clean_prefix}help {cog_name}`\n[{cog_name} commands!](https://discord.com/terms)")
        channel = self.get_destination()
        await channel.send(embed=embed)


    async def send_cog_help(self, cog):
        """
        Cog help.
        """
        commands = [c for c in cog.walk_commands()]
        filtered = await self.filter_commands(commands)
        command_names = [f"`{self.clean_prefix}{c.qualified_name}`" for c in filtered]
        if command_names:
            embed = discord.Embed(color=0x5474b4, description=f"Type `{self.clean_prefix}help <command>` for more information on a command.")
            embed.set_author(name=f"{cog.qualified_name} Help", icon_url=self.context.bot.user.avatar_url)
            embed.set_footer(text="SyNchron by sync#9074")
            embed.add_field(name="Description", value=cog.description, inline=False)
            embed.add_field(name="Commands", value=", ".join(command_names), inline=False)
            channel = self.get_destination()
            await channel.send(embed=embed)


    async def send_command_help(self, command):
        """
        Command help.
        """
        is_user_allowed = all([
                            await discord.utils.maybe_coroutine(check, self.context)
                            for check in command.checks
                            ])
        if is_user_allowed:
            embed = discord.Embed(color=0x5474b4, description=f"```fix\nUsage: {self.get_command_signature(command)}```")
            embed.set_author(name=f"{command.qualified_name} Help", icon_url=self.context.bot.user.avatar_url)
            embed.set_footer(text="SyNchron by sync#9074")
            embed.add_field(name="Description", value=command.help)
            alias = command.aliases
            if alias:
                embed.add_field(name="Aliases", value=", ".join(alias))
        channel = self.get_destination()
        await channel.send(embed=embed)



class Help(commands.Cog):
    """
    Overwrite default help command and run file as a cog.
    """
    def __init__(self, client):
        self.client = client
        help_cmd = MyHelpCommand()
        client.help_command = help_cmd





def setup(client):
    client.add_cog(Help(client))