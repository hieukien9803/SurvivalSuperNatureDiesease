from toolbox import is_number

class Food(object):
    types = ['fastFood', 'seafood', 'canFood', 'meat', 'fruit']

    def __init__(self, name, type, value):
        self.__name = str(name).strip()
        if is_number(value):
            self.__value = float(value)
        else:
            raise TypeError('Food value must be a numerical type.')
        type = str(type).strip()
        if type in Food.types:
            self.__type = type
        else:
            raise TypeError('Food type must be a member of Food.type.')

    def __str__(self):
        return f'{self.name} ({self.type}) nutrition: {self.value}'

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    name = property(get_name)
    type = property(get_type)
    value = property(get_value)
