from typing import Final
import os
from discord.ext import commands
import discord
import logging
from dotenv import load_dotenv
import asyncio
from commands.help import Help

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await  bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded extension: {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

handler = handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# @bot.command
# async def joined(ctx, member: discord.Member):
#     await ctx.send( await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}'))

# bot.run(token=TOKEN, log_handler=handler)

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
# client.run()

