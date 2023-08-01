import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class roll(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("roll is synced")

    # @commands.command()
    # async def sync(self) -> None:
    #     synced = await self.client.tree.sync()
    #     await print(f'Synced {len(synced)} commands')

    @app_commands.command(name="roll", description = "Rolls dices")
    async def roll(interaction: discord.Interaction, amount_of_dices:int=1, die_sides:int=6, modifers:str='+1'):
        message = f'**{amount_of_dices}d{die_sides} {modifers}** =\n'
        # message = ""
        # modi = modifers[:1]
        try:
            for i in range(0, amount_of_dices):
                number = random.randint(1, die_sides)
                
                # if modifers[0] == '+':
                #     message += f'**{amount_of_dices}d{die_sides} {modifers}** = {number} {modifers} = {number + int(modifers[1])}\n'
                # else:
                #     message += f'**{amount_of_dices}d{die_sides} {modifers}** = {number} {modifers} = {number - int(modifers[1])}\n'

                if number == 20 and die_sides == 20:
                    message += f'\t\t\t\t\t{number} {modifers} = **Nat Twenty**\n'
                elif number == 1 and die_sides == 20:
                    message += f'\t\t\t\t\t{number} {modifers} = **Nat One**\n'
                else:
                    message += f'\t\t\t\t\t{number} {modifers} = **{number + int(modifers)}**\n'
            await interaction.response.send_message(f'{message}')
        except:
            await interaction.response.send_message('**Invalid input**, did you try to write modifers like this **+1**')


async def setup(client:commands.Bot) -> None:
    await client.add_cog(roll(client))