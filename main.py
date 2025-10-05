import discord
from discord.ext import commands
from keep_alive import start
import logging
from dotenv import load_dotenv
import os

start() #Start the keep_alive server ##Command to test bot

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
@bot.command(aliases=["2", "hidup", "ngawor", "ksabar", "gamebayi", "taste",
                      "susu", "sekip", "aura", "hitam", "bukan",
                      "besok", "minggir", "ngetik", "ngocok", "anak",
                      "romantis", "gtw", "muak", "aas", "santai", "asu",
                      "najis", 'gaterima', 'menggoda', 'bangun', 'otw'])
#Remember
# to add
# aliases here
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

    # elif command_used == "":
    # embed.set_image(url="")

  # Set image based on the command used
  elif command_used == "2":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1354444598784557108/1422418681647992843/2_lah.jpg?ex=68dc9a20&is=68db48a0&hm=93659d3bb7fe2de2ec21bd2b424c240c67495e75bf5efbcf973a7dc68c5e3b9c&")
  elif command_used == "hidup":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422464631854727199/joko-widodo-is-my-spirit-v0-9x89ydyu34gf1.png?ex=68dcc4ec&is=68db736c&hm=d71f92c9b9871a40ea1fb31e17ff534c65eb65f83b977153f928633396f1095d&")
  elif command_used == "ngawor":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422475778364280882/a06e23e4ec128e68055ee802917f8e8a.png?ex=68dccf4d&is=68db7dcd&hm=7f11c5791d7d9428fc1629430be68e5056803e301ea535601433afee976e4387&")
  elif command_used == "ksabar":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1422476589924483102/images.png?ex=68dcd00f&is=68db7e8f&hm=38ce3d143c8f106e2911d8fd7bfb1f4ee6518b16d9d3005e41667ae94bfd6e4a&")
  elif command_used == "gamebayi":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294317715525642/IMG_2072.png?ex=68dfc9a0&is=68de7820&hm=20c7cc1e8a6e1c28cdd2b975ba5a041879fc2b5be2bd5c3869120731b1264abe&")
  elif command_used == "taste":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294326003339366/IMG_2071.png?ex=68dfc9a2&is=68de7822&hm=2967cda8e9d05718949f7d1f3563161104a589e6a520f02a02b12814f9b50a72&")
  elif command_used == "susu":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294336119865344/IMG_0904.jpg?ex=68dfc9a5&is=68de7825&hm=95afa658d9e2cafd58356936e91c129ee67f669ff3ac5d7f7d7a091d0905e04a&")
  elif command_used == "sekip":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294448959356948/FB_IMG_1751544896271.jpg?ex=68dfc9c0&is=68de7840&hm=218b87725498b53819318d0d05b763c7f3fa84d6218ee0cdf2d5711a2cd673b5&")
  elif command_used == "aura":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294515896254586/IMG_1956.png?ex=68dfc9d0&is=68de7850&hm=3a96a6d6fcf7021070d02932d3bc4f00b6b2fb17e2af82effadcef802bcf13bb&")
  elif command_used == "hitam":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294595541762048/FB_IMG_1748842845865.jpg?ex=68dfc9e3&is=68de7863&hm=256531b4a6df7da0aad9b49f49c59949e93d690450e3b406552759999d5ad2f2&")
  elif command_used == "bukan":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423294845572743268/FB_IMG_1748149411045.jpg?ex=68dfca1e&is=68de789e&hm=6382fb947d572ea564a8c79316b969c90260173fb2f695840130b2baf05f5847&")
  elif command_used == "besok":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423296203587584040/FB_IMG_1703431373507.png?ex=68dfcb62&is=68de79e2&hm=e3594409737ed9b84a94227963c63e781fe8e1b3a6345657ae75c7852a5be637&")
  elif command_used == "minggir":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423297380232462376/1423295752364625941remix-1759410919148.png?ex=68dfcc7b&is=68de7afb&hm=6716aa83ddd94a09e984a4fbf750c85ae0c1418d8dd1491eeffc80c34d04dc4e&")
  elif command_used == "ngetik":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423299523744108635/image.png?ex=68dfce7a&is=68de7cfa&hm=492bb89a90ea531201f42431340863c4dd98511401dda63faf9699bf10907216&")
  elif command_used == "ngocok":
    embed.set_image(url="https://media.discordapp.net/attachments/1422464446017699840/1423301841495523480/image.png?ex=68dfd0a2&is=68de7f22&hm=061be4a8448c19c6efbe88f1a87f22e5cf1a2f6d2729829bd91073740f5462f6&=&format=webp&quality=lossless&width=1063&height=349")
  elif command_used == "anak":
    embed.set_image(url="https://media.discordapp.net/attachments/1422464446017699840/1423302711310418030/image.png?ex=68dfd172&is=68de7ff2&hm=42cc4ff94295368d38a0f976c6aac2429bb3ad88d94c0af3a5778a196dcfb868&=&format=webp&quality=lossless&width=591&height=268")
  elif command_used == "romantis":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423306625418264667/image.png?ex=68dfd517&is=68de8397&hm=b0321780f900570d70e734117d2661a343f1b5730432801c92e836e957e94260&")
  elif command_used == "gtw":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1423321325564592188/image.png?ex=68dfe2c8&is=68de9148&hm=e9f9378cc6249d2b60f9bcc117cedc82dd078f86eebf7e77c7b54e5e6cb77669&")
  elif command_used == "muak":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424012745581269084/images.png?ex=68e266b7&is=68e11537&hm=92e8824183abeaef1c1c5296e465ae20a4f81e46c5756e771f67e7cdac825a7e&")
  elif command_used == "aas":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424014037951320104/1f6bd6cd47e307759f4dad1ad2ab273a.png?ex=68e267eb&is=68e1166b&hm=8bc73da5e253e45e97bd4332d8eab8dd6cfc959d93d694f3fe81d92b0a3baa92&")
  elif command_used == "santai":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424014461504852101/sdgs.png?ex=68e26850&is=68e116d0&hm=faed9d3db1d4b2205cdece6d176b65c6a0324f9cc90838c61608840b6a8fd5ad&")
  elif command_used == "asu":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424015262201679986/ed26f633d4db72061746ef33d13084e0.png?ex=68e311cf&is=68e1c04f&hm=4eca7491a113cd3640407b4d9c91d64b2cdc72a5ca19fdc14762999b4062a914&")
  elif command_used == "najis":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424015282707370005/Z.png?ex=68e311d4&is=68e1c054&hm=e046b4b721bb057dc51b86a95435bd9f1db032dccc75ca78899b2e52d5903d26&")
  elif command_used == "gaterima":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424015429956800563/images.png?ex=68e311f7&is=68e1c077&hm=564e9c441e779d3a34922b56bea0b43b1c4703c2e930abddfe43720b153c0ceb&")
  elif command_used == "menggoda":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424015816135016558/images.png?ex=68e31253&is=68e1c0d3&hm=9ba39e5e2d1e67731e807c0147593a5a755a3913b7a8340c52478872fe6cb080&")
  elif command_used == "bangun":
    embed.set_image(url="https://cdn.discordapp.com/attachments/1422464446017699840/1424016097644118126/f1debd23fce5a7dc48ad539009b27879.png?ex=68e31296&is=68e1c116&hm=0d146c960f8ac90c01316d7c022e5636b8656e6ccb34df9f7734309ce8154d52&")
  elif command_used == "otw":
    embed.set_image(url="https://media1.tenor.com/m/PEZPq1ey8SgAAAAd/capybara-crocodile.gif")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")
  elif command_used == "":
    embed.set_image(url="")


  await ctx.send(embed=embed)








# This should be the last line in your file
bot.run(token, log_handler=handler, log_level=logging.INFO)

