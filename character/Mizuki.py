from Player import Player


class Elizabeth(Player):

    def __init__(self, thirst=10, hunger=10, happiness=10, health=10):
        super().__init__(thirst, hunger, happiness, health)

    # Special skill: Don't have to eat for 4 days

    def skill(self):
        """
        This is the special skill for this character
        :return: None
        """
        # This character doesn't have to drink 5 days total
        pass