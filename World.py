class World(object):

    def __init__(self):
        self.__day = 3
        self.__scenario = 3

    def __str__(self):
        return self.__day

    def get_day(self):
        return self.__day

    def get_scenario(self):
        return self.__scenario

    def next_scenario(self):
        """Go up one scenario at a time"""
        self.__scenario += 1

    def next_day(self):
        """Go up one day at a time"""
        self.__day += 1




