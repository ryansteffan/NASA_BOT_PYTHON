import datetime
import os.path
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
        self.temp_dir = tempfile.TemporaryDirectory(prefix="apod-images-cache-")
        self.temp_file_name = self.temp_dir.name
        self.apod_image_file = (f"{self.temp_file_name}/"
                                f"apod-{datetime.date.today()}.jpg")

    @app_commands.command(name="daily_image",
                          description="Posts the Astronomy picture of the day.")
    async def daily_image(self, interaction: discord.Interaction) -> None:
        """
        Posts the daily APOD image to discord.

        Args:
            interaction (discord.Interaction): Represents the interaction
                                               with discord.
        """

        await interaction.response.defer()
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
            if not os.path.exists(self.apod_image_file):
                apod.download_image(self.apod_image_file)

            filename = os.path.basename(self.apod_image_file)
            image_file = discord.File(self.apod_image_file, filename=filename)
            try:
                apod_copyright = apod.copyright
            except nasa_api_errors.NasaApiDataNotFoundError:
                apod_copyright = "Copyright: NASA"
            color = discord.Color.dark_blue()
            embed = discord.Embed(
                title="Astronomy Picture of the Day",
                url=image_url,
                color=color,
                description=image_description
            )
            embed.set_image(url=f"attachment://{filename}")
            embed.set_footer(text=apod_copyright)
            try:
                await interaction.followup.send(embed=embed, file=image_file)
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
            if not os.path.exists(self.apod_image_file):
                apod.download_image(self.apod_image_file)

            filename = os.path.basename(self.apod_image_file)
            image_file = discord.File(self.apod_image_file, filename=filename)
            try:
                apod_copyright = apod.copyright
            except nasa_api_errors.NasaApiDataNotFoundError:
                apod_copyright = "Copyright: NASA"
            color = discord.Color.dark_blue()
            embed = discord.Embed(
                title="Astronomy Picture of the Day",
                url=image_url,
                color=color,
                description=image_description
            )
            embed.set_image(url=f"attachment://{filename}")
            embed.set_footer(text=apod_copyright)
            try:
                await channel.send(embed=embed, file=image_file)

                # Wipe the cache each day to prevent excessive disk usage.
                self.clean_up_cache()
            except Exception as e:
                nasa_bot_logger.exception(e)

    def clean_up_cache(self) -> None:
        """
        Removes all images that are currently in the apod image cache.

        Returns: None

        Raises:
            FileNotFoundError: If the image file does not exist in the cache.

        Notes:
            This method is different from a call to the temporary directory's
            cleanup method as it only removes the images that are currently
            in the cache, rather than removing the directory itself.
        """
        try:
            for _ in os.listdir(self.temp_dir.name):
                os.remove(self.apod_image_file)
        except FileNotFoundError as exception:
            nasa_bot_logger.exception(f"Error cleaning up cache: {exception}")


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

