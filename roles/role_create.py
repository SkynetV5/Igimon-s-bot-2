import discord
from discord.ext import commands

class CreateRole:
    def __init__(self, name: str, color: discord.Color, permissions: discord.Permissions):
        self.name = name
        self.color = color
        self.permisions = permissions
        
    async def create_role(self,guild):
        role = discord.utils.get(guild.roles, name=self.name)
        if not role:
            role = await guild.create_role(name=self.name,color=self.color,permissions=self.permisions)
            
        return role

    async def create_role_by_integration(self, interaction: discord.Integration):
        role = discord.utils.get(interaction.guild.roles, name=self.name)
        if not role:
            role = await interaction.guild.create_role_by_integration(name=self.name,color=self.color,permissions=self.permisions)
            
        return role
    

        

    