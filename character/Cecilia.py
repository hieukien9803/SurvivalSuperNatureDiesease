from Player import Player


class Cecilia(Player):

    def __init__(self, thirst, hunger, happiness):
        super().__init__(thirst, hunger, happiness)

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have a skill yet
        pass

