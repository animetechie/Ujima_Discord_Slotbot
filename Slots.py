import random
import discord

# List of Pokémon to use as symbols
pokemon = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Jigglypuff', 'Snorlax']

# Starting Xtals balance for the player
xtals = 100

def run_slot_machine(bet):
  """Run the slot machine with the given bet amount.
  Returns the player's winnings from the spin.
  """
  # Spin the reels
  reel1 = random.choice(pokemon)
  reel2 = random.choice(pokemon)
  reel3 = random.choice(pokemon)

  # Calculate winnings
  if reel1 == reel2 == reel3:
    # Jackpot!
    winnings = bet * 3
  elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
    # Two matching symbols
    winnings = bet * 2
  else:
    # No matching symbols
    winnings = 0

  return winnings

client = discord.Client()

@client.event
async def on_message(message):
  # Ignore messages from other bots
  if message.author.bot:
    return

  # Check if the message is a command to play the slot machine
  if message.content.startswith('!slot'):
    # Get the bet amount from the message
    try:
      bet = int(message.content.split()[1])
    except (IndexError, ValueError):
      await message.channel.send('Please specify a valid bet amount.')
      return

    # Make sure the player has enough Xtals to place the bet
    if xtals < bet:
      await message.channel.send('You do not have enough Xtals to place that bet.')
      return

    # Run the slot machine and update the player's Xtals balance
    winnings = run_slot_machine(bet)
    xtals += winnings
    if winnings > 0:
      await message.channel.send(f'You won {winnings} Xtals!')
    else:
      await message.channel.send('Sorry, you lost your bet.')

client.run('YOUR_BOT_TOKEN_HERE')
