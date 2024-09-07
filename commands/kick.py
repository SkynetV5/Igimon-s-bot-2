import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Kick(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="kick",description="Wyrzuca danego użytkownika z serwera")
    async def kick_command(self,interaction: discord.Integration, user: discord.User, reason: Optional[str]=None):
        try:
            if not interaction.user.guild_permissions.kick_members:
                await interaction.response.send_message("Nie masz uprawnień do wyrzucania użytkowników!", ephemeral=True)
                return
        
            await user.kick(reason=reason)

            await interaction.response.send_message(f"{user.mention} został wyrzucony. Powód: {reason if reason else 'Brak powodu.'}", ephemeral=True)

            if not user.bot:
                await user.send(f"Zostałeś wyrzucony z serwera {interaction.guild.name}. Powód: {reason if reason else 'Brak powodu.'}")

        except discord.Forbidden:
            await interaction.response.send_message("Nie mogę wyrzucić tego użytkownika. Upewnij się, że moja rola jest wyżej w hierarchii niż rola tego użytkownika.", ephemeral=True)

        except Exception as e:
            await interaction.response.send_message(f"Wystąpił błąd: {str(e)}", ephemeral=True)


async def setup(bot):
    print("Ładowanie Coga: Kick")
    await bot.add_cog(Kick(bot))