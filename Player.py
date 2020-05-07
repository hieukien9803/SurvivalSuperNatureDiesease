
class Player(object):

    def __init__(self, thirst, hunger, happiness, health):
        self.__thirst = thirst
        self.__hunger = hunger
        self.__happiness = happiness
        self.__health = health

    def __str__(self):
        return f'thrist point: {self.__thirst}' \
               f'\nhunger point: {self.__hunger}' \
               f'\nhappiness point: {self.__happiness}' \
               f'\nhealth point: {self.__health}'

    def get_happiness(self):
        return self.__happiness

    def get_thirst(self):
        return self.__thirst

    def get_hunger(self):
        return self.__hunger

    def get_health(self):
        return self.__health

    def eat(self):
        return self.__hunger + 1

    def drink(self):
        return self.__thirst + 1

    def play(self):
        return self.__happiness + 1


