import pygame
from user_interface.button import button
from user_interface.sound import Sound
from Player import Player
from inventory.Item import Item
from inventory.Drink import Drink
from inventory.Food import Food
import toolbox

pygame.init()

########### Load background images
menu_background = pygame.image.load('images/backgrounds/menu_background.png')
menu_background = pygame.transform.scale(menu_background, (1200, 700))
game_background = pygame.image.load('images/backgrounds/game_background.png')
game_background = pygame.transform.scale(game_background, (1200, 710))
character_background = pygame.image.load('images/backgrounds/character_background.png')
character_background = pygame.transform.scale(character_background, (1200, 700))
item_background = pygame.image.load('images/backgrounds/item_background.png')
item_background = pygame.transform.scale(item_background, (1200, 1053))

text1 = pygame.image.load('images/backgrounds/text1.png')
text1 = pygame.transform.scale(text1, (200, 100))

text2 = pygame.image.load('images/backgrounds/text2.png')
text2 = pygame.transform.scale(text2, (230, 100))

text3 = pygame.image.load('images/backgrounds/text3.png')
text3 = pygame.transform.scale(text3, (250, 100))

text4 = pygame.image.load('images/backgrounds/text4.png')
text4 = pygame.transform.scale(text4, (260, 120))

text5 = pygame.image.load('images/backgrounds/text5.png')
text5 = pygame.transform.scale(text5, (250, 420))
########### Load character images

mizuki = pygame.image.load('images/character/mizuki.png')
mizuki = pygame.transform.scale(mizuki, (140, 200))
taylor = pygame.image.load('images/character/taylor.png')
talor = pygame.transform.scale(taylor, (1200, 1053))
cecilia = pygame.image.load('images/character/Cecilia.png')
cecilia = pygame.transform.scale(cecilia, (140, 200))
chingchong = pygame.image.load('images/character/chingchong.png')
chinngchong = pygame.transform.scale(chingchong, (1200, 1053))

############################### Load food images

pizza = pygame.image.load('images/foods/pizza.png')
pizza = pygame.transform.scale(pizza, (120, 110))

banana = pygame.image.load('images/foods/banana.png')
banana = pygame.transform.scale(banana, (120, 110))

burger = pygame.image.load('images/foods/burger.png')
burger = pygame.transform.scale(burger, (120, 110))

ham = pygame.image.load('images/foods/ham.png')
ham = pygame.transform.scale(ham, (120, 110))

sushi = pygame.image.load('images/foods/sushi.png')
sushi = pygame.transform.scale(sushi, (120, 110))

tuna = pygame.image.load('images/foods/tuna_can.png')
tuna = pygame.transform.scale(tuna, (120, 110))
################################### Load drinks images
beer = pygame.image.load('images/drinks/beer.png')
beer = pygame.transform.scale(beer, (120, 110))

bubble = pygame.image.load('images/drinks/bubble_tea.png')
bubble = pygame.transform.scale(bubble, (120, 110))

coca = pygame.image.load('images/drinks/coca.png')
coca = pygame.transform.scale(coca, (75, 90))

coffee = pygame.image.load('images/drinks/coffee.png')
coffee = pygame.transform.scale(coffee, (120, 110))

milk = pygame.image.load('images/drinks/milk.png')
milk = pygame.transform.scale(milk, (120, 110))

water = pygame.image.load('images/drinks/water.png')
water = pygame.transform.scale(water, (120, 110))

wine = pygame.image.load('images/drinks/wine.png')
wine = pygame.transform.scale(wine, (120, 110))
################################ Load item images
computer = pygame.image.load('images/items/computer.png')
computer = pygame.transform.scale(computer, (160, 150))

first_aid = pygame.image.load('images/items/first_aid.png')
first_aid = pygame.transform.scale(first_aid, (180, 150))

mask = pygame.image.load('images/items/mask.png')
mask = pygame.transform.scale(mask, (130, 130))

musket = pygame.image.load('images/items/musket.png')
musket = pygame.transform.scale(musket, (130, 120))
display_width = 800
display_height = 600


# This is a small test for the button
def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont('comicsans', 90)
    TextSurf, TextRect = text_objects(text, largeText)
    win.blit(TextSurf, TextRect)


def drawWin(stages):
    if stages == 'menu':
        win.blit(menu_background, (0, 0))
        win.blit(pizza, (100, 100))
        win.blit(sushi, (300, 300))
        win.blit(coca, (200, 200))
        startButton.draw(win, (0, 0, 0))
        quitButton.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "character":
        win.blit(character_background, (0, 0))

        message_display("ChOOsE YoUr ChAraCteR")
        win.blit(text1, (60, 170))
        win.blit(text2, (350, 170))
        win.blit(text3, (630, 170))
        win.blit(text4, (900, 170))

        win.blit(cecilia, (970, 320))
        win.blit(taylor, (360, 300))
        win.blit(mizuki, (700, 320))
        win.blit(chingchong, (50, 320))
        button1.draw(win, (0, 0, 0))
        button2.draw(win, (0, 0, 0))
        button3.draw(win, (0, 0, 0))
        button4.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "item":
        win.blit(item_background, (0, 0))
        win.blit(musket, (600, 100))
        win.blit(computer, (300, 100))
        win.blit(first_aid, (580, 400))
        win.blit(mask, (300, 400))
        win.blit(text5, (880, 100))
        button5.draw(win, (0, 0, 0))
        button6.draw(win, (0, 0, 0))
        button7.draw(win, (0, 0, 0))
        button8.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "game":
        win.blit(game_background, (0, 0))
        draw(selection)
        pygame.display.update()


def draw(selection):
    if selection == "computer":
        win.blit(computer, (200, 200))
    if selection == "mask":
        win.blit(computer, (200, 200))
    if selection == "musket":
        win.blit(computer, (200, 200))
    if selection == "first_aid":
        win.blit(computer, (200, 200))


####### MAIN GAME ###########


pygame.display.set_caption("Epidemic")
winWidth = 1200
winHeight = 700
win = pygame.display.set_mode((winWidth, winHeight))

run = True
startButton = button((0, 255, 255), 450, 400, 300, 100, "Start")
quitButton = button((0, 255, 255), 450, 520, 300, 60, "Quit")

button1 = button((0, 255, 255), 100, 550, 120, 60, "Ying")
button2 = button((0, 255, 255), 400, 550, 120, 60, "Taylor")
button3 = button((0, 255, 255), 700, 550, 120, 60, "Mizuki")
button4 = button((0, 255, 255), 1000, 550, 120, 60, "Cecilia")

button5 = button((0, 255, 255), 300, 270, 175, 60, "Computer")
button6 = button((0, 255, 255), 600, 270, 130, 60, "Musket")
button7 = button((0, 255, 255), 300, 570, 120, 60, "Mask")
button8 = button((0, 255, 255), 600, 570, 150, 60, "First-Aid")

stages = "menu"
# winsound.PlaySound("gameMusic", winsound.SND_FILENAME)
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
                stages = "character"
            if button1.isOver(mousePos) and stages == "character":
                player = Player(10, 10, 10, 10)
                print("You chose Ying")
                stages = "item"
            elif button2.isOver(mousePos) and stages == "character":
                player = Player(10, 10, 10, 20)
                print("You chose Taylor")
                stages = "item"
            elif button3.isOver(mousePos) and stages == "character":
                player = Player(15, 15, 10, 10)
                print("You chose Mizuki")
                stages = "item"
            elif button4.isOver(mousePos) and stages == "character":
                player = Player(10, 10, 20, 10)
                print("You chose Cecilia")
                stages = "item"

            if button5.isOver(mousePos) and stages == "item":
                print("You got a computer")
                selection = 'computer'
                draw(selection)
                stages = "game"

            elif button6.isOver(mousePos) and stages == "item":
                print("You got a musket")
                selection = 'musket'
                draw(selection)
                stages = "game"

            elif button7.isOver(mousePos) and stages == "item":
                print("You got a mask")
                selection = 'mask'
                draw(selection)
                stages = "game"

            elif button8.isOver(mousePos) and stages == "item":
                print("You got first-aid kit")
                selection = 'first_aid'
                draw(selection)
                stages = "game"

            # Check the event for the button

            if quitButton.isOver(mousePos) and stages == 'menu':
                print("quit")
                run = False
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEMOTION and stages == 'menu':
            if startButton.isOver(mousePos) and stages == 'menu':
                startButton.color = (255, 0, 0)
            else:
                startButton.color = 0, 255, 255

            if quitButton.isOver(mousePos) and stages == 'menu':
                quitButton.color = (255, 0, 0)
            else:
                quitButton.color = 0, 255, 255

"""
        if event.type == pygame.MOUSEMOTION and stages == 'character':
            if button1.isOver(mousePos) and stages == 'character':
                button1.color = (255, 0, 0)
            else:
                button1.color = 0, 255, 255

            if button2.isOver(mousePos) and stages == 'character':
                button2.color = (255, 0, 0)
            else:
                button2 = 0, 255, 255

            if button3.isOver(mousePos) and stages == 'character':
                button3.color = (255, 0, 0)
            else:
                button2 = 0, 255, 255

            if button4.isOver(mousePos) and stages == 'character':
                button4.color = (255, 0, 0)
            else:
                button4 = 0, 255, 255
"""
