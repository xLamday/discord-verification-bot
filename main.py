import asyncio, discord
from discord.ext import commands
from os
from dotenv import load_dotenv ## Makes your token stored in a secure way and inaccesible


load_env()
token = os.environ['DISCORD_BOT_TOKEN']
WELCOME_CHANNEL_ID = channel_id
VERIFY_ROLE_ID = verify_role_id


#prefix
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#the bot is ready, show online status
@bot.event
async def on_ready():
    print("bot is ready and online")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!hi"))


#redirected to welcome channel and asks for verification
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(WELCOME_CHANNEL_ID)
    embed=discord.Embed(title=" Welcome", description=f"Hello {member.mention}, thanks for joining!")
    embed.add_field(name="Verify to access all channels!", value="")
    await channel.send(embed=embed)

#verification
@bot.command()
async def verify(ctx):
    role = ctx.guild.get_role(VERIFY_ROLE_ID)
    await ctx.author.add_roles(role)
    await ctx.send(f"The <@&{VERIFY_ROLE_ID}> role has successfully been added to you. Congrats!")
    

bot.run(token)
