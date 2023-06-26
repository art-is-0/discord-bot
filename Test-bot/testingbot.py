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

@client.tree.command(name='shutdown', description='Shutting down the bot')
async def shutdown(interraction: discord.Interaction):
    await interraction.response.send_message(content='*Shutting down the bot*')
    await client.close()

@client.tree.command(name='embeds')
async def test(interraction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.dark_gold()
        ,description='something\rsomething\r'
    )

    await interraction.channel.send(embed=embed)

class TestButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="test")
    async def test(self, interaction: discord.Interaction, Button: discord.ui.Button):
        pass

@client.tree.command(name='something')
async def something(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.dark_gold()
        ,description='something\rsomething\r'
    )

    await interaction.response.send_message(embed=embed, view=TestButtons())

# @client.tree.command(name='blackjack-test')
# async def test(interaction: discord.Interaction):
#     class Card:
#         def __init__(self, suit, value, card_value):
            
#             # Suit of the Card like Spades and Clubs
#             self.suit = suit

#             # Representing Value of the Card like A for Ace, K for King
#             self.value = value

#             # Score Value for the Card like 10 for King
#             self.card_value = card_value

    
#     # The type of suit
#     suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

#     # The suit value 
#     suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

#     # The type of card
#     cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#     # The card value
#     cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

#     # The deck of cards
#     deck = []

#     # Loop for every type of suit
#     for suit in suits:

#         # Loop for every type of card in a suit
#         for card in cards:

#             # Adding card to the deck
#             deck.append(Card(suits_values[suit], card, cards_values[card]))
        

#     import random
#     # Function to print the cards
#     def print_cards(cards, hidden):

#         s = ""
#         for card in cards:
#             s += "\t______ "
#         if hidden:
#             s += "\t______ "

#         s += "\n"
#         for card in cards:
#             s += "\t|    | "
#         if hidden:
#             s += "\t|    | "

#         s += "\n"
#         for card in cards:
#             if card.value == '10':
#                 s += "\t| {} | ".format(card.value)
#             else:
#                 s += "\t| {}  | ".format(card.value)
#         if hidden:
#             s += "\t| ## | " 

#         s += "\n"
#         for card in cards:
#             s += "\t|  {} | ".format(card.suit)
#         if hidden:
#             s += "\t| ## | "

#         s += "\n"
#         for card in cards:
#             s += "\t|____| "
#         if hidden:
#             s += "\t|____| "

#         return (''.join(s))

#     dealers_cards = []
#     for i in range(3):
#         dealers_cards.append(random.choice(deck))
#     # await interaction.response.send_message(print_cards(dealers_cards, False))
#     message = ''
#     message += 'Something\n'
#     message += print_cards(dealers_cards, False)
#     message += '\nSomething',4, '\n'
#     await interaction.response.send_message(''.join(message))

client.run(discord_token.token())