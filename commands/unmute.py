import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
from roles.role_create import CreateRole

class Unmute(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="unmute", description="Odcisza danego użytkownika")
    async def unmute_command(self, interaction: discord.Integration, user: discord.User, reason: Optional[str]=None):
        try:
            mute_role = discord.utils.get(interaction.guild.roles,name="Muted")
            if not mute_role:
                    mute_permisions = discord.Permissions(send_messages=False, speak=False, connect=True, view_channel=True)
                    color = discord.Color(0x000000)
                    bot_role = discord.utils.get(interaction.guild.roles, name="Igimon's Bot 2")
                    mute_role_create = CreateRole(name="Muted",color=color,permissions=mute_permisions) 
                    mute_role = await mute_role_create.create_role(interaction)
                    
                    if bot_role:
                        await mute_role.edit(position=bot_role.position - 1)

            if mute_role not in user.roles:
                await interaction.response.send_message(f"{user.mention} jest już odciszony.", ephemeral=True)
                return
            
            await user.remove_roles(mute_role)
            if not user.bot:
                await interaction.response.send_message(f"{user.mention} został odciszony.", ephemeral=True)
            else:
                await interaction.response.send_message("Bot został odciszony.", ephemeral=True)
            

        except Exception as e:
            await interaction.response.send_message(f"Błąd {e}", ephemeral=True)

async def setup(bot):
    print("Ładowanie Coga: Unmute")
    await bot.add_cog(Unmute(bot))