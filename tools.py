import pickle, json, time
from os import path
from random import randint, choice

from res import documentation



class Data:

    def __init__(self):
        self.dir_root = path.dirname(__file__)
        self.dir_data = path.join(self.dir_root, 'data')

    def save(self, data):
        with open(path.join(self.dir_data, data['dir']), 'wb') as f:
            pickle.dump(data, f)
            f.close()

    def load(self, data):
        to_return = data
        try:
            with open(path.join(self.dir_data, data['dir']), 'rb') as f:
                to_return = pickle.load(f)
                f.close()
        except FileNotFoundError:
            pass
        return to_return

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
        return TOKEN, PREFIX, OWNERS



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
            value = 'Heads'
        else:
            value = 'Tails'
        return value

    @staticmethod
    def roll(sides):
        try:
            string = ''
            value = randint(1, sides)
            return str(value)
        except:
            pass



