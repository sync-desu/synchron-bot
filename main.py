import discord
from discord.ext import commands
import os
import asyncpg

from cogs.dev import *
from utils.checks import *


async def get_prefix(client, message):
    """
    Returns guild default/custom prefix stored in database.
    """
    server = await client.db.fetchrow("SELECT prefix FROM prefixes WHERE guild_id = $1", message.guild.id)
    prefix = server["prefix"]
    return commands.when_mentioned_or(prefix)(client, message)


client = commands.Bot(command_prefix = get_prefix
                    , case_insensitive=True
                    , owner_id = 688917796943560734
                    , intents=discord.Intents().all())


async def create_db_pool():
    client.db = await asyncpg.create_pool(os.environ["DATABASE_URL"]) # ENV Variable in heroku


@client.event
async def on_ready():
    """
    Prints message when bot is online and changes default status to custom status.
    """
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="sekciest discord bot in 2021", type=5))
    return print('SyNchr0n is now awake.')


@client.event
async def on_message(message):
    """
    Ignores commands invoked by bot users and blacklisted users.
    Additionally ignores commands invoked in private messages.
    """
    await client.wait_until_ready()
    if message.author.bot:
        return
    if message.guild is None:
        return
    
    user_status = await client.db.fetchrow("SELECT status FROM users WHERE user_id = $1", message.author.id)
    if not user_status:
        pass
    elif user_status["status"] == "blacklist":
        return
    else:
        pass

    await client.process_commands(message)


#--------------------------------------------------COGS
cogs = ['dev', 'errors', 'fun', 'imgen',
         'misc', 'utility', 'help']
for cog in cogs:
    try:
        client.load_extension(f"cogs.{cog}")
    except Exception as e:
        print(f'Could not load cog {cog}. Reason: {str(e)}')


@client.command() 
@user_checks.my_owner()
async def reload(ctx, cogname = None):
    """
    Re-load a cog after making changes, or just to refresh the commands.
    """
    if not cogname:
        return
    try:
        client.reload_extension(f"cogs.{cogname}") 
    except Exception as e:
        print(f'Could not reload cog {cogname}. Reason: {str(e)}')
        await ctx.reply(f'Could not reload cog `{cogname}`.', mention_author=False, delete_after=1)
    else:
        print(f'Reloaded cog {cogname} successfully.')
        await ctx.reply(f'Reloaded cog `{cogname}` successfully.', mention_author=False, delete_after=1)
    return await bot_checks.message_delete(ctx)


@client.command() 
@user_checks.my_owner()
async def load(ctx, cogname = None):
    """
    Load a cog.
    """
    if not cogname:
        return
    try:
        client.load_extension(f"cogs.{cogname}")
    except Exception as e:
        print(f'Could not load cog {cogname}. Reason: {str(e)}')
        await ctx.reply(f'Could not load cog `{cogname}`.', mention_author=False, delete_after=1)
    else:
        print(f'Loaded cog {cogname} successfully.')
        await ctx.reply(f'Loaded cog `{cogname}` successfully.', mention_author=False, delete_after=1)
    return await bot_checks.message_delete(ctx)


@client.command() 
@user_checks.my_owner()
async def unload(ctx, cogname = None):
    """    
    Unload a cog.
    """
    if not cogname:
        return
    try:
        client.unload_extension(cogname) 
    except Exception as e:
        print(f'Could not unload cog {cogname}. Reason: {str(e)}')
        await ctx.reply(f'Could not unload cog `{cogname}``.', mention_author=False, delete_after=1)
    else:
        print(f'Unloaded cog {cogname} successfully.')
        await ctx.reply(f'Unloaded cog `{cogname}` successfully.', mention_author=False, delete_after=1)
    return await bot_checks.message_delete(ctx)





client.loop.run_until_complete(create_db_pool())
token = os.environ["token"] # ENV Variable in heroku
client.run(token)