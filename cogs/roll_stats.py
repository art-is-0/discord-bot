import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class roll_stats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("roll_stats is synced")

    # @commands.command()
    # async def sync(self) -> None:
    #     synced = await self.client.tree.sync()
    #     await print(f'Synced {len(synced)} commands')

    @app_commands.command(name='roll-stats', description='Roll for stats')
    async def roll_stats(self, interraction: discord.Interaction, die_sides:int=6):
        message = ''
        match die_sides:
            case 6:
                for i in range(6):
                    number = 0
                    lst = []
                    for i in range(4):
                        lst.append(random.randint(1,6))
                    lst.remove(min(lst))
                    for i in range(len(lst)):
                        number += lst[i]
                    message += (f'**4d6** - the lowest = {number}\n')
            case 20: 
                for i in range(6):
                    number = 0
                    number = random.randint(5,20)
                    message += (f'**1d20**, 5 or more = {number}\n')
            case _:
                message = f'**Not a valid input!**'
        await interraction.response.send_message(''.join(message))  


async def setup(client:commands.Bot) -> None:
    await client.add_cog(roll_stats(client))