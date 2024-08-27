import discord
from discord.ext import commands
from features.random_color_embed import RandomColorHex

class Avatar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar_command(self,ctx,member: discord.Member = None):
        try:
            if member is None:
                member = ctx.author
            random_color = RandomColorHex().random_color_hex()
            embed = discord.Embed(title=f"Avatar użytkownika {member.display_name}", color=random_color)
            embed.set_image(url=member.avatar)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Wystąpił Błąd. Nie mogłem wysłać prywatnej wiadomości. Sprawdź, czy masz otwarte DM z botem.")

async def setup(bot):
    print("Ładowanie Coga: Avatar")
    await bot.add_cog(Avatar(bot))
