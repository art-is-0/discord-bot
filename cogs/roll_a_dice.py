import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class roll_a_dice(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("roll_a_dice is synced")


    @app_commands.command(name='roll-a-dice', description='you shall roll a dice')
    async def roll_a_dice(self, interaction: discord.Interaction):
        
        async def message_print(interaction, dice_type, rolled):
                await interaction.response.send_message(content=f'On a **{dice_type}**, you rolled a **{rolled}**.', delete_after=30)
                
        class Roll(discord.ui.View):

            def __init__(self):
                super().__init__(timeout=None)

            @discord.ui.button(label="D4", style=discord.ButtonStyle.success)
            async def D4(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D4', random.randint(1,4))
            
            @discord.ui.button(label="D6", style=discord.ButtonStyle.success)
            async def D6(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D6', random.randint(1,6))

            @discord.ui.button(label="D8", style=discord.ButtonStyle.success)
            async def D8(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D8', random.randint(1,8))

            @discord.ui.button(label="D10", style=discord.ButtonStyle.success)
            async def D10(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D10', random.randint(1,10))

            @discord.ui.button(label="D20", style=discord.ButtonStyle.success)
            async def D20(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D20', random.randint(1,20))

            @discord.ui.button(label="D100", style=discord.ButtonStyle.success)
            async def D100(self, interaction: discord.Interaction, Button: discord.ui.Button):
                await asyncio.sleep(1)
                await message_print(interaction, 'D100', random.randint(1,100))

        await interaction.response.send_message(content="Please roll a **dice**, by pressing a **button**", view=Roll(), delete_after=30)


async def setup(client:commands.Bot) -> None:
    await client.add_cog(roll_a_dice(client))
