import datetime
import tempfile

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks

from src.nasa_api import Apod, nasa_api_errors
from src.utils import Config
from src.utils.nasa_bot_logger import nasa_bot_logger


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
        try:
            config = Config()
            self.channel = config.get_unique_item("apod_channel")
            self.endpoint = config.get_unique_item("apod_url")
        except Exception as e:
            nasa_bot_logger.exception(e)
        self.post_daily_image.start()
        self.bot = bot

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
            try:
                await interaction.response.send_message(apod.url)
            except Exception as e:
                nasa_bot_logger.exception(e)
        else:
            image_description = apod.explanation
            image_url = apod.url

            # Download the image to a temporary file
            with tempfile.TemporaryFile(prefix="apod_image") as temp_file:
                apod.download_image(temp_file.name)
            image_file = discord.File(temp_file.name)

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
            embed.set_image(url=f"attachment://{temp_file.name}")
            embed.set_footer(text=copyright)
            try:
                await interaction.response.send_message(embed=embed,
                                                        file=image_file)
            except Exception as e:
                nasa_bot_logger.exception(e)

    @tasks.loop(time=time)
    async def post_daily_image(self) -> None:
        """
        Post the APOD daily to discord.
        """
        channel = self.bot.get_channel(int(self.channel))
        apod = Apod(self.endpoint)
        if apod.is_video():
            try:
                await channel.send(apod.url)
            except Exception as e:
                nasa_bot_logger.exception(e)
        else:
            image_description = apod.explanation
            image_url = apod.url

            # Download the image to a temporary file
            with tempfile.TemporaryFile() as temp_file:
                with open(temp_file.name, "rb") as f:
                    image_file = discord.File(temp_file.name)
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
                    embed.set_image(url=f"attachment://{temp_file.name}")
                    embed.set_footer(text=copyright)
                    try:
                        await channel.send(embed=embed, file=image_file)
                    except Exception as e:
                        nasa_bot_logger.exception(e)

async def setup(bot: commands.Bot):
    """
    Adds the commands to a bot when the extension is loaded.

    Args:
        bot (commands.Bot): The bot to add the commands to.
    """
    try:
        config = Config()
        hour = int(config.get_unique_item("hour"))
        minute = int(config.get_unique_item("minute"))
        if hour < 0 or hour > 23:
            raise ValueError("The hour setting has been set to an invalid "
                             "value.")
        if minute < 0 or minute > 59:
            raise ValueError("The minute setting has been set to an invalid "
                             "value.")
    except Exception as e:
        nasa_bot_logger.exception(e)
    try:
        await bot.add_cog(APOD(bot), guilds=bot.guilds)
    except Exception as e:
        nasa_bot_logger.exception(e)
