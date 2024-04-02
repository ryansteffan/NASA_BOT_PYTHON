import datetime

import discord
from discord import app_commands
from discord.ext import commands

from src.utils.config import Config


class Settings(commands.GroupCog, name="setting"):
    """
    Represents the settings commands for the discord bot.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """
        Creates an instance of the Settings class.

        Args:
            bot (discord.ext.commands.Bot): The bot that the cog is being
                                            added to.
        """
        self.bot = bot
        self.history_size: int = 4
        self.history: list[dict] = []

    def reset_history(self) -> None:
        """
        Checks if the history should be reset.
        """
        if len(self.history) > self.history_size:
            self.history = []

    @app_commands.command(
        name="list_all",
        description="Displays all the current settings for the bot."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def list_all(self, interaction: discord.Interaction) -> None:
        """
        Lists all the settings for the discord bot.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
        """
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
    @app_commands.checks.has_permissions(administrator=True)
    async def set(self,
                  interaction: discord.Interaction,
                  setting: str,
                  new_value: str) -> None:
        """
        Sets a setting in the discord bot configuration file.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
            setting (str): The setting that is being changed.
            new_value (str): The new value for the setting.
        """
        config = Config()
        setting = str(setting).strip()
        new_value = str(new_value).strip()
        try:
            previous_value = config.get_unique_item(setting)
            self.reset_history()
            self.history.append({setting: [previous_value, new_value]})
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
        except AttributeError:
            await interaction.response.send_message("The setting selected "
                                                    "does not exist.")

    @app_commands.command(
        name="unset",
        description="Sets a setting to the state of \"unset\"."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def unset(self,
                    interaction: discord.Interaction,
                    setting: str) -> None:
        """
        Sets a value in the discord bot configuration to a value of "unset".

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
            setting (str): The setting to "unset".
        """
        config = Config()
        setting = str(setting).strip()
        try:
            previous_value = config.get_unique_item(setting)
            self.reset_history()
            self.history.append({setting: [previous_value, "unset"]})
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
        except AttributeError:
            await interaction.response.send_message("The setting selected "
                                                    "does not exist.")

    @app_commands.command(
        name="view_history",
        description="Displays the history for the past 5 changes that have "
                    "been made to the settings."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def view_history(self, interaction: discord.Interaction) -> None:
        """
        List the history of changes to the bot settings.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
        """
        setting_index = 0
        embed = discord.Embed(
            title="Recent Changes:",
            color=discord.Color.red(),
            description="Changes can be reverted with: /settings restore #",
            timestamp=datetime.datetime.now()
        )
        for setting in self.history:
            if setting_index < 6:
                for key, value in setting.items():
                    embed.add_field(name=f"{setting_index}. {key}",
                                    value=f"Old Value: {value[0]} ----> New "
                                          f"Value: {value[1]}",
                                    inline=False)
                    setting_index += 1

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="restore",
        description="Allows for a previous setting to be restored. Can only "
                    "be done on the past 5 commands executed"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def restore(self,
                      interaction: discord.Interaction,
                      change: int) -> None:
        """
        Restores a past setting change to the previous state.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
            change (int): The number of the change that is to be reverted.
        """
        config = Config()
        try:
            change = self.history[change]
            for key, value in change.items():
                config.update_unique_item(key, value[0])

            self.history.remove(change)
            await interaction.response.send_message(f"Change #{change} "
                                                    f"has be reset.")
        except IndexError:
            await interaction.response.send_message(
                "The change selected does not exist.")


async def setup(bot: commands.Bot):
    """
    Adds the commands to a bot when the extension is loaded.

    Args:
        bot (commands.Bot): The bot to add the commands to.
    """
    await bot.add_cog(Settings(bot), guilds=bot.guilds)
