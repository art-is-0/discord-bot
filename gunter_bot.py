import discord
import responses
import discord_token
import application_id
from discord import app_commands
from discord.ext import commands
import random
import asyncio
import os


TOKEN = discord_token.token()   # try to find out how to put the token into a .env file and get it to work.
# TOKEN = DISCORD_TOKEN
# intents = discord.Intents.all()
# intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents = discord.Intents.all(), application_id=application_id.id()) # Watch the damn capatalization on the Bot, pain ahhhh

@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    synced = await client.tree.sync()
    print(f'Synced {len(synced)} command(s)')

async def send_message(message, user_message, is_private):
    '''
    A function that is used to send messages back to the sender, channel or dms. 
    The function gets the message, the message send/posted and if it is supposed to be sent to the persons dms.

    Most often the function sends back a response based on the user_message, if the user_message does not fit
    any of the responses then it passes the function and returns nothing.
    '''
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

# Get the current directory (where your Python script is located)
current_directory = os.path.dirname(__file__)

# Specify the path to the "cogs" folder using os.path.join()
cogs_folder_path = os.path.join(current_directory, "cogs")

# Loading in the slash commands
async def load():
    # Loops through the "cogs" folder to load every file that ends in .py
    for file in os.listdir(cogs_folder_path):
        if file.endswith('.py'):
            if file.startswith('template'):
                pass
            elif file.startswith('test'):
                pass
            else:
                await client.load_extension(f'cogs.{file[:-3]}')    


# client.run(TOKEN)

# Starting function
async def main():
    # To load the slash commands and the bot at the same time
    await load()
    await client.start(TOKEN)


# Runs the start function
asyncio.run(main())