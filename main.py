import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
  print(f"{bot.user.name} aktif!")


@bot.command()
async def gel(ctx):
  if ctx.author.voice:
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"🎤 {channel.name} kanalına katıldım!")
  else:
    await ctx.send("❌ Önce bir ses kanalına girmelisin!")


@bot.command()
async def cık(ctx):
  if ctx.voice_client:
    await ctx.voice_client.disconnect()
    await ctx.send("👋 Ses kanalından ayrıldım!")
  else:
    await ctx.send("❌ Zaten bir ses kanalında değilim!")


bot.run(os.getenv("TOKEN"))
