import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Mute(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="mute",description="Wycisza danego użytkownika")
    async def mute_command(self, interaction: discord.Integration, user: discord.User, reason: Optional[str]=None):
        try:
            mute_role = discord.utils.get(interaction.guild.roles, name="Muted")
            if not mute_role:
                mute_permisions = discord.Permissions(send_messages=False, speak=False, connect=True, view_channel=True)
                color = discord.Color(0x000000)
                bot_role = discord.utils.get(interaction.guild.roles, name="Igimon's Bot 2")
                mute_role = await interaction.guild.create_role(name="Muted", permissions=mute_permisions,color=color)
                if bot_role:
                    await mute_role.edit(position=bot_role.position - 1)
            
            if mute_role in user.roles:
                await interaction.response.send_message(f"{user.mention} jest już wyciszony.", ephemeral=True)
                return

            await user.add_roles(mute_role,reason=reason)
            await user.send(f"Zostałeś wyciszony. Powód: {reason if reason else 'Brak powodu'}")
            await interaction.response.send_message(f"{user.mention} został wyciszony. Powód: {reason if reason else 'Brak powodu'}", ephemeral=True)

            
        except Exception as e:
            print(e)

async def setup(bot):
    print("Ładowanie Coga: Mute")
    await bot.add_cog(Mute(bot))