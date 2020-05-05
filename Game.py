import pygame
from user_interface.button import button
from user_interface.sound import Sound
from Player import Player
from inventory import Food, Drink, Item
import toolbox
pygame.init()



########### Load background images
menu_background = pygame.image.load('images/backgrounds/menu_background.png')
menu_background = pygame.transform.scale(menu_background, (1200,700))
game_background = pygame.image.load('images/backgrounds/game_background.png')
game_background = pygame.transform.scale(game_background, (1200,1053))
character_background = pygame.image.load('images/backgrounds/character_background.png')
character_background = pygame.transform.scale(character_background, (1200,1053))
item_background = pygame.image.load('images/backgrounds/item_background.png')
item_background = pygame.transform.scale(item_background, (1200,1053))

############################### Load food images



pizza = pygame.image.load('images/foods/pizza.png')
pizza = pygame.transform.scale(pizza, (120,110)).convert_alpha()





banana = pygame.image.load('images/foods/banana.png')
banana = pygame.transform.scale(banana, (120,110))

burger = pygame.image.load('images/foods/burger.png')
burger = pygame.transform.scale(burger, (120,110))

ham = pygame.image.load('images/foods/ham.png')
ham = pygame.transform.scale(ham, (120,110))

sushi = pygame.image.load('images/foods/sushi.png')
sushi = pygame.transform.scale(sushi, (120,110))

tuna = pygame.image.load('images/foods/tuna_can.png')
tuna = pygame.transform.scale(tuna, (120,110))
################################### Load drinks images
beer = pygame.image.load('images/drinks/beer.png')
beer = pygame.transform.scale(beer, (120,110))

bubble = pygame.image.load('images/drinks/bubble_tea.png')
bubble = pygame.transform.scale(bubble, (120,110))

coca = pygame.image.load('images/drinks/coca.png')
coca = pygame.transform.scale(coca, (75,90))

coffee = pygame.image.load('images/drinks/coffee.png')
coffee = pygame.transform.scale(coffee, (120,110))

milk = pygame.image.load('images/drinks/milk.png')
milk = pygame.transform.scale(milk, (120,110))

water = pygame.image.load('images/drinks/water.png')
water = pygame.transform.scale(water, (120,110))

wine = pygame.image.load('images/drinks/wine.png')
wine = pygame.transform.scale(wine, (120,110))
################################ Load item images
computer = pygame.image.load('images/items/computer.png')
computer = pygame.transform.scale(computer, (120,110))

first_aid = pygame.image.load('images/items/first_aid.png')
first_aid = pygame.transform.scale(first_aid, (120,110))

mask = pygame.image.load('images/items/mask.png')
mask = pygame.transform.scale(mask, (120,110))

medicine = pygame.image.load('images/items/medicine.png')
medicine = pygame.transform.scale(medicine, (120,110))

musket = pygame.image.load('images/items/musket.png')
musket = pygame.transform.scale(musket, (120,110))

phone = pygame.image.load('images/items/phone.png')
phone = pygame.transform.scale(phone, (120,110))


# This is a small test for the button
def drawWin(stages):
    if stages == 'menu':
        win.blit(menu_background, (0, 0))
        win.blit(pizza, (100,100))
        win.blit(coca, (200, 200))
        startButton.draw(win, (0, 0, 0))
        quitButton.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "character":
        win.blit(character_background, (0, 0))
        button1.draw(win, (0, 0, 0))
        button2.draw(win, (0, 0, 0))
        button3.draw(win, (0, 0, 0))
        button4.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "item":
        win.blit(item_background, (0,0))
####### MAIN GAME ###########


pygame.display.set_caption("Epidemic")
winWidth = 1200
winHeight = 700
win = pygame.display.set_mode((winWidth, winHeight))

run = True
startButton = button((0, 255, 255), 450, 400, 300, 100, "Start")
quitButton = button((0, 255, 255), 450, 520, 300, 60, "Quit")
stages = "menu"
#winsound.PlaySound("gameMusic", winsound.SND_FILENAME)
while run:
    drawWin(stages)
    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(mousePos) and stages == 'menu':
                print("clicked")
                button1 = button((0, 255, 255), 100, 550, 120, 60, "Hieu")
                button2 = button((0, 255, 255), 400, 550, 120, 60, "Taylor")
                button3 = button((0, 255, 255), 700, 550, 120, 60, "Mizuki")
                button4 = button((0, 255, 255), 1000, 550, 120, 60, "Cecilia")
                stages = "character"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.isOver(mousePos) and stages == "character":
                        player = Player(10, 10, 10, 10)
                        print("You chose Hieu")
                    elif button2.isOver(mousePos) and stages == "character":
                        player = Player(10, 10, 10, 20)
                        print("You chose Taylor")
                    elif button3.isOver(mousePos) and stages == "character":
                        player = Player(15, 15, 10, 10)
                        print("You chose Mizuki")
                    elif button4.isOver(mousePos) and stages == "character":
                        player = Player(10, 10, 20, 10)
                        print("You chose Cecilia")

                elif event.type == pygame.MOUSEMOTION and stages == "menu":
                    if button1.isOver(mousePos) and stages == 'character':
                        button1.color = (255, 0, 0)
                    else:
                        button1.color = 0, 255, 255

                    if button2.isOver(mousePos) and stages == 'character':
                        button2.color = (255, 0, 0)
                    else:
                        button2 = 0, 255, 255

        # Check the event for the button

            if quitButton.isOver(mousePos) and stages == 'menu':
                print("quit")
                run = False
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEMOTION and stages == "menu":
            if startButton.isOver(mousePos):
                startButton.color = (255, 0, 0)
            else:
                startButton.color = 0, 255, 255

            if quitButton.isOver(mousePos):
                quitButton.color = (255, 0, 0)
            else:
                quitButton.color = 0, 255, 255



