# Twitch-Speedrunner-Bot
A basic bot for Twitch with speedrunner-specific functionality and Speedrun.com API integration, written in Python.

## Index
1. [What Can This Bot Do?](#what-can-this-bot-do)
2. [Bot Commands](#bot-commands)
3. [How to Use the Bot](#how-to-use-the-bot)

## What Can This Bot Do?
- Tell a user the world record for the game & category you are running
- Tell a user your personal best time for the game & category you are running
- Create a [multitwitch.tv](http://multitwitch.tv/) race link with you and other speedrunners (if you are currently racing)
- Tell a user the stream uptime
- Tell a user how long they have been following you
- Add/delete basic text commands via Twitch chat

## Bot Commands
- `!wr` (everyone)
    - Returns the world record (time and runner) for the game & category specified in your stream title. Data is taken from the [speedrun.com](https://www.speedrun.com/) API in realtime.
- `!pb` (everyone)
    - Returns your personal best (time and leaderboard standing) for the game & category specified in your stream title. Data is taken from the [speedrun.com](https://www.speedrun.com/) API in realtime.
- `!race` (everyone)
    - Creates a [multitwitch.tv](http://multitwitch.tv/) link with you and your opponents' streams (if you are currently racing).
- `!uptime` (everyone)
    - Returns the duration the stream has been live for. Data is taken from the Twitch API in realtime.
- `!followage [optional_user]` (everyone)
    - Returns the amount of time the user has been following the channel owner. If the optional argument is specified, it will return the follow age for that user instead. Data is taken from the [newtimenow.com](http://api.newtimenow.com/) API in realtime.
- `!add <command_name> <command_text>` (channel owner & moderators only)
    - Adds a simple text command to the commands file. Command names are case sensitive. Commands can also be added manually to the *commands.txt* file, following the semicolon-separated format shown in the sample command.
- `!delete <command_name>` (channel owner only)
    - Deletes the specified command from the commands file. Command names are case sensitive. Commands can also be deleted manually from the *commands.txt* file.
- `!commands` (everyone)
    - Returns a list of bot commands.
- `!kill` (channel owner only)
    - Quits the bot program.
    
## How to Use the Bot
#### After creating a separate Twitch account for the bot to control, follow these steps:
1. Install the latest version of Python 3 ([here](https://www.python.org/downloads/))
2. Using **pip**, install the Python package *pytz*: `pip install pytz` or read more [here](https://pypi.org/project/pytz/)
3. Download the contents of the [bot](/bot) folder to your comupter. In the *Settings.py* file, enter the required information in the following fields:
    - **PASS**: *the oauth token for the Twitch account that will be controlled by the bot — get one [here](https://twitchapps.com/tmi/) while logged into the bot's Twitch account*
    - **IDENT**: *the username of the Twitch account that will be controlled by the bot*
    - **CHANNEL**: *the channel owner's Twitch username*
    - **CHANNELPASS**: *the oauth token for the channel owner's Twitch account — get one [here](https://twitchapps.com/tmi/) while logged into the channel owner's Twitch account*
    - **GAMES**: *Add, as a Python list, the game(s) you speedrun to this list. If you only speedrun one game, it should be a list with only one list inside. For each game's list, the first element should be the name of the game exactly how you'd type it in your stream title. The second element should be the code for the game that Speedrun.com uses in the hyperlink for that game's page. For example, Banjo-Tooie is 'bt'*:
    ![game code example](images/game%20code.PNG)
    - **CATEGORIES**: *Add, as a Python list, the categorie(s) of all the games you speedrun to this list. If you only run one category, it should be a list with only one list inside. For each category's list, the first element should be the name of the category exactly how you'd type it in your stream title. The second element should be the code for that category that Speedrun.com uses in the hyperlinks for that category. For example, Any% is usually 'Any' and 100% is usually '100'*:
    ![category code example](images/category%20code.PNG)
4. Run the *Run.py* file, and the bot will join your channel via the Twitch account you created for it, ready to be used!
