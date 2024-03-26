import datetime

import discord
from discord import app_commands
from discord.ext import commands

from utils.config import Config


class Settings(commands.GroupCog, name="setting"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="list_all",
        description="Displays all the current settings for the bot."
    )
    async def view(self, interaction: discord.Interaction):
        # TODO: Make this multi page
        config = Config()
        config_items = config.config_data.items()
        bot_name = self.bot.user
        tab = " -----> "
        protected = [
            "token",
            "bot_token",
            "bot_key",
            "api",
            "api_token",
            "api_key",
            "key",
            "password",
            "passkey",
            "pass"
        ]
        embed = discord.Embed(
            title=f"{bot_name} Settings:",
            color=discord.Color.red()
        )

        for keys, values in config_items:
            keys = str(keys)
            values = str(values)
            if keys.strip() in protected:
                embed.add_field(name=keys + tab + "*\*\*\*\*", value="",
                                inline=False)
            else:
                embed.add_field(name=keys + tab + values, value="",
                                inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="set",
        description="Set the state of a setting."
    )
    async def set(self,
                  interaction: discord.Interaction,
                  setting: str,
                  new_value: str) -> None:
        config = Config()
        setting = str(setting).strip()
        new_value = str(new_value).strip()
        previous_value = config.get_unique_item(setting)
        config.update_unique_item(setting, new_value)
        embed = discord.Embed(
            title="Settings changed:",
            color=discord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        embed.add_field(name="Old Settings",
                        value=f"{setting}: {previous_value}",
                        inline=False)
        embed.add_field(name="New Setting",
                        value=f"{setting}: {new_value}",
                        inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="unset",
        description="Sets a setting to the state of \"unset\"."
    )
    async def unset(self,
                    interaction: discord.Interaction,
                    setting: str):
        config = Config()
        setting = str(setting).strip()
        previous_value = config.get_unique_item(setting)
        config.update_unique_item(setting, "unset")
        embed = discord.Embed(
            title="Settings changed:",
            color=discord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        embed.add_field(name="Old Settings",
                        value=f"{setting}: {previous_value}",
                        inline=False)
        embed.add_field(name="New Setting",
                        value=f"{setting}: unset",
                        inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Settings(bot), guilds=bot.guilds)
