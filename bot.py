import discord
import responses
import discord_token

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
    TOKEN = discord_token.token()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

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