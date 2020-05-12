from Player import Player


class Mizuki(Player):

    def __init__(self, thirst, hunger, happiness):
        super().__init__(thirst, hunger, happiness)

    # Special skill: Don't have to eat for 4 days

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have to drink 5 days total
        pass