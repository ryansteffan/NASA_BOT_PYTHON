import discord
from discord.ext import commands

class ready_check(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has started...')

        #Checks if the bot has started

def setup(client):
    client.add_cog(ready_check(client))