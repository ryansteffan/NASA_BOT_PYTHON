import os 
import asyncio
import discord
from discord.ext import commands
from NASA_API.YAML_PARSER import yaml_parser

#imports all of the packages that are used in the main file. 

if __name__ == "__main__":

    intents = discord.Intents.all()

    client = commands.Bot(command_prefix= '$', intents=intents)

    #Sets the prfix for the bot.

    @client.command()
    @commands.has_role("NASA_Bot")
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')

        #Loads an extention from the cogs folder

    @client.command()
    @commands.has_role("NASA_Bot")
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')

        #Unloads an extention from the cogs folder

    @client.command()
    @commands.has_role("NASA_Bot")
    async def reload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    
    async def load_extensions():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await client.load_extension(f"cogs.{filename[:-3]}")
    
    #Loads all of the cogs on bot startup

    conf_location = os.path.abspath('conf/config.yaml')

    #Locates the yaml config file

    TOKEN = yaml_parser(conf_location).parse_data('DISCORD_TOKEN')

    #Loads the token that is used to connect to the discord bot

    async def main_thread():
        async with client:
            await load_extensions()
            await client.start(TOKEN)

    asyncio.run(main_thread())

    #Starts the bot.

#NASA_API syntax:   api('conf/config.yaml', 'APOD_URL').json_data('url')

