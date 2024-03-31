import os

import discord
from discord import app_commands
from discord.ext import commands

from utils.config import Config

if __name__ == '__main__':
    config = Config()
    intents = discord.Intents.all()
    prefix = config.get_unique_item("prefix")
    token = config.get_unique_item("token")
    guild = discord.Object(config.get_unique_item("guild"))
    bot = commands.Bot(command_prefix=prefix, intents=intents)


    @bot.event
    async def on_ready() -> None:
        """
        Prints bot start status and then syncs the commands.
        """
        print(f"The bot has started... ")
        for file in os.listdir("./cogs"):
            if file.endswith(".py") and "__init__" not in file:
                await bot.load_extension(f"cogs.{file[:-3]}")


    @bot.hybrid_command(name="list_extensions", with_app_command=True)
    @app_commands.guilds(guild)
    async def list_extensions(ctx: commands.Context) -> None:
        """
        Creates a command used by the bot to list all the available extensions.

        Args:
            ctx (discord.ext.commands.Context): The context with which the
                                                command has been invoked.
        """
        description = ""
        counter = 0
        for file in os.listdir("./cogs"):
            if file.endswith(".py") and "__init__" not in file:
                description = description + f"{counter}. {file[:-3]}\n"
                counter = counter + 1
        embed = discord.Embed(
            title="Available Extensions:",
            description=description,
            color=discord.Color.red()
        )
        await ctx.reply(embed=embed)


    @bot.hybrid_command(name="load_extension", with_app_command=True)
    @app_commands.guilds(guild)
    async def load_extension(ctx: commands.Context, extension="*") -> None:
        """
        Creates a command used to load extensions for the discord bot.

        Args:
            ctx (discord.ext.commands.Context): The context that the command
                                                was invoked with.
            extension (str): The extension specified by the user that should
                             be loaded. If none is specified then all
                             extensions are loaded.
        """
        try:
            if extension == "*":
                for filename in os.listdir("./cogs"):
                    if filename.endswith(".py") and "__init__" not in filename:
                        await bot.load_extension(f"cogs.{filename[:-3]}")
                        await ctx.reply("All extensions have been loaded.")
            else:
                await bot.load_extension(f"cogs.{extension}")
                await ctx.reply(f"The extension {extension} has been loaded.")
        except commands.ExtensionAlreadyLoaded:
            await ctx.reply(f"The extension {extension} is already loaded.")
        except commands.ExtensionNotFound:
            await ctx.reply(f"The extension {extension} could not be found.")
        except Exception:
            await ctx.reply(f"There was a fatal error loading {extension}, "
                            f"please check the bots logs.")


    @bot.hybrid_command(name="unload_extension", with_app_command=True)
    @app_commands.guilds(guild)
    async def unload_extension(ctx: commands.Context, extension="*") -> None:
        """
        Creates a command used to unload extensions used by the discord bot.

        Args:
            ctx (discord.ext.commands.Context): The context that the command
            was invoked
                                    with.
            extension (str): The extension that is to be unloaded. If none is
                             specified then all extensions are unloaded.
        """
        try:
            if extension == "*":
                for filename in os.listdir("./cogs"):
                    if filename.endswith(".py") and "__init__" not in filename:
                        await bot.unload_extension(f"cogs.{filename[:-3]}")
                        await ctx.reply("All extensions have been unloaded.")
            else:
                await bot.unload_extension(f"cogs.{extension}")
                await ctx.reply(f"The extension {extension} has been unloaded.")
        except commands.ExtensionNotLoaded:
            await ctx.reply(f"The extension {extension} is not loaded.")
        except commands.ExtensionNotFound:
            await ctx.reply(f"The extension {extension} could not be found.")
        except Exception:
            await ctx.reply(f"There was a fatal error loading {extension}, "
                            f"please check the bots logs.")


    @bot.hybrid_command(name="reload_extension", with_app_command=True)
    @app_commands.guilds(guild)
    async def reload_extension(ctx: commands.Context, extension="*") -> None:
        """
        Creates a command used by the discord bot to reload extensions.

        Args:
            ctx (discord.ext.commands.Context): The context with which the
                                                command has been invoked.
            extension (str): The extension that is to be reloaded. If none is
                             specified then all extensions are reloaded.
        """
        if extension == "*":
            await unload_extension(ctx)
            await load_extension(ctx)
        else:
            await unload_extension(ctx, extension=extension)
            await load_extension(ctx, extension=extension)


    @bot.hybrid_command(name="sync", with_app_command=True)
    @app_commands.guilds(guild)
    async def sync(ctx: commands.Context) -> None:
        """
        Creates a command used to sync the app_commands used by the bot.

        Args:
            ctx (discord.ext.commands.Context): The context with which the
                                                command was invoked.
        """
        synced = await bot.tree.sync(guild=guild)
        if synced:
            await ctx.channel.send("Slash commands have been synced.")
        else:
            await ctx.channel.send("Failed to sync the commands.")


    bot.run(token)
