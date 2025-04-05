import random
from discord.ext import commands

class Janken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def janken(self, ctx, choice: str):
        choices = ['グー', 'チョキ', 'パー']
        bot_choice = random.choice(choices)
        if choice not in choices:
            await ctx.send("「グー」「チョキ」「パー」のいずれかを選んでください。")
            return
        result = "[あいこ](https://nemtudo.me/e/DzX1)" if bot_choice == choice else (
            "[残念](https://nemtudo.me/e/hUK3)" if (bot_choice == 'グー' and choice == 'チョキ') or 
            (bot_choice == 'チョキ' and choice == 'パー') or 
            (bot_choice == 'パー' and choice == 'グー') else "[勝利](https://nemtudo.me/e/c1wb)"
        )
        await ctx.send(f"【じゃんけんの結果】\nあなたの選択: {choice}\nボットの選択: {bot_choice}\n{result}")

async def setup(bot):
    await bot.add_cog(Janken(bot))
