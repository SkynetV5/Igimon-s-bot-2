import discord
from discord.ext import commands

class CreateRole:
    def __init__(self, name: str, color: discord.Color, permissions: discord.Permissions):
        self.name = name
        self.color = color
        self.permisions = permissions

    async def create_role(self, interaction: discord.Integration):
        role =  discord.utils.get(interaction.guild.roles, name=self.name)
        if not role:
            role = await interaction.guild.create_role(name=self.name,color=self.color,permissions=self.permisions)
            
        return role

        

    