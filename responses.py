import random

def get_reponse(message: str) -> str:
    p_message = message.lower() 

    words = p_message.split()

    if 'stop' and 'annoying' in words:
        return 'annoying'

    if 'hello' in words:
        return 'Gunter'

    if 'titties' or 'boobs' or 'titty' in words:
        return 'https://tenor.com/view/adventure-time-chris-evans-abs-gunther-gif-3540409'

    if p_message == '!roll':
        return str(random.randint(1,6))

    if p_message == '!dance':
        return 'https://tenor.com/view/adventure-time-dance-dancing-gif-21794260'

    if p_message == '!sad':
        return 'https://tenor.com/view/sad-adventure-time-gunther-leaving-departing-gif-4674669'

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    # return 

    return 'I didn\'t understand what you wrote. Try typing "!help".'

def annoying_response(number: int) -> str:

    if number == 0:
        return 'GUNTER! GUNTER!'

    if number == 1:
        return '`-silent stare-`'

    if number == 2:
        return 'https://tenor.com/view/adventure-time-gunter-gunther-adventuret-time-gunther-adventure-time-gunter-gif-11018947'

    if number == 3:
        return 'https://tenor.com/view/gunter-wenk-adventure-time-stressed-angry-gif-3895478'

    if number == 4:
        return 'https://tenor.com/view/gunter-pingu-adventure-time-fart-prout-gif-14404719'
    
    if number == 5:
        return 'https://tenor.com/view/gunther-adventure-time-gif-8955418'
