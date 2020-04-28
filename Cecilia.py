from Player import Player


class Cecilia(Player):

    def __init__(self, thirst=10, hunger=10, happiness=10, health=10):
        super().__init__(thirst, hunger, happiness, health)
        self.__day = 5

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have to eat in 5 days total
        day = 5
        for day in self.__day:
            day = self.__day - 1


