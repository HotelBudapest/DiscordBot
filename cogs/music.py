import discord
from discord.ext import commands
from utils.audio_helper import get_youtube_audio_url
from discord import FFmpegPCMAudio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url: str):
        print("Play command triggered")
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            await ctx.send("You need to be in a voice channel to play audio.")
            return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            voice = await voice_channel.connect()

        audio_url = get_youtube_audio_url(url)
        if audio_url:
            source = FFmpegPCMAudio(audio_url)
            voice.play(source)
            await ctx.send(f"Now playing audio from: {url}")
        else:
            await ctx.send(f"Couldn't retrieve audio from: {url}")

    @commands.command()
    async def stop(self, ctx):
        print("Stop command triggered")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Audio stopped.")
        else:
            await ctx.send("No audio is playing right now.")

    @commands.command()
    async def leave(self, ctx):
        print("Leave command triggered")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
            await ctx.send("Disconnected from the voice channel.")
        else:
            await ctx.send("I am not in a voice channel.")

async def setup(bot):
    await bot.add_cog(Music(bot))
    print("Music cog loaded")
