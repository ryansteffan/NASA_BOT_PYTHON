import discord 
from discord.ext import commands 

class connection(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Command
    async def connection(self, ctx):
        await ctx.send(f"{round(self.client.latency * 1000)} ms")

        #Tests the server round trip time 

async def setup(client):
    await client.add_cog(connection(client))