import discord
from discord import app_commands
from discord.ext import commands
import discord_token

client = commands.Bot(command_prefix=',', intents = discord.Intents.all())
# client = discord.Intents.default()

@client.event
async def on_ready():
    print("Bot is up and running!")
    try:
        synced = await client.tree.sync()
        print('Synced')
    except Exception as e:
        print(e)

@client.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.mention} This is a slash command!', ephemeral=True)

client.run(discord_token.token())