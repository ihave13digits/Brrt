import pickle, json, time
from os import path
from random import randint, choice

from res import documentation



class Data:

    def __init__(self):
        self.dir_root = path.dirname(__file__)
        self.dir_data = path.join(self.dir_root, 'data')

    def save(self, data, data_dir):
        with open(path.join(self.dir_data, data_dir), 'wb') as f:
            #pickle.dump(data, f)
            pickle.dump(self.parse_data(data, mode='e'), f)
            f.close()

    def load(self, data_dir):
        to_return = {}
        try:
            with open(path.join(self.dir_data, data_dir), 'rb') as f:
                to_return = pickle.load(f)
                f.close()
        except FileNotFoundError:
            pass
        #return to_return
        return self.parse_data(to_return, mode='d')

    def parse_data(self, data, mode):
        parsed = {
            'dir' : '',
            'owners' : [],
            'secret' : [],
            'introductions' : [],
            'member_data' : {
                'negative' : {},
                'positive' : {},
                'rewards' : {},
                'points' : {},
                'level' : {},
                'lup' : {},
                'exp' : {}
                },
            'playing' : {},
            'enabled' : {
                'documentation' : True,
                'moderation' : True,
                'scoring' : True,
                'welcome' : True,
                'random' : True,
                'social' : True,
                'voting' : True,
                'roles' : True
                },
            'points' :0
            }

        parsed['dir'] = data['dir']
        parsed['owners'] = data['owners']
        parsed['secret'] = data['secret']
        parsed['introductions'] = data['introductions']
        for key in data['playing']:
            parsed['playing'][self.crypt(key, mode=mode)] = data['playing'][key]
        for dct in data['member_data']:
            for key in data['member_data'][dct]:
                parsed['member_data'][dct][self.crypt(key, mode=mode)] = data['member_data'][dct][key]
        parsed['enabled'] = data['enabled']
        parsed['points'] = data['points']

        return parsed

    def crypt(self, txt, key=47, mode='e'):
        chars = "0aZbYcXdW1eVf`U~g,T2.h?S!i@R#3j$Q%k^P&l4*O-m=N_n+5M(o)L{p}K6[q]J<r>I;7s:H/t'G\"8u|F vEwDx9CyBzA"
        cypher = ""
        for c in txt:
            if c in chars:
                if mode == "e":
                    character = (chars.find(c) + key) % 94
                if mode == "d":
                    character = (chars.find(c) - key) % 94
                cypher += chars[character]
            else:
                cypher += c
        return cypher

    @staticmethod
    def pre_start_up():
        with open(path.join('res', 'config.json'),"r") as f:
            data = json.loads(f.read())

        #print config to log for info purposes
        for key in data:
            print("{}: {}".format(key, data[key]))

        TOKEN = data["TOKEN"]
        PREFIX = data["PREFIX"]
        OWNERS = data['OWNERS']
        INTROS = data['INTROS']
        SECRET = data['SECRET']
        return TOKEN, PREFIX, OWNERS, INTROS, SECRET



class Vote:

    def __init__(self):
        self.users = {}
        self.votes = {}
        self.start_time = 0.0
        self.stop_time = 0.0

    def set_vote(self, data):
        self.votes.clear()
        for v in data['votes']:
            self.votes[v] = 0
        print(self.votes)

        now = time.time()
        self.start_time = now + data['start']
        self.stop_time = now + data['stop']

    def cast(self, data):
        if self.users[data['user']] == False and self.can_vote():
            self.users[data['user']] = True
            self.votes[data['vote']] += 1

    def can_vote(self):
        now = time.time()
        if now > self.start_time and now < self.stop_time:
            return True
        else:
            return False

    def get_winner(self):
        winners = {}
        value_to_beat = 0
        for v in self.votes:
            if self.votes[v] > value_to_beat:
                value_to_beat = self.votes[v]
                winners[v] = self.votes[v]

        if len(winners) > 1:
            self.votes = winners
            self.get_winner()

        return winners


class Misc:

    @staticmethod
    def get_docs(d, *a):
        if not a:
            response = str(documentation.docs.get(a, documentation.docs[d]['']))
        else:
            response = str(documentation.docs.get(a, documentation.docs[d][str(a[0])]))
        return response



    @staticmethod
    def style_text(text, frmt):
        #frmt = ['**', '*', '~~', '__', '||']
        for f in frmt:
            "{}{}{}".format(f, text, f)
        return text



    @staticmethod
    def rand_hex():
        value = randint(0, 16777215)
        return value

    @staticmethod
    def flip():
        coin = randint(1, 100)
        if coin % 2 == 0:
            value = 'Tails'
        else:
            value = 'Heads'
        return value

    @staticmethod
    def roll_dice(a):
        response = ""
        lmt = 1
        if not a:
            value = 6
        else:
            # get value
            try:
                value = int(a[0])
            except:
                value = 6
            value = abs(value)
            # check if workable
            if value > 1000:
                value = 1000
                response += "Brrt only roll up to 1,000.\n\n"
            if value <= 2:
                value = 2
            # get limit
            if len(a) > 1:
                try:
                    lmt = int(a[1])
                except:
                    lmt = 1
            # check if workable
            if lmt > 20 or lmt < 1:
                lmt = abs(lmt)
                die_choice = ['dies', 'dices']
                word = choice(die_choice)
                response += "Brrt only roll 1 to 20 {} at a time.\n\n".format(word)
            if lmt > 20:
                lmt = 20
            elif lmt < 1:
                lmt = 1
        for rolls in range(lmt):
            response += str(Misc.roll(value))+"\n"
        return response

    @staticmethod
    def roll(sides):
        try:
            string = ''
            value = randint(1, sides)
            return str(value)
        except:
            pass



