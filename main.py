import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)


# Event: Bot is ready to use
@bot.event
async def on_ready():
  print(f'Bot is ready. Logged in as {bot.user}.')


# Event: New member joins the server
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}!')


# Command: Responds with an embedded image
@bot.command(aliases=["hi", "greet"])  # Add alternative command names here
async def hello(ctx):
  embed = discord.Embed(
      color=discord.Color.black()
  )

  # Check which command was used
  command_used = ctx.invoked_with.lower()

  if command_used == "hello":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1354444598784557108/1422418681647992843/2_lah.jpg?ex=68dc9a20&is=68db48a0&hm=93659d3bb7fe2de2ec21bd2b424c240c67495e75bf5efbcf973a7dc68c5e3b9c&")
  elif command_used == "hi":
    embed.set_image(url="YOUR_HI_IMAGE_URL")
  elif command_used == "greet":
    embed.set_image(url="YOUR_GREET_IMAGE_URL")

  await ctx.send(embed=embed)


# This should be the last line in your file
bot.run(token, log_handler=handler, log_level=logging.INFO)

