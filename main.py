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

  game = discord.Activity(type=discord.ActivityType.watching,
                          name="The Realm of DisChill")
  await bot.change_presence(activity=game)



# # Event: New member joins the server
# @bot.event
# async def on_member_join(member):
#   channel = discord.utils.get(member.guild.text_channels, name='general')
#   if channel:
#     # Create a welcome embed card
#     embed = discord.Embed(
#         title=f"Welcome to {member.guild.name}!",
#         description=f"Hello {member.mention}! We're glad to have you join us."
#     )
#
#     # Add member information
#     embed.add_field(name="Joined", value=member.joined_at.strftime("%B %d, %Y"), inline=True)
#
#     # Set thumbnail to member's avatar
#     embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
#
#     await channel.send(embed=embed)



# Command: Responds with an embedded image
@bot.command(aliases=["2", "hidup", "ngawor", "ksabar"]) #Remember to add aliases here
async def list(ctx):
  embed = discord.Embed()

  # Check which command was used
  command_used = ctx.invoked_with.lower()

  if command_used == "list":
    # Get the list command itself
    list_command = bot.get_command("list")

    # Get aliases dynamically from the command
    aliases = list_command.aliases

    embed.title = ("Commands List"
                   "\n- - - - - - - - - - - - - - - - - - - -\n")
    embed.description = "\n".join(aliases)

  # Set image based on the command used
  elif command_used == "2":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1354444598784557108/1422418681647992843/2_lah.jpg?ex=68dc9a20&is=68db48a0&hm=93659d3bb7fe2de2ec21bd2b424c240c67495e75bf5efbcf973a7dc68c5e3b9c&")
  elif command_used == "hidup":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422464631854727199/joko-widodo-is-my-spirit-v0-9x89ydyu34gf1.png?ex=68dcc4ec&is=68db736c&hm=d71f92c9b9871a40ea1fb31e17ff534c65eb65f83b977153f928633396f1095d&")
  elif command_used == "ngawor":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422475778364280882/a06e23e4ec128e68055ee802917f8e8a.png?ex=68dccf4d&is=68db7dcd&hm=7f11c5791d7d9428fc1629430be68e5056803e301ea535601433afee976e4387&")
  elif command_used == "ksabar":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422476589924483102/images.png?ex=68dcd00f&is=68db7e8f&hm=38ce3d143c8f106e2911d8fd7bfb1f4ee6518b16d9d3005e41667ae94bfd6e4a&")


  await ctx.send(embed=embed)








# This should be the last line in your file
bot.run(token, log_handler=handler, log_level=logging.INFO)

