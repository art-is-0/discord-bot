import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class coinflip(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("coinflip is synced")

    @app_commands.command(name='coinflip', description='Guess which side the coin will fall on.')
    async def coinflip(self, interaction: discord.Interaction):
        async def heads_or_tails(interaction, choice):
            computer_choice = random.choice(['heads', 'tails'])
            if computer_choice == choice:
                await interaction.response.send_message(content=f' You guessed correctly, you guessed **{choice}** while it was **{computer_choice}**, congratualtions!!!', delete_after=15)
            else:
                await interaction.response.send_message(content=f' You lost, you guessed **{choice}** while it was **{computer_choice}**, what a loser', delete_after=15)

        class Cf(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)

            @discord.ui.button(label="Heads", style=discord.ButtonStyle.success)
            async def heads(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await heads_or_tails(interaction, 'heads')

            @discord.ui.button(label="Tails", style=discord.ButtonStyle.red)
            async def tails(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await heads_or_tails(interaction, 'tails')

        await interaction.response.send_message(content="Please choose **Heads** or **Tails**", view=Cf())



async def setup(client:commands.Bot) -> None:
    await client.add_cog(coinflip(client))
