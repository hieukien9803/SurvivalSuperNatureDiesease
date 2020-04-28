from Drink import Drink
from Food import Food
from World import World
from Item import Item
from Cecilia import Cecilia
from Elizabeth import Elizabeth

class Game(object):

    def __init__(self):
        self.__world = World(20, 20)
        self.__menu = 'main'

    def main(self):
        """Main event loop for store."""
        command = 'help'
        parameter = None
        while command != 'quit':
            if command == 'help':
                if self.__menu == 'main':
                    self.help('help.txt', 'Press <return> to continue.')
                elif self.__menu == 'more':
                    self.help('help2.txt', 'Press <return> to continue.')
            if command == 'more menu':
                self.__menu = 'more'
            if command == 'back to main menu':
                self.__menu = 'main'
            elif command == 'create player':
                self.create_player(parameter)
            elif command == 'create item':
                self.create_item(parameter)
            self.display()
            command, parameter = self.get_command()
        print('goodbye')

    def menu(self):
        """returns a string containing the menu."""
        return '[P]layer  [I]tem   [N]ext   [M]ore   [H]elp   [Q]uit'

    def menu_more(self):
        """returns a string containing the menu."""
        return '[S]ave   [O]pen   [H]elp   [B]ack'

    def get_command(self):
        """Get a valid command from the user."""
        commands = {'p': 'create player',
                    'i': 'create item',
                    'm': 'more menu',
                    'b': 'back to main menu',
                    'h': 'help',
                    '?': 'help',
                    'q': 'quit'}

        validCommands = commands.keys()

        userInput = '&'
        parameter = None
        while userInput[0].lower() not in validCommands:
            userInput = input('Command: ')
            if userInput == '':
                userInput = 'n'
                parameter = 1
        command = commands[userInput[0].lower()]
        if len(userInput) > 1:
            parameter = userInput[1:].strip()
        return command, parameter

    def create_player(self):
        Cecilia.__str__()
        Elizabeth.__str__()

    def status(self):
        """Returns a string representing the status of the world."""
        string = 'Day:   '

        return string

    def help(self, filename, prompt=None):
        """Displays instructions."""
        with open(filename, 'r') as file:
            help = file.read()
        print(help, end='')
        if prompt:
            input('\n' + prompt)

    def next_day(self, parameter):
        """Displays the next day of the game"""
        self.__world.next_day()

    def display(self):
        """
        Prints the world, status bar and menu
        :return: None
        """
        if self.__menu == 'main':
            print(self.__world, self.status() + '\n' + self.menu())
        elif self.__menu == 'more':
            print(self.__world, self.status() + '\n' + self.menu_more())


if __name__ == '__main__':
    simulation = Game()
    simulation.main()