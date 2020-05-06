from toolbox import is_number

class Drink(object):
    types = ['water', 'soda', 'liquor']

    def __init__(self, name, type, value, amount):
        self.__name = str(name).strip()
        self.__amount = amount
        if is_number(value):
            self.__value = float(value)
        else:
            raise TypeError('Drink value must be a numerical type.')
        type = str(type).strip()
        if type in Drink.types:
            self.__type = type
        else:
            raise TypeError('Drink type must be a member of Drink.type.')

    def __str__(self):
        return f'{self.name} ({self.type}) nutrition: {self.value}'

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def get_amount(self):
        return self.__amount

    name = property(get_name)
    type = property(get_type)
    value = property(get_value)
    amount = property(get_amount)
