from Player import p
from Water import w
from Food import f

class World(object):

    def __init__(self, food, water, player, computer, friend):
        self.__food = food
        self.__water = water
        self.__player = player
        self.__computer = computer
        self.__friend = friend

    def __str__(self):
        string = "Welcome to the game"
        self.__create_player()

    def create_player(self):
        name = input("What is your name? ")





