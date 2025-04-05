import os
import dotenv
from discord.ext import commands
bot = commands.Bot(
    [
        "-",
    ],
    description="ぶろんずだよ♪よろしくね♪",
)
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.ss")
    await bot.load_extension("cogs.janken")
    await bot.load_extension("cogs.quote")
    await bot.load_extension("cogs.5000")
dotenv.load_dotenv()
bot.run(os.getenv("buronzu"))
