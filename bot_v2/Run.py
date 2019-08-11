import string
import time
import urllib.request
from urllib.request import urlopen
from json import loads
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import getUser, getMessage
from Settings import CHANNEL, COOLDOWN, IDENT, CHANNELPASS, SRC_USERNAME, GAMES, CATEGORIES


#Returns the world record for the category that's written in the stream title
def worldRecord(input):
    if input == message.lower().strip():
        #Get the stream title from the Twitch API
        try:
            response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        except urllib.error.HTTPError as err:
            sendMessage(s, "Error: Invalid CHANNEL/CHANNELPASS in settings file")
            cooldown()
            return
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
        try:
            response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        except urllib.error.HTTPError as err:
            sendMessage(s, "Error: Invalid CHANNEL/CHANNELPASS in settings file")
            cooldown()
            return
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


#Returns a kadgar.net link with the channel owner and the other racers if a race is happening
def raceCommand(input):
    if input == message.lower().strip():
        #Get the stream title from the Twitch API
        try:
            response = urlopen('https://api.twitch.tv/kraken/channels/{}?oauth_token={}'.format(CHANNEL, CHANNELPASS.strip('oauth:')))
        except urllib.error.HTTPError as err:
            sendMessage(s, "Error: Invalid CHANNEL/CHANNELPASS in settings file")
            cooldown()
            return
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


        sendMessage(s, "Race link: http://kadgar.net/live" + CHANNEL + "/" + "/".join(contenders))
        cooldown()


#Displays commands
def getCommands(input):
    if input == message.strip().lower():
        sendMessage(s, 'Commands: !wr • !pb • !race')
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


#Checks if a message is from Twitch or a user
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

while True:

    readbuffer = s.recv(1024)
    readbuffer = readbuffer.decode()
    temp = readbuffer.split("\n")
    readbuffer = readbuffer.encode()
    readbuffer = temp.pop()


    for line in temp:
        print(line)
        if "PING" in line and Console(line):
            msgg = "PONG tmi.twitch.tv\r\n".encode()
            s.send(msgg)
            print(msgg)
            break
        user = getUser(line)
        message = getMessage(line)
        print(user + " said: " + message)

        response = urlopen('https://tmi.twitch.tv/group/user/{}/chatters'.format(CHANNEL))
        readable = response.read().decode('utf-8')
        chatlist = loads(readable)
        chatters = chatlist['chatters']
        moderators = chatters['moderators']
        vips = chatters['vips']
        viewers = chatters['viewers']


        getCommands('!commands')
        worldRecord('!wr')
        personalBest('!pb')
        raceCommand('!race')
        quitCommand('!kill')
        continue
