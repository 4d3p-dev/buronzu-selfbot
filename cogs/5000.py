from discord.ext import commands

class Cog5000(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="5000")
    async def generate_image(self, ctx, top: str = "", bottom: str = ""):
        url = f"https://gsapi.cbrx.io/image?top={top}&bottom={bottom}"
        await ctx.send(url)

async def setup(bot):
    await bot.add_cog(Cog5000(bot))
