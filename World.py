
from inventory.Drink import Drink
from inventory.Food import Food
from inventory.Item import Item


class World(object):

    def __init__(self, scenario, day):
        # self.__food = food
        # self.__drink = drink
        # self.__player = []
        # self.__drinks = []
        # self.read_drinks('drinks')
        # self.__foods = []
        # self.read_foods('foods')
        # self.__items = []
        # self.read_items('items')
        self.__scenario = scenario
        self.__day = day

    def read_drinks(self, filename):
        """Read the available drinks from a file."""
        with open(filename, 'r') as drinksFile:
            for line in drinksFile:
                name, type, value, amount = line.split(',')
                try:
                    self.__drinks.append(Drink(name, type, value, amount))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_foods(self, filename):
        """Read the available foods from a file."""
        with open(filename, 'r') as foodsFile:
            for line in foodsFile:
                name, type, value, amount = line.split(',')
                try:
                    self.__drinks.append(Food(name, type, value, amount))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_items(self, filename):
        """Read the available items from a file."""
        with open(filename, 'r') as itemsFile:
            for line in itemsFile:
                name, amount = line.split(',')
                try:
                    self.__items.append(Item(name, amount))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')


    def get_day(self):
        """Go up one day at a time"""
        return self.__day

    def get_scenario(self):
        """Go up 1 scenario at a time"""
        return self.__scenario
