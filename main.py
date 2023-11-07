import asyncio, discord
from discord.ext import commands

#global variables
TOKEN = "token"
WELCOME_CHANNEL_ID = channel_id
VERIFY_ROLE_ID = verify_role_id


#prefix
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#the bot is ready, show online status
@bot.event
async def on_ready():
    print("bot is ready and online")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!hi"))

#when typed !hi, yo:) output by the bot
@bot.command
async def hi(ctx):
    await ctx.send("yo:)")

#redirected to welcome channel and asks for verification
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(WELCOME_CHANNEL_ID)
    embed=discord.Embed(title=" Welcome", description=f"Hello {member.mention}, thanks for joining!")
    embed.add_field(name="Verify to access all channels!", value="")
    await channel.send(embed=embed)


#verification
# @bot.command()
# async def verify(ctx):
    


#command= !clr
@bot.command()
async def clr(ctx, count=1):
    messages = await ctx.channel.purge(limit=count+1)
    await ctx.send(f'{len(messages)-1} messages were deleted!', delete_after=5)

        
bot.run(TOKEN)
