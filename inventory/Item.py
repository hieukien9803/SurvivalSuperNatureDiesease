
class Item(object):

    def __init__(self, name):
        self.__name = str(name).strip()

    def __str__(self):
        return f'{self.name}'

    def get_name(self):
        return self.__name

    name = property(get_name)