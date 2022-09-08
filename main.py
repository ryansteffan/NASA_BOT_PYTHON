import os 
import discord
from discord.ext import commands
from NASA_API.YAML_PARSER import yaml_parser

#imports all of the packages that are used in the main file. 

if __name__ == "__main__":

    client = commands.Bot(command_prefix= '$')

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

        #Reloads an extention from the cogs folder

    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

    #Loads all of the cogs on bot startup

    conf_location = os.path.abspath('conf\config.yaml')

    #Locates the yaml config file

    TOKEN = yaml_parser(conf_location).parse_data('DISCORD_TOKEN')

    #Loads the token that is used to connect to the discord bot

    client.run(TOKEN)

    #Starts the bot.

#NASA_API syntax:    api('conf\config.yaml', 'APOD_URL').json_data('url')

