import discord
import random
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")
    print("--------------")

@client.command()
async def hi(ctx):
    await ctx.send("Hello, I am Arian's Bot\nArian is dumb\nHow may I help you?")
    
@client.command()
async def bye(ctx):
    await ctx.send("Goodbye\nSee you again, Arian is still dumb!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1182350182109691936)
    await channel.send(f"Kire {member.mention} mama, welcome to the server!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1182350182109691936)
    await channel.send(f"Oh no :( Bye {member.mention}")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('music.flac')
        player = voice.play(source)
    else: 
        await ctx.send('User must be in a voice channel to run this command')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('I left the voice channel')
    else: 
        await ctx.send('I am not in a voice channel')

@client.command(pass_context = True)
async def toss(ctx):
    stuff = ["Heads", "Tails"]
    index = random.randint(0,1)
    await ctx.send(f"You have got: {stuff[index]}")

@client.command(pass_context = True)
async def dice_roll(ctx):
    await ctx.send(f"You have rolled: {random.randint(1,6)}")

@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No audio is playing right now.")
    
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("No audio is playing right now.")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send("No audio is playing right now.")

@client.command(pass_context = True)
async def play(ctx, *, arg):
        voice = ctx.guild.voice_client
        arg_new = f"D:\Chernobylite\Artcell\Artcell\Aniket Prantor\{arg}.flac"
        print(arg_new)
        source = FFmpegPCMAudio(arg_new)
        player = voice.play(source)

client.run('MTE4MjM0NDI0NDE1MzgxNTE1MQ.GoXDYU.zjS13MQZ8CuiT4hAl7y-CFqtWESQUXcwxM-Mz0')