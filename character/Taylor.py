from Player import Player


class Taylor(Player):

    def __init__(self, thirst, hunger, happiness):
        super().__init__(thirst, hunger, happiness)

    # Special skill:

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have to drink 5 days total
        pass