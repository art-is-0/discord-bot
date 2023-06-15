import discord
import responses
import discord_token
import blackjack
from discord import app_commands
from discord.ext import commands
import random
import asyncio

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






    # Slash commands

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




    @client.tree.command(name='blackjack', description="Play blackjack against the bot!")
    async def play_blackjack(interraction: discord.Interaction):

        # The Card class definition
        class Card:
            def __init__(self, suit, value, card_value):
                
                # Suit of the Card like Spades and Clubs
                self.suit = suit
        
                # Representing Value of the Card like A for Ace, K for King
                self.value = value
        
                # Score Value for the Card like 10 for King
                self.card_value = card_value

        # The type of suit
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    
        # The suit value 
        suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    
        # The type of card
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
        # The card value
        cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    
        # The deck of cards
        deck = []
    
        # Loop for every type of suit
        for suit in suits:
    
            # Loop for every type of card in a suit
            for card in cards:
    
                # Adding card to the deck
                deck.append(Card(suits_values[suit], card, cards_values[card]))

        # Function to print the cards
        def print_cards(cards, hidden):

            s = ""
            for card in cards:
                s += "\t______ "
            if hidden:
                s += "\t______ "

            s += "\n"
            for card in cards:
                s += "\t|    | "
            if hidden:
                s += "\t|    | "

            s += "\n"
            for card in cards:
                if card.value == '10':
                    s += "\t| {} | ".format(card.value)
                else:
                    s += "\t| {}  | ".format(card.value)
            if hidden:
                s += "\t| ## | " 

            s += "\n"
            for card in cards:
                s += "\t|  {} | ".format(card.suit)
            if hidden:
                s += "\t| ## | "

            s += "\n"
            for card in cards:
                s += "\t|____| "
            if hidden:
                s += "\t|____| "

            return (''.join(s))
            

        # Cards for both dealer and player
        player_cards = []
        dealer_cards = []
    
        # Scores for both dealer and player
        player_score = 0
        dealer_score = 0
    
        # Initial dealing for player and dealer
        while len(player_cards) < 2:
            message = ''

            # Randomly dealing a card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
    
            # Updating the player score
            player_score += player_card.card_value
    
            # In case both the cards are Ace, make the first ace value as 1 
            if len(player_cards) == 2:
                if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                    player_cards[0].card_value = 1
                    player_score -= 10
    
            # Print player cards and score      
            message += "PLAYER CARDS: \n"
            message += print_cards(player_cards, False)
            message += f"\nPLAYER SCORE = {player_score} \n\n"
    
    
            # Randomly dealing a card
            dealer_card = random.choice(deck)
            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)
    
            # Updating the dealer score
            dealer_score += dealer_card.card_value
    
            # Print dealer cards and score, keeping in mind to hide the second card and score
            message += "DEALER CARDS: \n"
            if len(dealer_cards) == 1:
                message += print_cards(dealer_cards, False)
                message += f"\nDEALER SCORE = {dealer_score} \n"
            else:
                message += print_cards(dealer_cards[:-1], True)   
                message += f"\nDEALER SCORE = {dealer_score - dealer_cards[-1].card_value}\n"
    
    
            # In case both the cards are Ace, make the second ace value as 1 
            if len(dealer_cards) == 2:
                if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                    dealer_cards[1].card_value = 1
                    dealer_score -= 10
    
            await interraction.channel.send(''.join(message))
            await asyncio.sleep(0.2)
    
        message = ''
        # Player gets a blackjack   
        if player_score == 21:
            message += "PLAYER HAS A BLACKJACK!!!!\n"
            message += "PLAYER WINS!!!!\n"
            await interraction.channel.send(''.join(message))
            quit()
    
        # # Print dealer and player cards
        # message += "DEALER CARDS: \n"
        # message += print_cards(dealer_cards[:-1], True), '\n'
        # message += "DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value, '\n'
    
        # print() 
    
        message += "PLAYER CARDS: \n"
        message += print_cards(player_cards, False)
        message += f"PLAYER SCORE = {player_score} \n"
        await interraction.channel.send(''.join(message))
        await asyncio.sleep(0.2)


    
        # Managing the player moves
        while player_score < 21:
            message = ''
            await interraction.channel.send("Enter H to Hit or S to Stand : ")

            def check(m):
                return m.author == interraction.user and m.channel == interraction.channel
            
            choice = await client.wait_for('message', check=check)

            try:
            # # Sanity checks for player's choice
            # if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            #     await interraction.channel.send("Wrong choice!! Try Again")
            #     await asyncio.sleep(0.2)
    
                # If player decides to HIT
                if choice.upper() == 'H':
        
                    # Dealing a new card
                    player_card = random.choice(deck)
                    player_cards.append(player_card)
                    deck.remove(player_card)
        
                    # Updating player score
                    player_score += player_card.card_value
        
                    # Updating player score in case player's card have ace in them
                    c = 0
                    while player_score > 21 and c < len(player_cards):
                        if player_cards[c].card_value == 11:
                            player_cards[c].card_value = 1
                            player_score -= 10
                            c += 1
                        else:
                            c += 1    
        
                    # Print player and dealer cards
                    message += "DEALER CARDS: \n"
                    message += print_cards(dealer_cards[:-1], True)
                    message += f"\nDEALER SCORE = {dealer_score - dealer_cards[-1].card_value} \n"
        
                    message += "PLAYER CARDS: \n"
                    message += print_cards(player_cards, False)
                    message += f"\nPLAYER SCORE = { player_score}\n"
                    await interraction.channel.send(''.join(message))
                    await asyncio.sleep(0.2)
                    
                # If player decides to Stand
                if choice.upper() == 'S':
                    break

            except:
                await interraction.channel.send("Wrong choice!! Try Again")
                await asyncio.sleep(0.2)
        message = ''
        # Print player and dealer cards
        message += "PLAYER CARDS: \n"
        message += print_cards(player_cards, False)
        message += f"\nPLAYER SCORE = {player_score} \n"
    
        message += "\nDEALER IS REVEALING THE CARDS....\n"
    
        message += "\nDEALER CARDS: \n"
        message += print_cards(dealer_cards, False)
        message += f"\nDEALER SCORE = { dealer_score}\n"
        await interraction.channel.send(''.join(message))
        await asyncio.sleep(0.2)
    
        # Check if player has a Blackjack
        if player_score == 21:
            await interraction.channel.send("PLAYER HAS A BLACKJACK")
            quit()
    
        # Check if player busts
        if player_score > 21:
            await interraction.channel.send("PLAYER BUSTED!!! GAME OVER!!!")
            quit()


        # Managing the dealer moves
        while dealer_score < 17:
            message = ''
    
            await interraction.response.send_message("DEALER DECIDES TO HIT.....")
    
            # Dealing card for dealer
            dealer_card = random.choice(deck)
            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)
    
            # Updating the dealer's score
            dealer_score += dealer_card.card_value
    
            # Updating player score in case player's card have ace in them
            c = 0
            while dealer_score > 21 and c < len(dealer_cards):
                if dealer_cards[c].card_value == 11:
                    dealer_cards[c].card_value = 1
                    dealer_score -= 10
                    c += 1
                else:
                    c += 1
    
            # print player and dealer cards
            message += "PLAYER CARDS: \n"
            message += print_cards(player_cards, False)
            message += f"\nPLAYER SCORE = {player_score}\n\n"
    
            message += "DEALER CARDS: \n"
            message += print_cards(dealer_cards, False)
            message += f"\nDEALER SCORE = {dealer_score}\n"      
    
            await interraction.channel.send(''.join(message))
            await asyncio.sleep(0.2)
    
        # Dealer busts
        if dealer_score > 21:        
            await interraction.channel.send("DEALER BUSTED!!! YOU WIN!!!") 
            quit()  
    
        # Dealer gets a blackjack
        if dealer_score == 21:
            await interraction.channel.send("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
            quit()
    
        # TIE Game
        if dealer_score == player_score:
            await interraction.channel.send("TIE GAME!!!!")
            quit()
    
        # Player Wins
        elif player_score > dealer_score:
            await interraction.channel.send("PLAYER WINS!!!")                 
            quit()

        # Dealer Wins
        else:
            await interraction.channel.send("DEALER WINS!!!")                 
            quit()




    client.run(TOKEN)