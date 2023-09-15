import discord
import datetime
from discord.ext import commands, tasks
from NASA_API.API import api
from NASA_API.YAML_PARSER import yaml_parser


class daily_report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.apod_daily.start()

        #Checks if the server has started

    hour = yaml_parser('conf/config.yaml').parse_data('TIME', 'HOUR')
    minute = yaml_parser('conf/config.yaml').parse_data('TIME', 'MINUTE')
    time = datetime.time(hour=hour, minute=minute, tzinfo=datetime.timezone.utc)
    #Sets the time for the bot to post the APOD. Time Zones to be added later

    @tasks.loop(time=time)
    async def apod_daily(self):
        self.channel = self.client.get_channel(yaml_parser('conf/config.yaml').parse_data('CHANNEL'))
        self.api_image = api('conf/config.yaml', 'APOD_URL').json_data('url')
        self.api_explination = api('conf/config.yaml', 'APOD_URL').json_data('explanation')

        if "youtube" in self.api_image:
            await self.channel.send(self.api_image)
        else:
            self.embed = discord.Embed(
                title="Astronomy Picture of the Day",
                url=self.api_image,
                description=self.api_explination,
                colour=discord.Colour.dark_blue()
            )
            #Creates the embed variable
            
            self.embed.set_image(url=self.api_image)
            self.embed.set_footer(text=self.api_image)
            #Sets the args used for the embed

            await self.channel.send(embed=self.embed)
            #Scheduals the apod to send every 24 hours from bot start

async def setup(client):
    await client.add_cog(daily_report(client))


