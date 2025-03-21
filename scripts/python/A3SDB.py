import discord
from discord import app_commands
import subprocess

# Your bot token (keep it secret, regenerate if exposed)
BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# List of Discord user IDs who are allowed to run commands (as integers)
AUTHORIZED_USER_IDS = [YOUR_USER_ID]

# Your Discord Guild ID (Your Discord Server ID)
GUILD_ID = "YOUR_GUILD_ID"

#The Windows Service running your Arma 3 Server
SERVICE_NAME = "Arma3Server"

# Helper function to query service state
def get_service_state(service_name: str) -> str:
    try:
        result = subprocess.run(["sc", "query", service_name], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return ""

# Create a subclass of discord.Client
class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands to the specific guild so they appear instantly
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f"Slash commands synced to guild {guild.id}.")

client = MyClient()

# Authorization helper
def is_authorized(interaction: discord.Interaction) -> bool:
    return interaction.user.id in AUTHORIZED_USER_IDS

# /start command: Only start if the service isn't running already.
@client.tree.command(name="start", description="Starts the Arma3Server service")
async def start(interaction: discord.Interaction):
    if not is_authorized(interaction):
        await interaction.response.send_message("You are not authorized to execute this command.", ephemeral=True)
        return

    state = get_service_state("Arma3Server")
    if "RUNNING" in state:
        await interaction.response.send_message("Service 'Arma3Server' is already running!")
        return

    try:
        subprocess.run(["sc", "start", "Arma3Server"], check=True)
        await interaction.response.send_message("Your request has been processed: Service 'Arma3Server' started successfully!")
    except Exception as e:
        await interaction.response.send_message(f"Failed to start service 'Arma3Server': {e}")

# /stop command: Only stop if the service is running.
@client.tree.command(name="stop", description="Stops the Arma3Server service")
async def stop(interaction: discord.Interaction):
    if not is_authorized(interaction):
        await interaction.response.send_message("You are not authorized to execute this command.", ephemeral=True)
        return

    state = get_service_state("Arma3Server")
    if "STOPPED" in state or "STOP_PENDING" in state or "not running" in state.lower():
        await interaction.response.send_message("Service 'Arma3Server' is already stopped!")
        return

    try:
        subprocess.run(["sc", "stop", "Arma3Server"], check=True)
        await interaction.response.send_message("Your request has been processed: Service 'Arma3Server' stopped successfully!")
    except Exception as e:
        await interaction.response.send_message(f"Failed to stop service 'Arma3Server': {e}")

# /restart command: Check state, stop only if running, then start.
@client.tree.command(name="restart", description="Restarts the Arma3Server service")
async def restart(interaction: discord.Interaction):
    if not is_authorized(interaction):
        await interaction.response.send_message("You are not authorized to execute this command.", ephemeral=True)
        return

    state = get_service_state("Arma3Server")
    if "RUNNING" in state:
        try:
            subprocess.run(["sc", "stop", "Arma3Server"], check=True)
        except subprocess.CalledProcessError as e:
            # If stopping fails due to already being stopped, ignore it.
            if "1062" not in str(e):
                await interaction.response.send_message(f"Failed to stop service 'Arma3Server': {e}")
                return

    try:
        subprocess.run(["sc", "start", "Arma3Server"], check=True)
        await interaction.response.send_message("Your request has been processed: Service 'Arma3Server' restarted successfully!")
    except Exception as e:
        await interaction.response.send_message(f"Failed to restart service 'Arma3Server': {e}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("Type /start, /stop, or /restart in your server to control the Arma3Server service.")

client.run(BOT_TOKEN)
