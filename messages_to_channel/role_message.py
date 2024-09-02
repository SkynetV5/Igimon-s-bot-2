import discord
from features.assigment_role_to_user import RoleAssigment


def role_messages(guild):
    roles = guild.roles
    embed = discord.Embed(title="Roles", description="Choose Your Roles.", colour=0x000000)
    roles_not_to_choose = ['Admin', '@everyone']
    for role in roles:
        if role.name not in roles_not_to_choose:
            embed.add_field(name=role.name, value='\u200b', inline=False)
    view = RoleAssigment(roles,roles_not_to_choose)
    return embed,view