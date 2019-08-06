import string
import time
import datetime
import pytz
from pytz import timezone
import random
import urllib.request
from urllib.request import urlopen
from json import loads
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import getUser, getMessage
from Settings import CHANNEL, COOLDOWN, IDENT, CHANNELPASS, SRC_USERNAME, GAMES, CATEGORIES


#Basic command function
def basicCommand(input, output):
    if input == message.strip():
        sendMessage(s, output)
        cooldown()


#Adds a text command to commands.txt
def addCommand(input):
    if input == message.lower().split()[0] and (user == CHANNEL or user in moderators) and user != IDENT:
        a = open("commands.txt", "r")
        commandList = a.readlines()
        commandNames = []
        for line in commandList:
            commandNames.append(line.split()[0].lower().strip(";"))
        a.close()
        writeCommand = open("commands.txt", "a")
        commandMessage = message
        command = commandMessage.split(input, 1)[-1].strip()
        try:
            if command[0] == "!" and command.split()[0] not in commandNames:
                writeCommand.write(command.split()[0] + "; " + command.split(' ', 1)[1] + "\n")
                sendMessage(s, "Command " + command.split()[0] + " successfully added.")
                writeCommand.close()
                cooldown()
            elif command.split()[0] in commandNames:
                sendMessage(s, "Error: Command " + command.split()[0] + " already exists")
                cooldown()
                return
            else:
                sendMessage(s, "Error: Invalid syntax for the !add command. Correct syntax is: !add <command_name> <command_text>")
                cooldown()
        except IndexError as err:
            sendMessage(s, "Error: Invalid syntax for the !add command. Correct syntax is: !add <command_name> <command_text>")
            cooldown()
    elif input == message.lower().split()[0]:
        sendMessage(s, "@" + user.title() + " Only the channel owner and moderators may use the !add command.")
        cooldown()


#Deletes a specified command from commands.txt
def deleteCommand(input):
    if input == message.lower().split()[0] and user == CHANNEL:
        a = open("commands.txt", "r")
        commandList = a.readlines()
        commandNames = []
        for line in commandList:
            commandNames.append(line.split()[0].lower().strip(";"))
        a.close()

        try:
            command = message.split()[1].strip().lower()
        except IndexError as err:
            sendMessage(s, "Error: Invalid syntax for the !delete command. Correct syntax is: !delete <command_name>")
            cooldown()
            return

        try:
            message.split()[2]
            if message.split()[2]:
                sendMessage(s, "Error: Invalid syntax for the !delete command. Correct syntax is: !delete <command_name>")
                cooldown()
                return
        except IndexError as err:
            pass

        if command in commandNames:
            for commandLine in commandList:
                if command == commandLine.split()[0].lower().strip(";"):
                    commandList.remove(commandLine)
            overwriteCommand = open("commands.txt", "w")
            overwriteCommand.writelines(commandList)
            overwriteCommand.close()
            sendMessage(s, "Command {} successfully deleted.".format(command))
            cooldown()
        else:
            sendMessage(s, "Error: Command {} not found".format(command))
            cooldown()

    elif input in message:
        sendMessage(s, "@" + user.title() + " Only the channel owner may use the !delete command.")
        cooldown()


#Tells user how long they've been following the channel
def followAge(input):
    if input == message.lower().split()[0]:
        messageSplit = message.lower().split()
        try:
            messageSplit[1]
        except IndexError as err:
            follower = user
        else:
            follower = messageSplit[1]

        response = urlopen('http://api.newtimenow.com/follow-length/?channel={}&user={}'.format(CHANNEL, follower))
        readable = response.read().decode('utf-8')
        now = datetime.datetime.now()
        try:
            date = datetime.datetime.strptime(readable.split()[0], '%Y-%m-%d')
        except ValueError as err:
            sendMessage(s, follower.title() + " is not following " + CHANNEL.title() + ".")
            return

        age = now - date
        age = str(age)
        age_in_days = int(age.split()[0])
        years = divmod(age_in_days, 365)
        months = divmod(years[1], 30)
        days = months[1]
        if years[0] > 0:
            sendMessage(s, follower.title() + " has been following " + CHANNEL.title() + " for " + str(years[0]) + " years, " + str(months[0]) + " months, " + str(days) + " days.")
        elif months[0] > 0:
            sendMessage(s, follower.title() + " has been following " + CHANNEL.title() + " for " + str(months[0]) + " months, " + str(days) + " days.")
        else:
            sendMessage(s, follower.title() + " has been following " + CHANNEL.title() + " for " + str(days) + " days.")

        cooldown()


#Returns the stream uptime
def upTime(input):
    if input == message.lower().strip():
        #Get the uptime from the Twitch API
        response = urlopen('https://api.twitch.tv/kraken/streams/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        readable = response.read().decode('utf-8')
        stream_info = loads(readable)
        stream = stream_info["stream"]

        if stream == None:
            sendMessage(s, CHANNEL.title() + " is not live.")
            cooldown()
            return
        elif stream != None:
            pass

        createdAt = datetime.datetime.strptime(stream["created_at"][11:19], '%H:%M:%S').time()
        now = datetime.datetime.now().time()
        dateTimeCreatedAt = datetime.datetime.combine(datetime.date.today(), createdAt)
        dateTimeCreatedAtUTC = timezone('UTC').localize(dateTimeCreatedAt)
        dateTimeNow = datetime.datetime.combine(datetime.date.today(), now)
        dateTimeNowEST = timezone('US/Eastern').localize(dateTimeNow)
        dateTimeUptime = dateTimeNowEST - dateTimeCreatedAtUTC

        uptime_hours = str(int(str(dateTimeUptime).split(':')[0]))
        uptime_min = str(int(str(dateTimeUptime).split(':')[1]))

        if int(uptime_hours) == 0:
            sendMessage(s, CHANNEL.title() + " has been live for " + uptime_min + " minutes.")
            cooldown()
            return
        elif int(uptime_hours) > 0:
            sendMessage(s, CHANNEL.title() + " has been live for " + uptime_hours + " hours, " + uptime_min + " minutes.")
            cooldown()
            return


#Returns the world record for the category that's written in the stream title
def worldRecord(input):
    if input == message.lower().strip():
        #Get the stream title from the Twitch API
        response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        readable = response.read().decode('utf-8')
        lst = loads(readable)
        title = lst['status'].lower()
        game = None

        for i in range(len(GAMES)):
            if GAMES[i][0].lower() in title:
                game = GAMES[i][1]
                break

        category = None
        category_title = None
        for i in range(len(CATEGORIES)):
            if CATEGORIES[i][0].lower() in title:
                category = CATEGORIES[i][1]
                category_title = CATEGORIES[i][0]
                break

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?top=1&embed=players'.format(game, category))
            readable = response.read().decode('utf-8')
            lst = loads(readable)
            runner = lst['data']['players']['data'][0]['names']['international']
            time_in_sec = int(lst['data']['runs'][0]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            wr = ''
            if hours[0] > 0:
                wr = str(hours[0]) + " hours " + str(minutes[0]) + " min " + str(seconds) + " sec "
            elif minutes[0] > 0:
                wr = str(minutes[0]) + " min " + str(seconds) + " sec "
            else:
                wr = str(seconds) + " sec "

            sendMessage(s, "The " + category_title + " world record is " + wr + "by " + runner + ".")
            cooldown()

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return


#Returns the channel owner's personal best time for the category that's written in the stream title
def personalBest(input):
    if input == message.lower().strip():
        #Get the stream title from the Twitch API
        response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        readable = response.read().decode('utf-8')
        lst = loads(readable)
        title = lst['status'].lower()
        game = None

        for i in range(len(GAMES)):
            if GAMES[i][0].lower() in title:
                game = GAMES[i][1]
                break

        category = None
        category_title = None
        for i in range(len(CATEGORIES)):
            if CATEGORIES[i][0].lower() in title:
                category = CATEGORIES[i][1]
                category_title = CATEGORIES[i][0]
                break

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?embed=players'.format(game, category))
            readable = response.read().decode('utf-8')
            lst = loads(readable)

            place = 0
            for name in lst['data']['players']['data']:
                place = place + 1
                try:
                    name['names']
                except KeyError as err:
                    continue
                if name['names']['international'].lower() == SRC_USERNAME:
                    break

            if place > len(lst['data']['players']['data']):
                sendMessage(s, CHANNEL.title() + " currently has no " + category_title + " PB on the leaderboard.")
                cooldown()
                return

            time_in_sec = int(lst['data']['runs'][place - 1]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            pb = ''
            if hours[0] > 0:
                pb = str(hours[0]) + " hours " + str(minutes[0]) + " min " + str(seconds) + " sec"
            elif minutes[0] > 0:
                pb = str(minutes[0]) + " min " + str(seconds) + " sec"
            else:
                pb = str(seconds) + " sec"

            sendMessage(s, CHANNEL.title() + "\'s " + category_title + " PB is " + pb + ".")
            cooldown()

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return


#Returns a multitwitch.tv link with the channel owner and the other racers if a race is happening
def raceCommand(input):
    if input == message.lower().strip():
        #Get the stream title from the Twitch API
        response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        readable = response.read().decode('utf-8')
        lst = loads(readable)
        title = lst['status'].lower()

        if 'race with' in title:
            pass
        elif 'race with' not in title:
            sendMessage(s, CHANNEL.title() + " is not currently racing or no racers detected in stream title.")
            cooldown()
            return

        title_list = title.split()
        r = title_list.index('with') + 1
        contenders = []
        length = len(title_list)
        diff = length - r
        while True:
            contenders.append(title_list[r].strip(','))
            diff = diff - 1
            r = r + 1
            if diff == 0:
                break


        sendMessage(s, "Race link: multitwitch.tv/" + CHANNEL + "/" + "/".join(contenders))
        cooldown()


#Displays commands
def getCommands(input):
    if input == message.strip().lower():
        sendMessage(s, '!followage • !uptime • !wr • !pb • !race • '+' • '.join(listCommand))
        cooldown()


#Global cooldown
def cooldown():
    if user == CHANNEL:
        pass
    elif user:
        abort_after = COOLDOWN
        start = time.time()
        while True:
            delta = time.time() - start
            if delta >= abort_after:
                break


#Checks to see if a message is from Twitch or a user
def Console(line):
    if "PRIVMSG" in line:
        return False
    else:
        return True


#Quits the bot program
def quitCommand(input):
    if input == message.strip().lower() and user == CHANNEL:
        sendMessage(s, "/me has been disconnected.")
        quit()
    elif input == message.strip():
        sendMessage(s, "@" + user.title() + " Only the channel owner may use the !kill command.")
        cooldown()


s = openSocket()
joinRoom(s)
readbuffer = ""

#Loop that keeps the chat active
while True:

    discordTimer(time.time())
    pointTimer(time.time())

    readbuffer = s.recv(1024)
    readbuffer = readbuffer.decode()
    temp = readbuffer.split("\n")
    readbuffer = readbuffer.encode()
    readbuffer = temp.pop()


    for line in temp:
        print(line)
        #Prevents afk kick from Twitch server
        if "PING" in line and Console(line):
            msgg = "PONG tmi.twitch.tv\r\n".encode()
            s.send(msgg)
            print(msgg)
            break
        #Prints chat lines (in the console) in a more readable fashion
        user = getUser(line)
        message = getMessage(line)
        print(user + " said: " + message)

        #List of chatters, moderators and VIPs
        response = urlopen('https://tmi.twitch.tv/group/user/{}/chatters'.format(CHANNEL))
        readable = response.read().decode('utf-8')
        chatlist = loads(readable)
        chatters = chatlist['chatters']
        moderators = chatters['moderators']
        vips = chatters['vips']
        viewers = chatters['viewers']

        #Makes dictionary of commands from commands.txt
        commands = {}
        listCommand = []
        commandFile = open("commands.txt", "r")
        commandList = commandFile.readlines()
        commandFile.close()
        for command in commandList:
            try:
                commandInput, commandOutput = command.split(";")
                commands[commandInput] = commandOutput
            except ValueError as err:
                sendMessage(s, "Error: Invalid command in commands file")
                cooldown()

        #Loops commands dictionary through basicCommand function and creates a list of commands
        for input, output in commands.items():
            basicCommand(input, output)
            listCommand.append(input)


        #Add command functions below
        getCommands('!commands')
        addCommand('!add')
        deleteCommand('!delete')
        worldRecord('!wr')
        personalBest('!pb')
        raceCommand('!race')
        upTime('!uptime')
        followAge('!followage')
        quitCommand('!kill')
        continue
