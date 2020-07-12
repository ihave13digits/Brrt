import pickle, time
from os import path
from random import randint, choice

from res import documentation, brrt_help



class Data:

    def __init__(self):
        self.dir_root = path.dirname(__file__)
        self.dir_data = path.join(self.dir_root, 'data')

    def save(self, data):
        with open(path.join(self.dir_data, data['dir']), 'wb') as f:
            pickle.dump(data, f)
            f.close()

    def load(self, data):
        try:
            with open(path.join(self.dir_data, data['dir']), 'rb') as f:
                to_return = pickle.load(f)
                f.close()
        except FileNotFoundError:
            pass
        return to_return



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
    def helper(a):
        response = str(brrt_help.helper[a])
        return response

    @staticmethod
    def source(a):
        response = str(documentation.source[a])
        return response

    @staticmethod
    def python(a):
        response = str(documentation.python[a])
        return response

    @staticmethod
    def rust(a):
        response = str(documentation.rust[a])
        return response

    @staticmethod
    def roll(sides):
        try:
            string = ''
            if sides > 1000:
                sides = 1000
                string += "Brrt only roll up to 1,000.\n"
            value = randint(1, int(sides))
            string += str(value)
            return string
        except:
            pass



class Score:

    def __init__(self):
        self.points = 0
        self.level = 0
        self.experience = 0
        self.next_level = 10

    def level_up(self):
        self.points += 100
        self.level += 1
        self.experience -= self.next_level
