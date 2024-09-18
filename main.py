from typing import Final
import os
import discord
import logging
from discord.ext import commands
from discord import app_commands
from messages_to_channel.role_message import role_messages
from messages_to_channel.rules_message import rules_message
from roles.role_create import CreateRole
from features.random_color_embed import RandomColorHex
from dotenv import load_dotenv
import asyncio
import json

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CONFIG_JSON = 'config.json'
DEFAULT_CONFIG_JSON = {
    "MESSAGE_ROLE_SEND": False,
    "MESSAGE_RULES_SEND": False,
    "MESSAGE_ROLE_ID": 0,
    "MESSAGE_RULES_ID": 0
}

class IgmionsBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True 
        intents.members = True
        intents.reactions = True 
        super().__init__(command_prefix='!', intents=intents)
        

    async def _load_extensions(self):
        for filename in os.listdir('./commands'):
            if filename.endswith('.py') and filename != '__init__.py':
                try:
                    await self.load_extension(f'commands.{filename[:-3]}')
                    print(f'Loaded extension: {filename}')
                except Exception as e:
                    print(f'Failed to load extension {filename}: {e}')
    

    async def setup_hook(self):
        # Ładowanie rozszerzeń
        await self._load_extensions()
       
        # Synchronizacja komend
        try:
            synced_commands = await self.tree.sync()
            print(f'Synced {len(synced_commands)} commands')
        except Exception as e:
            print(f'Failed to sync commands: {e}')
        
    
    def _load_config(self):
        try:
            with open(CONFIG_JSON, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(CONFIG_JSON, 'w') as file:
                json.dump(DEFAULT_CONFIG_JSON,file,indent=4)
            with open(CONFIG_JSON, 'r') as file:
                return json.load(file)

    def _save_config(self,config):
        with open(CONFIG_JSON, 'w') as file:
             json.dump(config,file,indent=4)

    async def on_ready(self):
        try:
            print(f'We have logged in as {self.user}')
            
            config = self._load_config()

            channel_name = "role-roles"
            guild = discord.utils.get(self.guilds)
            channel = discord.utils.get(self.get_all_channels(), name=channel_name)
            embed_role, view_role = role_messages(guild)


            if config.get("MESSAGE_ROLE_SEND") == False:
                if not channel:
                    channel = await guild.create_text_channel(name=channel_name)

                if channel:
                    guild = channel.guild
                    message = await channel.send(embed=embed_role, view=view_role)
                    config['MESSAGE_ROLE_SEND'] = True
                    config['MESSAGE_ROLE_ID'] = message.id
                    self._save_config(config)
            else:
                message_id = config['MESSAGE_ROLE_ID']
                message = await channel.fetch_message(message_id)
                if message:
                    embed_role, view_role = role_messages(guild)
                    await message.edit(embed=embed_role, view=view_role)    
            
            if config.get("MESSAGE_RULES_SEND") == False:
                channel_name = 'regulamin-rules'

                channel = discord.utils.get(self.get_all_channels(),name = channel_name)

                if not channel:
                    channel = await guild.create_text_channel(name=channel_name)
                

                await channel.set_permissions(guild.default_role, read_messages=True, send_messages=False, view_channel=True)
    
                for ch in guild.channels:
                    if ch != channel:
                        await ch.set_permissions(guild.default_role, read_messages=False, view_channel=False)

                if channel:
                    embed = rules_message()
                    message = await channel.send(embed=embed)
                    await message.add_reaction("✅")
                    config['MESSAGE_RULES_SEND'] = True
                    config['MESSAGE_RULES_ID'] = message.id
                    self._save_config(config)
            else:
                message = await channel.fetch_message(message_id)
                if message:
                    embed = rules_message()
                    await message.edit(embed=embed)   

        except Exception as e:
            print(e)
            
    async def on_raw_reaction_add(self, payload):
        
        try:
            config = self._load_config()
            message_id = config.get("MESSAGE_RULES_ID")

            if payload.message_id != message_id:
                return 

            guild = self.get_guild(payload.guild_id)
            if not guild:
                return

            member = guild.get_member(payload.user_id)
            if not member:
                return

            if member.bot:
                return  # Ignoruj reakcje botów

            emoji = str(payload.emoji)
            if emoji == "✅":
                role = discord.utils.get(guild.roles, name="Member")

                if not role:
                    permissions = discord.Permissions(send_messages=True, speak=True, connect=True, view_channel=True)
                    random_color = RandomColorHex().random_color_hex()
                    color = discord.Color(random_color)
                    member_role_create = CreateRole(name="Member", color=color, permissions=permissions)
                    role = await member_role_create.create_role(guild)

                if role not in member.roles:
                    await member.add_roles(role)
        except Exception as e:
            print(e)

    async def _on_message(self, message: discord.Message):
        # Ignorowanie wiadomości wysłanych przez samego bota
        if message.author == self.user:
            return

    async def main(self):
        await self.start(TOKEN)

if __name__ == "__main__":

    bot = IgmionsBot()
    asyncio.run(bot.main())

