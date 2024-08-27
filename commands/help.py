import discord
from discord.ext import commands
from features.random_color_embed import RandomColorHex

help_commands = {
    '!helps' : 'Wyświetla okno pomocy.',
    '!avatar': 'Wyświetla avatar użytkownika (bez oznaczenia użytkownika - wyświetli avatar osoby wpisującej komende)',
    '!kiss': 'Całuje danego użytkownika (!kiss osoba)',
    '!poke': 'Zaczepia gracza (!poke osoba)'
}


class Help(commands.Cog) :
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name="helps")
    async def help_command(self,ctx):
        user = ctx.message.author
        try:
            random_color = RandomColorHex().random_color_hex()
            embed = discord.Embed(title="Pomoc - Lista Komend", description="Oto dostępne komendy:", colour=random_color)
            for command, description in help_commands.items():
                embed.add_field(name=command, value=description, inline=False)
            

            await user.send(embed=embed)
        except Exception as e:
            await ctx.send("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.")


    
async def setup(bot):
    print("Ładowanie Coga: Help")
    await bot.add_cog(Help(bot))

