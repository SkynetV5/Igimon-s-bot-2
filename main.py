from typing import Final
import os
import discord
import logging
from discord.ext import commands
from discord import app_commands
from messages_to_channel.role_message import role_messages
from messages_to_channel.rules_message import rules_message
from dotenv import load_dotenv
import asyncio
import json

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CONFIG_JSON = 'config.json'

class IgmionsBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True 
        intents.members = True
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
        with open(CONFIG_JSON, 'r') as file:
            return json.load(file)

    def _save_config(self,config):
        with open(CONFIG_JSON, 'w') as file:
             json.dump(config,file,indent=4)
    async def on_ready(self):
        try:
            print(f'We have logged in as {self.user}')
            
            config = self._load_config()

            if config.get("MESSAGE_ROLE_SEND") == False:
                channel_name = "role-roles"

                channel = discord.utils.get(self.get_all_channels(), name=channel_name)
                guild = discord.utils.get(self.guilds)
                if not channel:
                    channel = await guild.create_text_channel(name=channel_name)

                if channel:
                    guild = channel.guild
                    embed, view = role_messages(guild)
                    await channel.send(embed=embed, view=view)
                    config['MESSAGE_ROLE_SEND'] = True
                    self._save_config(config)


            if config.get("MESSAGE_RULES_SEND") == False:
                channel_name = 'regulamin-rules'

                channel = discord.utils.get(self.get_all_channels(),name = channel_name)

                if not channel:
                    channel = await guild.create_text_channel(name=channel_name)
                
                if channel:
                    embed = rules_message()
                    await channel.send(embed=embed)
                    config['MESSAGE_RULES_SEND'] = True
                    self._save_config(config)
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

