import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class economy(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client
