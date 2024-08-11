import discord
from discord.ext import commands
# importing cool libs

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='i.', intents=intents) 
# making prefix for our ice cream bot

@bot.command()
async def icecream(ctx): # this is command 
    await ctx.send('I like ice cream') # this is response
# you can make more commands


bot.run('ur_token')
# yay ice cream bot
