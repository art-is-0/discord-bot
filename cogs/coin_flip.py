import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class coin_flip(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("coin_flip is synced")

    # @commands.command()
    # async def sync(self) -> None:
    #     synced = await self.client.tree.sync()
    #     await print(f'Synced {len(synced)} commands')

    @app_commands.command(name='flip-a-coin', description='What did you think, you just flip a coin and guess the side!')
    async def coin_flip(interraction: discord.Interaction, which_side:str='heads'):
        lst = ['heads', 'tails']
        flipped = lst[random.randint(0,1)]
        message = f'You said ***{which_side}*** and it was ***{flipped}***.\n'
        if which_side.lower not in lst:
            message += 'Wrong input!'
        else:
            if which_side.lower() == flipped:
                message += '**You won, congratualtions!!!**'
            else:
                message += '**You lost, what a loser!**'

        await interraction.response.send_message(''.join(message))

async def setup(client:commands.Bot) -> None:
    await client.add_cog(coin_flip(client))