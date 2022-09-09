import discord
from discord.ext import commands, tasks
from NASA_API.API import api
from NASA_API.YAML_PARSER import yaml_parser

class daily_report(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.api_image = api('conf/config.yaml', 'APOD_URL').json_data('url')
        self.api_explination = api('conf/config.yaml', 'APOD_URL').json_data('explanation')

    @commands.Cog.listener()
    async def on_ready(self):
        self.apod_daily.start()

        #Checks if the server has started

    @tasks.loop(hours=24, reconnect=True)
    async def apod_daily(self):
        self.channel = self.client.get_channel(yaml_parser('conf/config.yaml').parse_data('CHANNEL'))

        embed = discord.Embed(
            title="Astronomy Picture of the Day",
            url=self.api_image,
            description=self.api_explination,
            colour=discord.Colour.dark_blue()
        )

        #Creates the embed variable

        embed.set_image(url=self.api_image)
        embed.set_footer(text=self.api_image)

        #Sets the args used for the embed

        await self.channel.send(embed=embed)
        #Scheduals the apod to send every 24 hours from bot start

def setup(client):
    client.add_cog(daily_report(client))


