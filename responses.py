import random

def get_reponse(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there!'

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    return 

    # return 'I didn\'t understand what you wrote. Try typing "help".'

