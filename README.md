# Twitch-Speedrunner-Bot
A basic bot for Twitch with speedrunner-specific functionality.

## Index
1. [What Can This Bot Do?](#what-can-this-bot-do)
2. [Bot Commands](#bot-commands)
3. [How to Use the Bot](#how-to-use-the-bot)

## What Can This Bot Do?
- Create a [multitwitch.tv](http://multitwitch.tv/) race link with you and other speedrunners (if you are currently racing)
- Tell a user the world record for the game & category you are running
- Tell a user your personal best time for the game & category you are running
- Tell a user the stream uptime
- Tell a user how long they have been following you
- Add/delete basic text commands via Twitch chat

## Bot Commands
- `!wr`
    - Returns the world record (time and runner) for the game & category specified in your stream title.
- `!pb`
    - Returns your personal best (time and leaderboard standing) for the game & category specified in your stream title.
- `!race`
    - Creates a [multitwitch.tv](http://multitwitch.tv/) link with you and your opponents' streams (if you are currently racing).
- `!uptime`
    - Returns the duration the stream has been live for.
- `!followage [optional_user]`
    - Returns the amount of time the user has been following the channel owner. If the optional argument is specified, it will return the follow age for that user instead.
- `!add <command_name> <command_text>`
    - Adds a simple text command to the commands file. Command names are case sensitive.
- `!delete <command_name>`
    - Deletes the specified command from the commands file. Command names are case sensitive.
- `!commands`
    - Returns a list of bot commands.
    
## How to Use the Bot
1. Install the latest version of Python 3 ([here](https://www.python.org/downloads/))
2. Using **pip**, install the Python package *pytz*: `pip install pytz` or read more [here](https://pypi.org/project/pytz/)
3. In the *settings.py* file, enter the required information in the following fields:
    - **PASS**: *the oauth token for the Twitch account that will be controlled by the bot — get one [here](https://twitchapps.com/tmi/) while logged into the bot's Twitch account*
    - **IDENT**: *the username of the Twitch account that will be controlled by the bot*
    - **CHANNEL**: *the channel owner's Twitch username*
    - **CHANNELPASS**: *the oauth token for the channel owner's Twitch account — get one [here](https://twitchapps.com/tmi/) while logged into the channel owner's Twitch account*
    - **GAMES**: *Add, as a Python list, the game(s) you speedrun to this list. If you only speedrun one game, it should be a list with only one list inside. For each game's list, the first element should be the name of the game exactly how you'd type it in your stream title. The second element should be the code for the game that Speedrun.com uses in the hyperlink for that game's page. For example, Banjo-Tooie is 'bt'*
    - **CATEGORIES**: *Add, as a Python list, the categorie(s) of all the games you speedrun to this list. If you only run one category, it should be a list with only one list inside. For each category's list, the first element should be the name of the category exactly how you'd type it in your stream title. The second element should be the code for that category that Speedrun.com uses in the hyperlinks for that category. For example, Any% is usually 'Any' and 100% is usually '100'*
