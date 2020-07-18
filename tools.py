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
    def api(a):
        response = str(documentation.api.get(a, documentation.api['']))
        return response

    @staticmethod
    def source(a):
        response = str(documentation.source.get(a, documentation.source['']))
        return response

    @staticmethod
    def c(a):
        response = str(documentation.c.get(a, documentation.c['']))
        return response

    @staticmethod
    def c_sharp(a):
        response = str(documentation.c_sharp.get(a, documentation.c_sharp['']))
        return response

    @staticmethod
    def c_pp(a):
        response = str(documentation.c_pp.get(a, documentation.c_pp['']))
        return response

    @staticmethod
    def java(a):
        response = str(documentation.java.get(a, documentation.java['']))
        return response

    @staticmethod
    def javascript(a):
        response = str(documentation.javascript.get(a, documentation.javascript['']))
        return response

    @staticmethod
    def lua(a):
        response = str(documentation.lua.get(a, documentation.lua['']))
        return response

    @staticmethod
    def perl(a):
        response = str(documentation.perl.get(a, documentation.perl['']))
        return response

    @staticmethod
    def python(a):
        response = str(documentation.python.get(a, documentation.python['']))
        return response

    @staticmethod
    def ruby(a):
        response = str(documentation.ruby.get(a, documentation.ruby['']))
        return response

    @staticmethod
    def rust(a):
        response = str(documentation.rust.get(a, documentation.rust['']))
        return response



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
    def roll(sides):
        try:
            string = ''
            value = randint(1, sides)
            return str(value)
        except:
            pass



