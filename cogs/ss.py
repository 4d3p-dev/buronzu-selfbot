import discord
from discord.ext import commands
from pyppeteer import launch
import io
class Screenshot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ss(self, ctx, url: str):
        browser = await launch(headless=True, args=["--no-sandbox"])
        page = await browser.newPage()
        await page.goto(url)
        screenshot = await page.screenshot()
        await browser.close()
        with io.BytesIO(screenshot) as image_file:
            await ctx.send(file=discord.File(image_file, 'ss.png'))
async def setup(bot):
    await bot.add_cog(Screenshot(bot))
