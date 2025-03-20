![A3SAT_Logo](https://github.com/user-attachments/assets/16a8b678-9d9b-48ba-ab5a-9edc6fa69599)

# A3SAT - Arma 3 Server Administration Tools (Alpha)
**Status**: Active Development 🟢

These tools are designed to streamline and enhance the management of your Windows Arma 3 Server, offering a range of features to simplify administrative tasks.

## Features 📋

- **Automated Mod Download and Update**: Simplify mod management by automatically downloading and updating required mods, ensuring both the server and connected clients have the necessary content.

- **HTML Modlist Import**: Enable the server to parse and import mod lists from `.html` files generated by the Arma 3 client, automating the process of identifying and downloading the correct mods.

- **Automatic `.bikey` Management and Symlink Generation**: Streamline the handling of `.bikey` files by automatically copying them to the appropriate directories. Additionally, create symlinks pointing to SteamCMD downloads (e.g., `107410/<modid>`), facilitating                                                               easy mod updates by maintaining consistent folder references.

- **Arma 3 Server as a Windows Service**: Utilize the Non-Sucking Service Manager (`NSSM.exe`) to run the Arma 3 server as a Windows service, ensuring automatic startup and recovery, thereby enhancing server reliability and uptime.

- **Headless-Client Setup**(HT): Sets up Headless-Client(s) for your server if you choose to do so.

- **Discord Bot Integration**: Manage your server remotely by starting, stopping, or restarting it directly through Discord commands

Collectively, these features provide a robust and user-friendly environment for efficient Arma 3 server administration.

## Planned Features 🚧 

- **Telegram & Slack Bot**
- **Automatic Mod Sorting**

## Dependencies 🔗

- **PowerShell**: Employed to Automate the Arma 3 Server setup.​
- **[NSSM](https://nssm.cc/download) (Non-Sucking Service Manager)**: A tool that allows you to run the Arma 3 server as a Windows service, ensuring it starts automatically and remains running, thereby enhancing server reliability.
- **[SteamCMD](https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip)**: The command-line version of Steam, used to install and update the Arma 3 server files, as well as manage Steam Workshop mods. 
- **[Python 3.x](https://www.python.org/downloads)** (Optional): Utilized for the Discord Bot.​

## Installation 🪛

- **
