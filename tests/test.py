

def test():
    print('\n----product test----')
    food = Food('Bubble Tea', 'canFood', 13.50)
    print(food)

    print('\n ---player test---')
    player = Player(10,10,10,10)
    print(player)

    print('\n ---drink file test')
    World.read_drinks('drinks')

    print('\n ---foods file test')
    World.read_foods('foods.txt')

    print('\n ---item file test')
    World.read_items('items.txt')


test()