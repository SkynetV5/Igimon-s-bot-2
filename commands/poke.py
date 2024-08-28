import discord
from discord.ext import commands
from discord import app_commands



class Poke(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="poke" ,description='Zaczepia gracza')
    async def poke_command(self,interation: discord.Integration, user: discord.User = None):
        try:
            if user is not None:
                await interation.response.send_message(f"Hey {user.mention}!")
        except Exception as e:
            await interation.response.send_message("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.", ephemeral=True)



async def setup(bot):
    print("Ładowanie Coga: Poke")
    await bot.add_cog(Poke(bot))
