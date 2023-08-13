import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class shutdown(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("shutdown is synced")

    @app_commands.command(name='shutdown', description='Shutting down the bot')
    async def shutdown(self, interraction: discord.Interaction):
        await interraction.response.send_message(content='*Shutting down the bot*', delete_after=5)
        await self.client.close()


async def setup(client:commands.Bot) -> None:
    await client.add_cog(shutdown(client))