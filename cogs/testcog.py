# import discord
# from discord.ext import commands
# from discord import app_commands

# class testcog(commands.Cog):
#     def __init__(self, client: commands.Bot):
#         self.client = client

#     @app_commands.command(name='testcog', description='test')
#     async def testcog(self, interaction:discord.Interaction):
#         await interaction.response.send_message('something')

# async def setup(client:commands.Bot) -> None:
#     await client.add_cog(testcog(client))


import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio
