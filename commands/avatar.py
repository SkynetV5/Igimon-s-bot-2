import discord
from discord.ext import commands
from discord import app_commands
from features.random_color_embed import RandomColorHex

class Avatar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="avatar", description='Wyświetla avatar użytkownika (bez oznaczenia - wyświetli avatar użytkownika wpisującej komende)')
    async def avatar_command(self,interaction: discord.Integration,user: discord.User = None):
        try:
            if user is None:
                user = interaction.user
            random_color = RandomColorHex().random_color_hex()
            embed = discord.Embed(title=f"Avatar użytkownika {user.display_name}", color=random_color)
            embed.set_image(url=user.avatar)

            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.", ephemeral=True)

async def setup(bot):
    print("Ładowanie Coga: Avatar")
    await bot.add_cog(Avatar(bot))
