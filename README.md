# gunter-bot
Learing how to make a discord bot, just having fun

## To Do List
* Find a way to hold the code running while me not being active
* Add ffmpeg support
  * Need a ffmpeg library for python
  * Can ask ProTDC for help or infomation
* Add gambling to the bot
  * Add a economy where people can earn and use dollerydoos to gamble
  * Implement a way to gamble in the different minigames, such as blackjack and coinflip, perhaps add more minigames
  * Find a way to store that information of the player

## Completed
* First make a blackjack game in python, check out programming-projects-for-n00bz github repo for the game
  * Implement the blackjack game so it works in discord

* Make it so you type a slashcommand to start the game
  * Have the game be in a function so you don't need to use slashcommands to continue
  * Fix the response system
  * Using buttons for hit or stand
  * Fix the visuals, kinda done, at the beginnning and end of the card command use ``, to make it into code and more viewable in discord
    *  Maybe try to use embeds when the message is sent, does not look good
            
  * Add more time between each send, using asyncio.sleep()
  * Make the code more readable and add descriptions

  * Put the slash commands in cogs
    * Sync the damn code to discord, a cog did not have a description