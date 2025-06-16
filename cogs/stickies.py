from discord.ext import commands
import discord

class StickyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stickies = {}

    @commands.command()
    async def stick(self, ctx, *, msg):
        """Sticks a message to the current channel."""
        old = self.stickies.get(ctx.channel.id)
        if old:
            await old.delete()
        sticky_msg = await ctx.send(f"📌 {msg}")
        self.stickies[ctx.channel.id] = sticky_msg

    @commands.command()
    async def stickstop(self, ctx):
        """Stops the current sticky message in the channel."""
        if ctx.channel.id in self.stickies:
            await ctx.send("Sticky message paused.")

    @commands.command()
    async def stickremove(self, ctx):
        """Removes the sticky message from the channel."""
        msg = self.stickies.pop(ctx.channel.id, None)
        if msg:
            await msg.delete()
            await ctx.send("Sticky message removed.")

async def setup(bot):
    await bot.add_cog(StickyCog(bot))