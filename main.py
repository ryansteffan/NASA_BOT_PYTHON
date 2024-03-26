import os

import discord
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
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and "__init__" not in filename:
                await bot.load_extension(f"cogs.{filename[:-3]}")


    @bot.command()
    async def sync(ctx: commands.Context) -> None:
        """
        Manually syncs the app commands for the discord bot.

        Args:
            ctx (commands.Context): The context for the command.
        """
        synced = await bot.tree.sync(guild=guild)
        if synced:
            await ctx.channel.send("Slash commands have been synced.")
        else:
            await ctx.channel.send("Failed to sync the commands.")


    bot.run(token)
