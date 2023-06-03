import discord
import responses
import discord_token
from discord import app_commands
from discord.ext import commands
import random

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
            

        # await interaction.response.send_message(''.join(message))

    @client.tree.command(name='roll-stats', description='Roll for stats')
    async def roll_stats(interraction: discord.Interaction, die_sides:int=6):
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

    @client.tree.command(name='shutdown', description='Shutting down the bot')
    async def shutdown(interraction: discord.Interaction):
        await interraction.response.send_message(content='*Shutting down the bot*')
        await client.close()

    @client.tree.command(name='flip-a-coin', description='What did you think, you just flip a coin and guess the side!')
    async def coin_flip(interraction: discord.Interaction, which_side:str='heads'):
        lst = ['heads', 'tails']
        flipped = lst[random.randint(0,1)]
        message = f'You said {which_side} and it was {flipped}.\n'
        if which_side.lower() == lst[0] or lst[1]:
            if which_side.lower() == flipped:
                message += '**You won, congratualtions!!!**'
            else:
                message += '**You lost, what a loser!**'
        else:
            message += 'Wrong input!'

        await interraction.response.send_message(''.join(message))

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