import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks

from src.nasa_api import Apod, nasa_api_errors
from src.utils import Config


class APOD(commands.GroupCog, name="apod"):
    # Creates the time object for the daily post.
    time = datetime.time(
        hour=int(Config().get_unique_item("hour")),
        minute=int(Config().get_unique_item("minute")),
        tzinfo=datetime.timezone.utc
    )

    def __init__(self, bot: commands.Bot):
        """
        Creates an instance of the APOD class.

        Args:
            bot (discord.ext.commands.Bot): The bot that the cog is being
            added to.
        """
        config = Config()
        self.bot = bot
        self.channel = config.get_unique_item("apod_channel")
        self.endpoint = config.get_unique_item("apod_url")
        self.post_daily_image.start()

    @app_commands.command(name="daily_image",
                          description="Posts the Astronomy picture of the day.")
    async def daily_image(self, interaction: discord.Interaction) -> None:
        """
        Posts the daily APOD image to discord.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
        """
        apod = Apod(self.endpoint)
        if apod.is_video():
            await interaction.response.send_message(apod.url)
        else:
            image_description = apod.explanation
            image_url = apod.url
            try:
                copyright = apod.copyright
            except nasa_api_errors.NasaApiDataNotFoundError:
                copyright = "Copyright: NASA"
            color = discord.Color.dark_blue()
            embed = discord.Embed(
                title="Astronomy Picture of the Day",
                url=image_url,
                color=color,
                description=image_description
            )
            embed.set_image(url=image_url)
            embed.set_footer(text=copyright)
            await interaction.response.send_message(embed=embed)

    @tasks.loop(time=time)
    async def post_daily_image(self) -> None:
        """
        Post the APOD daily to discord.
        """
        channel = self.bot.get_channel(int(self.channel))
        apod = Apod(self.endpoint)
        if apod.is_video():
            await channel.send(apod.url)
        else:
            image_description = apod.explanation
            image_url = apod.url
            try:
                copyright = apod.copyright
            except nasa_api_errors.NasaApiDataNotFoundError:
                copyright = "Copyright: NASA"
            color = discord.Color.dark_blue()
            embed = discord.Embed(
                title="Astronomy Picture of the Day",
                url=image_url,
                color=color,
                description=image_description
            )
            embed.set_image(url=image_url)
            embed.set_footer(text=copyright)
            await channel.send(embed=embed)


async def setup(bot: commands.Bot):
    """
    Adds the commands to a bot when the extension is loaded.

    Args:
        bot (commands.Bot): The bot to add the commands to.
    """
    config = Config()
    hour = int(config.get_unique_item("hour"))
    minute = int(config.get_unique_item("minute"))
    if hour < 0 or hour > 23:
        raise ValueError("The hour setting has been set to an invalid value.")
    if minute < 0 or minute > 59:
        raise ValueError("The minute setting has been set to an invalid value.")
    await bot.add_cog(APOD(bot), guilds=bot.guilds)
