from Player import Player


class Ying(Player):

    def __init__(self, thirst, hunger, happiness):
        super().__init__(thirst, hunger, happiness)
        self.__day = 5

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have a skill yet
        pass


