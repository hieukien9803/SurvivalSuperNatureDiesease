from Hand import h

class Player(object):

    def __init__(self, food, water, thirst, hunger, happiness):
        self.__food = food
        self.__water = water
        self.__thirst = thirst
        self.__hunger = hunger
        self.__happiness = happiness

    def eat(self):
        return self.__hunger + 1

    def drink(self):
        return self.__thirst + 1

    def play(self):
        return self.__happiness + 1
