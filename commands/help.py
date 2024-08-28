import discord
from discord import app_commands
from discord.ext import commands
from features.random_color_embed import RandomColorHex

help_commands = {
    '/helps' : 'Wyświetla okno pomocy.',
    '/avatar': 'Wyświetla avatar użytkownika (bez oznaczenia użytkownika - wyświetli avatar użytkownika wpisującej komende)',
    '/kiss': 'Całuje danego użytkownika',
    '/poke': 'Zaczepia gracza'
}


class Help(commands.Cog) :
    def __init__(self,bot):
        self.bot = bot
    @app_commands.command(name="helps", description="Wyświetla okno pomocy.")
    async def help_command(self,interaction: discord.Integration):
        user = interaction.user
        try:
            random_color = RandomColorHex().random_color_hex()
            embed = discord.Embed(title="Pomoc - Lista Komend", description="Oto dostępne komendy:", colour=random_color)
            for command, description in help_commands.items():
                embed.add_field(name=command, value=description, inline=False)
            

            await interaction.response.send_message(embed=embed,ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.", ephemeral=True)


    
async def setup(bot):
    print("Ładowanie Coga: Help")
    await bot.add_cog(Help(bot))

