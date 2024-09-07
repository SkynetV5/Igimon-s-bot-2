import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Ban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @app_commands.command(name="ban",description="Banuje danego użytkownika z serwera")
    async def kick_command(self,interaction: discord.Integration, user: discord.User, reason: Optional[str]=None):
        try:
            if not interaction.user.guild_permissions.ban_members:
                await interaction.response.send_message("Nie masz uprawnień do banowania użytkowników!", ephemeral=True)
                return
        
            await user.ban(reason=reason)

            await interaction.response.send_message(f"{user.mention} został zbanowany. Powód: {reason if reason else 'Brak powodu.'}", ephemeral=True)

            if not user.bot:
                await user.send(f"Zostałeś zbanowany na serwerze {interaction.guild.name}. Powód: {reason if reason else 'Brak powodu.'}")

        except discord.Forbidden:
            await interaction.response.send_message("Nie mogę zbanować tego użytkownika. Upewnij się, że moja rola jest wyżej w hierarchii niż rola tego użytkownika.", ephemeral=True)

        except Exception as e:
            await interaction.response.send_message(f"Wystąpił błąd: {str(e)}", ephemeral=True)


async def setup(bot):
    print("Ładowanie Coga: Ban")
    await bot.add_cog(Ban(bot))