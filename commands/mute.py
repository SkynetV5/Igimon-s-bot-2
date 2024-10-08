import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
from roles.role_create import CreateRole

class Mute(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="mute",description="Wycisza danego użytkownika")
    async def mute_command(self, interaction: discord.Integration, user: discord.User, reason: Optional[str]=None):
        try:
            guild = interaction.guild
            mute_role = discord.utils.get(guild.roles, name="Muted")
            if not mute_role:
                    mute_permisions = discord.Permissions(send_messages=False, speak=False, connect=True, view_channel=True)
                    color = discord.Color(0x010101)
                    bot_role = discord.utils.get(guild.roles, name="Igimon's Bot 2")
                    mute_role_create = CreateRole(name="Muted",color=color,permissions=mute_permisions) 
                    mute_role = await mute_role_create.create_role_by_integration(interaction)
                    
                    if bot_role:
                        await mute_role.edit(position=bot_role.position - 1)

            if mute_role in user.roles:
                await interaction.response.send_message(f"{user.mention} jest już wyciszony.", ephemeral=True)
                return

            await user.add_roles(mute_role,reason=reason)
            if not user.bot:
                await user.send(f"Zostałeś wyciszony. Powód: {reason if reason else 'Brak powodu'}")
                await interaction.response.send_message(f"{user.mention} został wyciszony. Powód: {reason if reason else 'Brak powodu'}", ephemeral=True)
            else:
                await interaction.response.send_message(f" Bot został wyciszony. Powód: {reason if reason else 'Brak powodu'}", ephemeral=True)
            
        except Exception as e:
             await interaction.response.send_message(f"Błąd {e}", ephemeral=True)

async def setup(bot):
    print("Ładowanie Coga: Mute")
    await bot.add_cog(Mute(bot))