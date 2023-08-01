import discord
from discord.ext import commands
from discord import app_commands

class cog1(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog?")

    @app_commands.command(name='cog1', description="Send hello!")
    async def cog1(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="hello")
    
async def setup(client:commands.Bot) -> None:
    await client.add_cog(cog1(client))