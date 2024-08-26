import discord
from discord.ext import commands
from features.random_color_embed import RandomColorHex

class Help(commands.Cog) :
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name="helps")
    async def help_command(self,ctx):
        user = ctx.message.author
        try:
            random_color = RandomColorHex().random_color_hex()
            print(random_color)
            embed = discord.Embed(title="Pomoc - Lista Komend", description="Oto dostępne komendy:", colour=random_color)
            embed.add_field(name="!helps", value="Wyświetla okno pomocy.", inline=False)

            await user.send(embed=embed)
        except:
            await ctx.send("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.")


    
async def setup(bot):
    print("Ładowanie Coga: Help")
    await bot.add_cog(Help(bot))

