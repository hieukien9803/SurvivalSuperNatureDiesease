from Drink import Drink
from Food import Food
from Item import Item

class World(object):

    def __init__(self, food, drink):
        self.__food = food
        self.__drink = drink
        self.__player = []
        self.__drinks = []
        self.read_drinks('drinks')
        self.__foods = []
        self.read_foods('foods')
        self.__items = []
        self.read_items('items')

    def __str__(self):
        pass

    def read_drinks(self, filename):
        """Read the available drinks from a file."""
        with open(filename, 'r') as drinksFile:
            for line in drinksFile:
                name, type, value = line.split(',')
                try:
                    self.__drinks.append(Drink(name, type, value))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_foods(self, filename):
        """Read the available foods from a file."""
        with open(filename, 'r') as foodsFile:
            for line in foodsFile:
                name, type, value = line.split(',')
                try:
                    self.__drinks.append(Food(name, type, value))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_items(self, filename):
        """Read the available items from a file."""
        with open(filename, 'r') as itemsFile:
            for line in itemsFile:
                name = line.split(',')
                try:
                    self.__items.append(Item(name))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')








