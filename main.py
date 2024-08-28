from typing import Final
import os
import discord
import logging
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

class IgmionsBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
        

    async def load_extensions(self):
        for filename in os.listdir('./commands'):
            if filename.endswith('.py') and filename != '__init__.py':
                try:
                    await self.load_extension(f'commands.{filename[:-3]}')
                    print(f'Loaded extension: {filename}')
                except Exception as e:
                    print(f'Failed to load extension {filename}: {e}')
    

    async def setup_hook(self):
        # Ładowanie rozszerzeń
        await self.load_extensions()
       
        # Synchronizacja komend
        try:
            synced_commands = await self.tree.sync()
            print(f'Synced {len(synced_commands)} commands')
        except Exception as e:
            print(f'Failed to sync commands: {e}')
        

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
    async def on_message(self, message: discord.Message):
        # Ignorowanie wiadomości wysłanych przez samego bota
        if message.author == self.user:
            return

    async def main(self):
        await self.start(TOKEN)

if __name__ == "__main__":

    bot = IgmionsBot()
    asyncio.run(bot.main())

