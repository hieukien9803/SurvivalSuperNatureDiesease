import pygame
from user_interface.button import button
from user_interface.sound import Sound
from Player import Player
from inventory.Item import Item
from inventory.Drink import Drink
from inventory.Food import Food
import random
import toolbox

pygame.init()

########### Load background images
menu_background = pygame.image.load('images/backgrounds/menu_background.png')
menu_background = pygame.transform.scale(menu_background, (1200, 700))
game_background = pygame.image.load('images/backgrounds/game_background.png')
game_background = pygame.transform.scale(game_background, (1200, 710))

character_background = pygame.image.load('images/backgrounds/character_background/character_background.png')
character_background = pygame.transform.scale(character_background, (1200, 700))
item_background = pygame.image.load('images/backgrounds/item_background/item_background.png')
item_background = pygame.transform.scale(item_background, (1200, 1053))

text1 = pygame.image.load('images/backgrounds/character_background/text1.png')
text1 = pygame.transform.scale(text1, (200, 100))

text2 = pygame.image.load('images/backgrounds/character_background/text2.png')
text2 = pygame.transform.scale(text2, (230, 100))

text3 = pygame.image.load('images/backgrounds/character_background/text3.png')
text3 = pygame.transform.scale(text3, (250, 100))

text4 = pygame.image.load('images/backgrounds/character_background/text4.png')
text4 = pygame.transform.scale(text4, (260, 120))

text5 = pygame.image.load('images/backgrounds/item_background/text5.png')
text5 = pygame.transform.scale(text5, (250, 420))
######## Load scenario images
scenario1 = pygame.image.load('images/backgrounds/scenarios/scenario1.png')
scenario2 = pygame.image.load('images/backgrounds/scenarios/scenario2.png')
scenario3 = pygame.image.load('images/backgrounds/scenarios/scenario3.png')
scenario4 = pygame.image.load('images/backgrounds/scenarios/scenario4.png')
scenario5 = pygame.image.load('images/backgrounds/scenarios/scenario5.png')
scenario6 = pygame.image.load('images/backgrounds/scenarios/scenario6.png')
scenario7 = pygame.image.load('images/backgrounds/scenarios/scenario7.png')
scenario8 = pygame.image.load('images/backgrounds/scenarios/scenario8.png')
scenario9 = pygame.image.load('images/backgrounds/scenarios/scenario9.png')
scenario10 = pygame.image.load('images/backgrounds/scenarios/scenario10.png')
scenario11 = pygame.image.load('images/backgrounds/scenarios/scenario11.png')
########  Load scenario result images
scenario1end = pygame.image.load('images/backgrounds/scenarios/scenario1end.png') # Dead
scenario1sur = pygame.image.load('images/backgrounds/scenarios/scenario1sur.png') # Nothing

scenario2end = pygame.image.load('images/backgrounds/scenarios/scenario2end.png') # Dead
scenario2sur = pygame.image.load('images/backgrounds/scenarios/scenario2sur.png') # Nothing

scenario3end = pygame.image.load('images/backgrounds/scenarios/scenario3end.png') # Nothing
scenario3sur = pygame.image.load('images/backgrounds/scenarios/scenario3sur.png') # Lost all the food

scenario4end = pygame.image.load('images/backgrounds/scenarios/scenario4end.png') # Dead
scenario4sur = pygame.image.load('images/backgrounds/scenarios/scenario4sur.png') # Nothing

scenario5end = pygame.image.load('images/backgrounds/scenarios/scenario5end.png') # Nothing
scenario5sur = pygame.image.load('images/backgrounds/scenarios/scenario5sur.png') # Gain 4 foods

scenario6end = pygame.image.load('images/backgrounds/scenarios/scenario6end.png') # Lost 2 foods
scenario6sur = pygame.image.load('images/backgrounds/scenarios/scenario6sur.png') # Nothing
# Special one
scenario7option1 = pygame.image.load('images/backgrounds/scenarios/scenario7option1.png')
scenario7option2 = pygame.image.load('images/backgrounds/scenarios/scenario7option2.png')
scenario7option3 = pygame.image.load('images/backgrounds/scenarios/scenario7option3.png')

scenario8end = pygame.image.load('images/backgrounds/scenarios/scenario8end.png')
scenario8sur = pygame.image.load('images/backgrounds/scenarios/scenario8sur.png')

scenario9end = pygame.image.load('images/backgrounds/scenarios/scenario9end.png')
scenario9sur = pygame.image.load('images/backgrounds/scenarios/scenario9sur.png')

scenario10end = pygame.image.load('images/backgrounds/scenarios/scenario10end.png')
scenario10sur = pygame.image.load('images/backgrounds/scenarios/scenario10sur.png')
# Another special one
scenario11option1 = pygame.image.load('images/backgrounds/scenarios/scenario11option1.png')
scenario11option2 = pygame.image.load('images/backgrounds/scenarios/scenario11option2.png')
scenario11option3 = pygame.image.load('images/backgrounds/scenarios/scenario11option3.png')
scenario11option4 = pygame.image.load('images/backgrounds/scenarios/scenario11option4.png')

########### Load character images

mizuki = pygame.image.load('images/character/mizuki.png')
mizuki = pygame.transform.scale(mizuki, (200, 300))
taylor = pygame.image.load('images/character/taylor.png')
talor = pygame.transform.scale(taylor, (200, 300))
cecilia = pygame.image.load('images/character/Cecilia.png')
cecilia = pygame.transform.scale(cecilia, (200, 300))
chingchong = pygame.image.load('images/character/chingchong.png')
chinngchong = pygame.transform.scale(chingchong, (100, 200))

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
        win.blit(taylor, (330, 270))
        win.blit(mizuki, (700, 320))
        win.blit(chingchong, (0, 290))
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
        if selection == "computer":
            win.blit(computer, (200, 280))
        if selection == "mask":
            win.blit(mask, (50, 100))
        if selection == "musket":
            win.blit(musket, (190, 30))
        if selection == "first_aid":
            win.blit(first_aid, (840, 500))

        if character == "ying":
            win.blit(chingchong, (430, 130))
        if character == "taylor":
            win.blit(taylor, (430, 130))
        if character == "mizuki":
            win.blit(mizuki, (500, 220))
        if character == "cecilia":
            win.blit(cecilia, (500, 220))

        button9.draw(win, (0, 0, 0))

        for counter in range(5):
            number = counter
            number = number + 280
            win.blit(coca, (number, 600))

        pygame.display.update()

    elif stages == "scenario":
        scenario = 11
        if scenario == 1:
            win.blit(scenario1, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 2:
            win.blit(scenario2, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 3:
            win.blit(scenario3, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 4:
            win.blit(scenario4, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 5:
            win.blit(scenario5, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 6:
            win.blit(scenario6, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 7:
            win.blit(scenario7, (300, 1))
            Button1.draw(win, (0, 0, 0))
            Button2.draw(win, (0, 0, 0))
            Button3.draw(win, (0, 0, 0))
        elif scenario == 8:
            win.blit(scenario8, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 9:
            win.blit(scenario9, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 10:
            win.blit(scenario10, (300, 1))
            yesButton.draw(win, (0, 0, 0))
            noButton.draw(win, (0, 0, 0))
        elif scenario == 11:
            win.blit(scenario11, (300, 1))
            Button1.draw(win, (0, 0, 0))
            Button2.draw(win, (0, 0, 0))
            Button3.draw(win, (0, 0, 0))
            Button4.draw(win, (0, 0, 0))
        pygame.display.update()

    elif stages == "result":
        scenario = 11
        if yesButton.isOver(mousePos) and scenario == 1:
            win.blit(scenario1end, (300, 1))
        if noButton.isOver(mousePos) and scenario == 1:
            win.blit(scenario1sur, (300, 1))

        if yesButton.isOver(mousePos) and scenario == 2:
            win.blit(scenario2end, (300, 1))
        if noButton.isOver(mousePos) and scenario == 2:
            win.blit(scenario2sur, (300, 1))

        if yesButton.isOver(mousePos) and scenario == 3:
            win.blit(scenario3end, (300, 1))
        if noButton.isOver(mousePos) and scenario == 3:
            win.blit(scenario3sur, (300, 1))

        if yesButton.isOver(mousePos) and scenario == 4:
            win.blit(scenario4end, (300, 1))
        if noButton.isOver(mousePos) and scenario == 4:
            win.blit(scenario4sur, (300, 1))

        if noButton.isOver(mousePos) and scenario == 5:
            win.blit(scenario5end, (300, 1))
        if yesButton.isOver(mousePos) and scenario == 5:
            win.blit(scenario5sur, (300, 1))

        if noButton.isOver(mousePos) and scenario == 6:
            win.blit(scenario6sur, (300, 1))
        if yesButton.isOver(mousePos) and scenario == 6:
            win.blit(scenario6end, (300, 1))

        if Button1.isOver(mousePos) and scenario == 7:
            win.blit(scenario7option1, (300, 1))
        if Button2.isOver(mousePos) and scenario == 7:
            win.blit(scenario7option2, (300, 1))
        if Button3.isOver(mousePos) and scenario == 7:
            win.blit(scenario7option3, (300, 1))

        if noButton.isOver(mousePos) and scenario == 8:
            win.blit(scenario8sur, (300, 1))
        if yesButton.isOver(mousePos) and scenario == 8:
            win.blit(scenario8end, (300, 1))

        if noButton.isOver(mousePos) and scenario == 9:
            win.blit(scenario9end, (300, 1))
        if yesButton.isOver(mousePos) and scenario == 9:
            win.blit(scenario9sur, (300, 1))

        if noButton.isOver(mousePos) and scenario == 10:
            win.blit(scenario10sur, (300, 1))
        if yesButton.isOver(mousePos) and scenario == 10:
            win.blit(scenario10end, (300, 1))

        if Button1.isOver(mousePos) and scenario == 11:
            win.blit(scenario11option1, (300, 1))
        if Button2.isOver(mousePos) and scenario == 11:
            win.blit(scenario11option2, (300, 1))
        if Button3.isOver(mousePos) and scenario == 11:
            win.blit(scenario11option3, (300, 1))
        if Button4.isOver(mousePos) and scenario == 11:
            win.blit(scenario11option4, (300, 1))

        pygame.display.update()


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

button9 = button((0, 255, 255), 1020, 580, 160, 80, "Scenario")

yesButton = button((0, 250, 154), 400, 530, 120, 100, "YES")
noButton = button((255, 69, 0), 700, 530, 120, 100, "NO")

Button1 = button((0, 255, 0), 430, 580, 60, 60, "1")
Button2 = button((0, 255, 0), 530, 580, 60, 60, "2")
Button3 = button((0, 255, 0), 630, 580, 60, 60, "3")
Button4 = button((0, 255, 0), 730, 580, 60, 60, "4")

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
                character = "ying"
                stages = "item"
            elif button2.isOver(mousePos) and stages == "character":
                player = Player(10, 10, 10, 20)
                print("You chose Taylor")
                character = "taylor"
                stages = "item"
            elif button3.isOver(mousePos) and stages == "character":
                player = Player(15, 15, 10, 10)
                print("You chose Mizuki")
                character = "mizuki"
                stages = "item"
            elif button4.isOver(mousePos) and stages == "character":
                player = Player(10, 10, 20, 10)
                print("You chose Cecilia")
                character = "cecilia"
                stages = "item"

            if button5.isOver(mousePos) and stages == "item":
                print("You got a computer")
                selection = 'computer'
                stages = "game"

            elif button6.isOver(mousePos) and stages == "item":
                print("You got a musket")
                selection = 'musket'
                stages = "game"

            elif button7.isOver(mousePos) and stages == "item":
                print("You got a mask")
                selection = 'mask'
                stages = "game"

            elif button8.isOver(mousePos) and stages == "item":
                print("You got first-aid kit")
                selection = 'first_aid'
                stages = "game"

            if button9.isOver(mousePos) and stages == "game":
                print("scenario clicked")
                stages = "scenario"

            if yesButton.isOver(mousePos) and stages == "scenario":
                print("Yes")
                stages = "result"
            if noButton.isOver(mousePos) and stages == "scenario":
                print("No")
                stages = "result"
            if Button1.isOver(mousePos) and stages == "scenario":
                print("1")
                stages = "result"
            if Button2.isOver(mousePos) and stages == "scenario":
                print("2")
                stages = "result"
            if Button3.isOver(mousePos) and stages == "scenario":
                print("3")
                stages = "result"
            if Button4.isOver(mousePos) and stages == "scenario":
                print("4")
                stages = "result"
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
