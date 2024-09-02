import discord

class RoleAssigment(discord.ui.View):
    def __init__(self,roles,roles_not_to_choose):
        super().__init__()
        self.roles = roles
        for role in roles:
            if role.name not in roles_not_to_choose:
                self.add_item(RoleButton(role))

class RoleButton(discord.ui.Button):
    def __init__(self, role):
        super().__init__(label=role.name,style=discord.ButtonStyle.primary)
        self.role = role

    async def callback(self, interaction: discord.Integration):
        user = interaction.user
        if self.role in user.roles:
            try:
                await user.remove_roles(self.role)
                await interaction.response.send_message(f"Removed role {self.role.name}", ephemeral=True)
            except discord.Forbidden:
                await interaction.response.send_message("I don't have permission to remove that role.", ephemeral=True)
            except discord.HTTPException as e:
                await interaction.response.send_message(f"Failed to remove role due to: {e}", ephemeral=True)
        else:
            try:
                await user.add_roles(self.role)
                await interaction.response.send_message(f"Added role {self.role.name}", ephemeral=True)
            except discord.Forbidden:
                await interaction.response.send_message("I don't have permission to add that role.", ephemeral=True)
            except discord.HTTPException as e:
                await interaction.response.send_message(f"Failed to add role due to: {e}", ephemeral=True)