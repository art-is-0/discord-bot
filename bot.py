import discord
import responses
import discord_token
from discord import app_commands
from discord.ext import commands
import random

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_reponse(user_message)

        match response:
            case 'annoying':
                for i in range(6):
                    response = responses.annoying_response(i)
                    await message.author.send(response)

            case str():
                await message.author.send(response) if is_private else await message.channel.send(response)

            case _:
                pass

    except Exception as e: 
        print(e)

async def annoying():
    pass


def run_discord_bot():
    TOKEN = discord_token.token()   # try to find out how to put the token into a .env file and get it to work.
    # TOKEN = DISCORD_TOKEN
    # intents = discord.Intents.all()
    # intents.message_content = True
    # client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='!', intents = discord.Intents.all()) # Watch the damn capatalization on the Bot, pain ahhhh


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')

    @client.tree.command(name="roll", description = "Rolls dices")
    async def roll(interaction: discord.Interaction, amount_of_dices:int=1, die_sides:int=6, modifers:str='+1'):
        message = f'**{amount_of_dices}d{die_sides} {modifers}** ='
        # message = ""

        for i in range(0, amount_of_dices):
            number = random.randint(1, die_sides)
            
            # if modifers[0] == '+':
            #     message += f'**{amount_of_dices}d{die_sides} {modifers}** = {number} {modifers} = {number + int(modifers[1])}\n'
            # else:
            #     message += f'**{amount_of_dices}d{die_sides} {modifers}** = {number} {modifers} = {number - int(modifers[1])}\n'

            if number == 20:
                message += f' | {number} {modifers} = **Natural Twenty**'
            else:
                if modifers[0] == '+':
                    message += f' | {number} {modifers} = **{number + int(modifers[1])}** '
                else:
                    message += f' | {number} {modifers} = **{number - int(modifers[1])}** '
                
            
        await interaction.response.send_message(f'{message} |')
        # await interaction.response.send_message(''.join(message))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        match user_message[0]:
            case '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)

            case _:
                await send_message(message, user_message, is_private=False)

        
    client.run(TOKEN)