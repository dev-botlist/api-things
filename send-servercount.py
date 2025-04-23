import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
import asyncio

class SendCount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="send-count", description="Sends the server count to the API")
    @app_commands.checks.has_permissions(administrator=True)
    async def send_count(self, interaction: discord.Interaction):
        server_count = len(self.bot.guilds)
        bot_id = "<YOUR_BOT_ID>"
        token = "<YOUR_API_TOKEN>"

        await interaction.response.defer(ephemeral=True)

        url = f"https://dev-botlist.com/api/{bot_id}/servercount"
        payload = {
            "token": token,
            "serverCount": server_count
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload) as resp:
                    if resp.status == 200:
                        await interaction.followup.send(
                            f"✅ Server count successfully updated: **{server_count}**",
                            ephemeral=True
                        )
                    else:
                        data = await resp.json()
                        message = data.get("message", "Unknown error")
                        await interaction.followup.send(
                            f"❌ Error while sending: {message}",
                            ephemeral=True
                        )
            except Exception as e:
                await interaction.followup.send(
                    f"❌ Exception occurred: {str(e)}",
                    ephemeral=True
                )

async def setup(bot):
    await bot.add_cog(SendCount(bot))
