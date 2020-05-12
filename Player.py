class Player(object):

    def __init__(self, thirst, hunger, happiness):
        self.__thirst = thirst
        self.__hunger = hunger
        self.__happiness = happiness

    def __str__(self):
        """Return a string as the current point of the player"""
        return (f'thrist point: {self.__thirst}'
                f'\nhunger point: {self.__hunger}'
                f'\nhappiness point: {self.__happiness}')

    def get_happiness(self):
        return self.__happiness

    def get_thirst(self):
        return self.__thirst

    def get_hunger(self):
        return self.__hunger

    def hungry(self):
        self.__hunger = self.__hunger - 1
        return self.__hunger

    def thirsty(self):
        self.__thirst = self.__thirst - 1
        return self.__thirst

    def bored(self):
        self.__happiness = self.__happiness - 1
        return self.__happiness

    def eat(self):
        self.__hunger = self.__hunger + 1
        return self.__hunger

    def drink(self):
        self.__thirst = self.__thirst + 1
        return self.__thirst

    def play(self):
        self.__happiness = self.__happiness + 1
        return self.__happiness + 1
