# Discord Service Manager Bot

This Discord bot provides convenient slash commands (`/start`, `/stop`, `/restart`) to control the "Arma3Server" service on Windows servers. It is built with Python using the `discord.py` library.


## Features

- **Slash Commands**: Easy and intuitive commands within Discord.
- **Service Management**: Start, stop, and restart the Windows "Arma3Server" service.
- **Authorization**: Commands are restricted to specified Discord user IDs for security.
- **Service State Check**: Checks the current state before performing operations, avoiding unnecessary errors.

## Requirements

- Python 3.8+
- Windows OS (the bot controls Windows services)
- `discord.py` library (`pip install -U discord.py`)
- Discord Bot Token
- Administrative privileges on the host machine to manage Windows services


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```


### 2. Install Dependencies

```bash
pip install -U discord.py
```

### 3. Configure Bot

Open `A3DSR.py` and replace:

- `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token.
- `AUTHORIZED_USER_IDS` with your Discord user IDs allowed to use the bot.
- `guild = discord.Object(id=485519731034423318)` with your Discord guild (server) ID.

Example:
```python
BOT_TOKEN = "your-real-token-here"
AUTHORIZED_USER_IDS = [123456789012345678]
```


## Usage

### Run the Bot

Make sure to run the bot with administrative privileges, as it needs them to control services.

```bash
python A3DSR.py
```

The bot will log into Discord and sync slash commands automatically.


### Discord Commands

- `/start` - Starts the "Arma3Server" service if it's not already running.
- `/stop` - Stops the "Arma3Server" service if it's running.
- `/restart` - Restarts the "Arma3Server" service (gracefully handling current state).

Only users listed in `AUTHORIZED_USER_IDS` can execute these commands.


## Security and Best Practices

- **Token Security**: Keep your Discord bot token private. If exposed, regenerate it immediately.
- **Limited Access**: Add only trusted user IDs to the authorized list.
- **Admin Privileges**: Run the bot on a secure, monitored system, as it requires admin rights.


## Troubleshooting

- Ensure the bot has the `applications.commands` and `bot` permissions in Discord.
- Verify the bot is correctly invited to your Discord server.
- Confirm the bot is run with administrative privileges on your system.
- Check the console logs for error messages if commands do not respond as expected.


## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


