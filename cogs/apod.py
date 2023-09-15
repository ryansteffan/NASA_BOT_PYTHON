import discord 
from discord.ext import commands
from NASA_API.API import api

class apod(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.api_image = api('conf/config.yaml', 'APOD_URL').json_data('url')
        self.api_explination = api('conf/config.yaml', 'APOD_URL').json_data('explanation')

        #Gets the picture of the day via NASA_API

    @commands.Command
    async def apod(self, ctx):

        embed = discord.Embed(
            title="Astronomy Picture of the Day",
            url=self.api_image,
            description=self.api_explination,
            colour=discord.Colour.dark_blue()
        )

        #Creates the embed variable

        embed.set_image(url=self.api_image)
        embed.set_footer(text=self.api_image)

        #Sets the args used in the embed

        await ctx.send(embed=embed)

        #Sends the call made from the api when apod is run in the server

async def setup(client):
    await client.add_cog(apod(client))
