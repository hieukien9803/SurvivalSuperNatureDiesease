
class Item(object):

    def __init__(self, name, amount):
        self.__name = str(name).strip()
        self.__amount = amount

    def __str__(self):
        return f'{self.name}'

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    name = property(get_name)