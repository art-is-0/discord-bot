import discord
from discord.ext import commands
from colorama import Back, Fore, Style
from dotenv import load_dotenv
import os
import time
import platform

load_dotenv()

# test_guild = int(os.getenv('TEST_GUILD'))
# test_guild = discord.Object(id=test_guild)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
APPLICATION_ID = os.getenv('APPLICATION_ID')

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents().all(), application_id=APPLICATION_ID)
        self.initial_extensions = [
                            'cogs.blackjack',
                            'cogs.coin_flip',
                            'cogs.coinflip',
                            'cogs.roll_a_dice',
                            'cogs.roll_dnd',
                            'cogs.roll_stats',
                            'cogs.shutdown',
                            # 'cogs.testcog'
                            'cogs.selectmenus'
                          ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            try: 
                await self.load_extension(ext)  
            except Exception as e:
                print('Failed to load extension %s.', ext)
                print(e)

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        # synced = await self.tree.sync()
        # print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands" + Fore.RESET)


client = Client()

from typing import Literal, Optional

@client.command()
@commands.guild_only()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

client.run(DISCORD_TOKEN)