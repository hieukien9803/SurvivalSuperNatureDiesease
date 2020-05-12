class World(object):

    def __init__(self):
        self.__day = 0
        self.__scenario = 0

    def get_day(self):
        """Return the current day"""
        return self.__day

    def get_scenario(self):
        """Return the current scenario"""
        return self.__scenario

    def next_scenario(self):
        """Go up one scenario at a time"""
        self.__scenario += 1

    def next_day(self):
        """Go up one day at a time"""
        self.__day += 1




