import discord
from discord.ext import commands



class Poke(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="poke")
    async def poke_command(self,ctx, member: discord.Member = None):
        try:
            if member is not None:
                await ctx.send(f"Hey {member.mention}!")
        except Exception as e:
            await ctx.send("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.")



async def setup(bot):
    print("Ładowanie Coga: Poke")
    await bot.add_cog(Poke(bot))
