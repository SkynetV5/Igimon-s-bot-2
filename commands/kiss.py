import discord
from discord.ext import commands
from discord import app_commands
from features.random_color_embed import RandomColorHex
import math
from random import randint

class Kiss(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @app_commands.command(name="kiss", description='Całuje danego użytkownika')
    async def kiss_command(self,interaction: discord.Integration ,user: discord.User = None):
        kiss_list = ['całuje ', 'namiętnie całuje', 'nie odwzajemnia twojego całusa']
        random_number = randint(0,len(kiss_list))
        await interaction.response.send_message(f"{interaction.user.display_name} {kiss_list[random_number]} {user.mention}")

    
async def setup(bot):
    print("Ładowanie Coga: Kiss")
    await bot.add_cog(Kiss(bot))