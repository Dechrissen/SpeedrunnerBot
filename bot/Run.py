import string
import time
import math
import urllib.request
from urllib.request import urlopen
from json import loads
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import getUser, getMessage
from Settings import CHANNEL, COOLDOWN, IDENT, CHANNELPASS, SRC_USERNAME, GAMES, CATEGORIES


#Returns the world record for the category that's written in the stream title
def worldRecord(input):
    if input == message.lower().split()[0].strip():
        #Check to see if an argument is specified first
        argument = False
        try:
            message.lower().split()[1]
        except IndexError as err:
            pass
        else:
            argument = True

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
                platform = GAMES[i][3]
                break

        category = None
        category_title = None

        #Check again to see if an argument was specified
        if argument == False:
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() in title:
                    category = CATEGORIES[i][1]
                    category_title = CATEGORIES[i][0]
                    break
        elif argument == True:
            specified_category = message.lower().split(input, 1)[-1].strip()
            for i in range(len(CATEGORIES)):
                if specified_category == CATEGORIES[i][0].lower():
                    category_title = CATEGORIES[i][0]
                    category = CATEGORIES[i][1]
                    break
            if category == None:
                sendMessage(s, "Error: Invalid category specified")
                cooldown()
                return

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?top=1&embed=players&platform={}'.format(game, category, platform))
            readable = response.read().decode('utf-8')
            lst = loads(readable)
            runner = lst['data']['players']['data'][0]['names']['international']
            time_in_sec = int(lst['data']['runs'][0]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            wr = ''
            if hours[0] > 0:
                wr = str(hours[0]) + "h " + str(minutes[0]) + "m " + str(seconds) + "s "
            elif minutes[0] > 0:
                wr = str(minutes[0]) + "m " + str(seconds) + "s "
            else:
                wr = str(seconds) + "s "

            sendMessage(s, "The " + category_title + " world record is " + wr + "by " + runner + ".")
            cooldown()
            return

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return


def second(input):
    if input == message.lower().split()[0].strip():
        #Check to see if an argument is specified first
        argument = False
        try:
            message.lower().split()[1]
        except IndexError as err:
            pass
        else:
            argument = True

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
                platform = GAMES[i][3]
                break

        category = None
        category_title = None

        #Check again to see if an argument was specified
        if argument == False:
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() in title:
                    category = CATEGORIES[i][1]
                    category_title = CATEGORIES[i][0]
                    break
        elif argument == True:
            specified_category = message.lower().split(input, 1)[-1].strip()
            for i in range(len(CATEGORIES)):
                if specified_category == CATEGORIES[i][0].lower():
                    category_title = CATEGORIES[i][0]
                    category = CATEGORIES[i][1]
                    break
            if category == None:
                sendMessage(s, "Error: Invalid category specified")
                cooldown()
                return

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?top=2&embed=players&platform={}'.format(game, category, platform))
            readable = response.read().decode('utf-8')
            lst = loads(readable)
            runner = lst['data']['players']['data'][1]['names']['international']
            time_in_sec = int(lst['data']['runs'][1]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            place2nd = ''
            if hours[0] > 0:
                place2nd = str(hours[0]) + "h " + str(minutes[0]) + "m " + str(seconds) + "s "
            elif minutes[0] > 0:
                place2nd = str(minutes[0]) + "m " + str(seconds) + "s "
            else:
                place2nd = str(seconds) + "s "

            sendMessage(s, "The 2nd place time for " + category_title + " is " + place2nd + "by " + runner + ".")
            cooldown()
            return

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return


def third(input):
    if input == message.lower().split()[0].strip():
        #Check to see if an argument is specified first
        argument = False
        try:
            message.lower().split()[1]
        except IndexError as err:
            pass
        else:
            argument = True

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
                platform = GAMES[i][3]
                break

        category = None
        category_title = None

        #Check again to see if an argument was specified
        if argument == False:
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() in title:
                    category = CATEGORIES[i][1]
                    category_title = CATEGORIES[i][0]
                    break
        elif argument == True:
            specified_category = message.lower().split(input, 1)[-1].strip()
            for i in range(len(CATEGORIES)):
                if specified_category == CATEGORIES[i][0].lower():
                    category_title = CATEGORIES[i][0]
                    category = CATEGORIES[i][1]
                    break
            if category == None:
                sendMessage(s, "Error: Invalid category specified")
                cooldown()
                return

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?top=3&embed=players&platform={}'.format(game, category, platform))
            readable = response.read().decode('utf-8')
            lst = loads(readable)
            runner = lst['data']['players']['data'][2]['names']['international']
            time_in_sec = int(lst['data']['runs'][2]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            place3rd = ''
            if hours[0] > 0:
                place3rd = str(hours[0]) + "h " + str(minutes[0]) + "m " + str(seconds) + "s "
            elif minutes[0] > 0:
                place3rd = str(minutes[0]) + "m " + str(seconds) + "s "
            else:
                place3rd = str(seconds) + "s "

            sendMessage(s, "The 3rd place time for " + category_title + " is " + place3rd + "by " + runner + ".")
            cooldown()
            return

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return


def fourth(input):
    if input == message.lower().split()[0].strip():
        #Check to see if an argument is specified first
        argument = False
        try:
            message.lower().split()[1]
        except IndexError as err:
            pass
        else:
            argument = True

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
                platform = GAMES[i][3]
                break

        category = None
        category_title = None

        #Check again to see if an argument was specified
        if argument == False:
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() in title:
                    category = CATEGORIES[i][1]
                    category_title = CATEGORIES[i][0]
                    break
        elif argument == True:
            specified_category = message.lower().split(input, 1)[-1].strip()
            for i in range(len(CATEGORIES)):
                if specified_category == CATEGORIES[i][0].lower():
                    category_title = CATEGORIES[i][0]
                    category = CATEGORIES[i][1]
                    break
            if category == None:
                sendMessage(s, "Error: Invalid category specified")
                cooldown()
                return

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        if category != None:
            response = urlopen('https://www.speedrun.com/api/v1/leaderboards/{}/category/{}?top=4&embed=players&platform={}'.format(game, category, platform))
            readable = response.read().decode('utf-8')
            lst = loads(readable)
            runner = lst['data']['players']['data'][3]['names']['international']
            time_in_sec = int(lst['data']['runs'][3]['run']['times']['realtime_t'])
            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            place4th = ''
            if hours[0] > 0:
                place4th = str(hours[0]) + "h " + str(minutes[0]) + "m " + str(seconds) + "s "
            elif minutes[0] > 0:
                place4th = str(minutes[0]) + "m " + str(seconds) + "s "
            else:
                place4th = str(seconds) + "s "

            sendMessage(s, "The 4th place time for " + category_title + " is " + place4th + "by " + runner + ".")
            cooldown()
            return

        elif category == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

#Returns the channel owner's personal best time for the category that's written in the stream title
def personalBest(input):
    if input == message.lower().split()[0]:
        category_specified = False
        try:
            message.split()[2]
        except IndexError as err:
            pass
        else:
            category_specified = True

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
                game = GAMES[i][1].lower()
                platform_title = GAMES[i][2]
                break

        category_title = None
        if category_specified == True:
            category_title = message.lower().strip('!pb ')
            first_word = category_title.lower().split()[0]
            category_title = category_title.split(first_word, 1)[-1].strip()
            check = False
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() == category_title:
                    check = True
                    category_title = CATEGORIES[i][0]
                    break
            if check == False:
                sendMessage(s, "Error: Invalid category specified")
                cooldown()
                return

        elif category_specified == False:
            for i in range(len(CATEGORIES)):
                if CATEGORIES[i][0].lower() in title:
                    category_title = CATEGORIES[i][0]
                    break

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        username = None
        try:
            message.split()[1]
        except IndexError as err:
            username = SRC_USERNAME
        else:
            username = message.split()[1]


        if category_title != None:
            try:
                response = urlopen('https://www.speedrun.com/api/v1/users/{}/personal-bests?embed=category,game,platform'.format(username))
            except urllib.error.HTTPError as err:
                sendMessage(s, "Error: Speedrun.com user not found")
                cooldown()
                return

            readable = response.read().decode('utf-8')
            lst = loads(readable)

            place = None
            time_in_sec = None
            for cat in lst['data']:
                if cat['category']['data']['name'].lower() == category_title.lower() and cat['game']['data']['abbreviation'].lower() == game and cat['platform']['data']['name'] == platform_title:
                    time_in_sec = int(cat['run']['times']['realtime_t'])
                    place = cat['place']
                    break

            if place == None:
                sendMessage(s, username.title() + " currently does not have a PB for " + category_title + " on the leaderboard.")
                cooldown()
                return

            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

            hours = divmod(time_in_sec, 3600)
            minutes = divmod(hours[1], 60)
            seconds = minutes[1]
            pb = ''
            if hours[0] > 0:
                pb = str(hours[0]) + "h " + str(minutes[0]) + "m " + str(seconds) + "s"
            elif minutes[0] > 0:
                pb = str(minutes[0]) + "m " + str(seconds) + "s"
            else:
                pb = str(seconds) + "s"

            sendMessage(s, username.title() + "\'s " + category_title + " PB is " + pb + " (" + ordinal(place) + " place).")
            cooldown()

        elif category_title == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return
        
        
#Tells user the leaderboard standing of the channel owner, or a specified user
def place(input):
    if input == message.lower().split()[0]:
        username = None
        try:
            message.split()[1]
        except IndexError as err:
            username = SRC_USERNAME
        else:
            username = message.split()[1]

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
                game = GAMES[i][1].lower()
                platform_title = GAMES[i][2]
                break

        if game == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        category_title = None
        for i in range(len(CATEGORIES)):
            if CATEGORIES[i][0].lower() in title:
                category_title = CATEGORIES[i][0]
                break

        if category_title != None:
            try:
                response = urlopen('https://www.speedrun.com/api/v1/users/{}/personal-bests?embed=category,game,platform'.format(username))
            except urllib.error.HTTPError as err:
                sendMessage(s, "Error: Speedrun.com user not found")
                cooldown()
                return

            readable = response.read().decode('utf-8')
            lst = loads(readable)

            place = None
            time_in_sec = None
            for cat in lst['data']:
                if cat['category']['data']['name'].lower() == category_title.lower() and cat['game']['data']['abbreviation'].lower() == game and cat['platform']['data']['name'] == platform_title:
                    time_in_sec = int(cat['run']['times']['realtime_t'])
                    place = cat['place']
                    break

            if place == None:
                sendMessage(s, username.title() + " currently does not have a PB for " + category_title + " on the leaderboard.")
                cooldown()
                return

            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

            sendMessage(s, username.title() + " is in " + ordinal(place) + " place for " + category_title + ".")

        elif category_title == None:
            sendMessage(s, "No game and/or category detected in stream title.")
            cooldown()
            return

        

def leaderboard(input):
    if input == message.lower().strip():
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
        game_title = None

        for i in range(len(GAMES)):
            if GAMES[i][0].lower() in title:
                game = GAMES[i][1]
                game_title = GAMES[i][0]
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
            sendMessage(s, game_title + " " + category_title + " Leaderboard: https://www.speedrun.com/{}#{}".format(game, category))
            cooldown()
            return

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


        sendMessage(s, "Race link: http://kadgar.net/live/" + CHANNEL + "/".join(contenders))
        cooldown()


#Displays commands
def getCommands(input):
    if input == message.strip().lower():
        sendMessage(s, 'Commands: !wr • !2nd • !3rd • !4th • !pb • !leaderboard • !race')
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
        sendMessage(s, "[Disconnected]")
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
        second('!2nd')
        third('!3rd')
        fourth('!4th')
        personalBest('!pb')
        place('!place')
        leaderboard('!leaderboard')
        raceCommand('!race')
        quitCommand('!kill')
        continue
