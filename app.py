# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

win = 0
loss = 0

@bot.command(name='add_win')
async def add_win(ctx):
    global win
    win += 1
    print(win)

    
    response = f"You won again! That's {win} wins! Neat!"
    await ctx.send(response)

@bot.command(name='add_loss')
async def add_loss(ctx):
    global loss
    loss += 1
    print(loss)

    
    response = f"You lost again. That's {loss} losses. Bummer!"
    await ctx.send(response)

bot.run(TOKEN)