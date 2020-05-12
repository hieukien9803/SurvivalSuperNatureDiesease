import pygame

from user_interface.button import button
from user_interface import sound

from character.Hieu import Ying
from character.Taylor import Taylor
from character.Mizuki import Mizuki
from character.Cecilia import Cecilia
from character.Skeleton import Skeleton

from World import World

pygame.init()

# Load menu background images and set a size for them
menu_background = pygame.image.load('images/backgrounds/menu_background.png')
menu_background = pygame.transform.scale(menu_background, (1200, 700))
# Load help image
help = pygame.image.load('images/backgrounds/help.png')
help = pygame.transform.scale(help, (600, 600))
# Load game background images and set a size for them
game_background = pygame.image.load('images/backgrounds/game_background.png')
game_background = pygame.transform.scale(game_background, (1200, 710))
game_background_rain = pygame.image.load('images/backgrounds/game_background_rain.png')
game_background_rain = pygame.transform.scale(game_background_rain, (1200, 710))
game_background_snow = pygame.image.load('images/backgrounds/game_background_snow.png')
game_background_snow = pygame.transform.scale(game_background_snow, (1200, 710))
the_end = pygame.image.load('images/backgrounds/theEnd.png')
# Load game bar images and set a size for them
drumStick = pygame.image.load('images/backgrounds/bar/drumstick.png')
drumStick = pygame.transform.scale(drumStick, (40, 50))
Water = pygame.image.load('images/backgrounds/bar/water.png')
Water = pygame.transform.scale(Water, (30, 50))
smile = pygame.image.load('images/backgrounds/bar/smile.png')
smile = pygame.transform.scale(smile, (45, 45))
bar = pygame.image.load('images/backgrounds/bar/statusBar.png')
bar = pygame.transform.scale(bar, (400, 200))
# Load character background images and set a size for them
character_background = pygame.image.load('images/backgrounds/character_background/character_background.png')
character_background = pygame.transform.scale(character_background, (1200, 700))
text1 = pygame.image.load('images/backgrounds/character_background/text1.png')
text1 = pygame.transform.scale(text1, (200, 100))
text2 = pygame.image.load('images/backgrounds/character_background/text2.png')
text2 = pygame.transform.scale(text2, (230, 100))
text3 = pygame.image.load('images/backgrounds/character_background/text3.png')
text3 = pygame.transform.scale(text3, (250, 100))
text4 = pygame.image.load('images/backgrounds/character_background/text4.png')
text4 = pygame.transform.scale(text4, (260, 120))
# Load item background images and set a size for them
item_background = pygame.image.load('images/backgrounds/item_background/item_background.png')
item_background = pygame.transform.scale(item_background, (1200, 1053))
text5 = pygame.image.load('images/backgrounds/item_background/text5.png')
text5 = pygame.transform.scale(text5, (250, 420))
# Load day background images and set a size for them
day1 = pygame.image.load('images/backgrounds/day/day1.png')
day1 = pygame.transform.scale(day1, (1200, 800))
day2 = pygame.image.load('images/backgrounds/day/day2.png')
day2 = pygame.transform.scale(day2, (1200, 800))
day3 = pygame.image.load('images/backgrounds/day/day3.png')
day3 = pygame.transform.scale(day3, (1200, 800))
day4 = pygame.image.load('images/backgrounds/day/day4.png')
day4 = pygame.transform.scale(day4, (1200, 800))
day5 = pygame.image.load('images/backgrounds/day/day5.png')
day5 = pygame.transform.scale(day5, (1200, 800))
day6 = pygame.image.load('images/backgrounds/day/day6.png')
day6 = pygame.transform.scale(day6, (1200, 800))
day7 = pygame.image.load('images/backgrounds/day/day7.png')
day7 = pygame.transform.scale(day7, (1200, 800))
day8 = pygame.image.load('images/backgrounds/day/day8.png')
day8 = pygame.transform.scale(day8, (1200, 800))
day9 = pygame.image.load('images/backgrounds/day/day9.png')
day9 = pygame.transform.scale(day9, (1200, 800))
day10 = pygame.image.load('images/backgrounds/day/day10.png')
day10 = pygame.transform.scale(day10, (1200, 800))
day11 = pygame.image.load('images/backgrounds/day/day11.png')
day11 = pygame.transform.scale(day11, (1200, 800))
# Load scenario images
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
# Load scenario's results images
scenario1end = pygame.image.load('images/backgrounds/scenarios/scenario1end.png')  # Dead
scenario1sur = pygame.image.load('images/backgrounds/scenarios/scenario1sur.png')  # Nothing
scenario2end = pygame.image.load('images/backgrounds/scenarios/scenario2end.png')  # Dead
scenario2sur = pygame.image.load('images/backgrounds/scenarios/scenario2sur.png')  # Nothing
scenario3end = pygame.image.load('images/backgrounds/scenarios/scenario3end.png')  # Nothing
scenario3sur = pygame.image.load('images/backgrounds/scenarios/scenario3sur.png')  # Lost all the food
scenario4end = pygame.image.load('images/backgrounds/scenarios/scenario4end.png')  # Dead
scenario4sur = pygame.image.load('images/backgrounds/scenarios/scenario4sur.png')  # Nothing
scenario5end = pygame.image.load('images/backgrounds/scenarios/scenario5end.png')  # Nothing
scenario5sur = pygame.image.load('images/backgrounds/scenarios/scenario5sur.png')  # Gain 4 foods
scenario6end = pygame.image.load('images/backgrounds/scenarios/scenario6end.png')  # Lost 2 foods
scenario6sur = pygame.image.load('images/backgrounds/scenarios/scenario6sur.png')  # Nothing
scenario7option1 = pygame.image.load('images/backgrounds/scenarios/scenario7option1.png')  # Nothing
scenario7option2 = pygame.image.load('images/backgrounds/scenarios/scenario7option2.png')  # Dead
scenario7option3 = pygame.image.load('images/backgrounds/scenarios/scenario7option3.png')  # Dead
scenario8end = pygame.image.load('images/backgrounds/scenarios/scenario8end.png')
scenario8sur = pygame.image.load('images/backgrounds/scenarios/scenario8sur.png')
scenario9end = pygame.image.load('images/backgrounds/scenarios/scenario9end.png')
scenario9sur = pygame.image.load('images/backgrounds/scenarios/scenario9sur.png')
scenario10end = pygame.image.load('images/backgrounds/scenarios/scenario10end.png')
scenario10sur = pygame.image.load('images/backgrounds/scenarios/scenario10sur.png')
scenario11option1 = pygame.image.load('images/backgrounds/scenarios/scenario11option1.png')
scenario11option2 = pygame.image.load('images/backgrounds/scenarios/scenario11option2.png')
scenario11option3 = pygame.image.load('images/backgrounds/scenarios/scenario11option3.png')
scenario11option4 = pygame.image.load('images/backgrounds/scenarios/scenario11option4.png')
# Load character images and set a size for them
mizuki = pygame.image.load('images/character/mizuki.png')
mizuki = pygame.transform.scale(mizuki, (200, 300))
taylor = pygame.image.load('images/character/taylor.png')
taylor = pygame.transform.scale(taylor, (300, 300))
cecilia = pygame.image.load('images/character/Cecilia.png')
cecilia = pygame.transform.scale(cecilia, (200, 300))
ying = pygame.image.load('images/character/chingchong.png')
ying = pygame.transform.scale(ying, (300, 300))
skeleton = pygame.image.load('images/character/skeleton.png')
skeleton = pygame.transform.scale(skeleton, (200, 300))
# Load foods images and set a size for them
pizza = pygame.image.load('images/foods/pizza.png')
pizza = pygame.transform.scale(pizza, (120, 110))
banana = pygame.image.load('images/foods/banana.png')
banana = pygame.transform.scale(banana, (120, 110))
burger = pygame.image.load('images/foods/burger.png')
burger = pygame.transform.scale(burger, (60, 55))
ham = pygame.image.load('images/foods/ham.png')
ham = pygame.transform.scale(ham, (120, 110))
sushi = pygame.image.load('images/foods/sushi.png')
sushi = pygame.transform.scale(sushi, (120, 110))
tuna = pygame.image.load('images/foods/tuna_can.png')
tuna = pygame.transform.scale(tuna, (120, 110))
# Load drinks images and set a size for them
beer = pygame.image.load('images/drinks/beer.png')
beer = pygame.transform.scale(beer, (120, 110))
bubble = pygame.image.load('images/drinks/bubble_tea.png')
bubble = pygame.transform.scale(bubble, (120, 110))
coca = pygame.image.load('images/drinks/coca.png')
coca = pygame.transform.scale(coca, (45, 50))
coffee = pygame.image.load('images/drinks/coffee.png')
coffee = pygame.transform.scale(coffee, (120, 110))
milk = pygame.image.load('images/drinks/milk.png')
milk = pygame.transform.scale(milk, (120, 110))
water = pygame.image.load('images/drinks/water.png')
water = pygame.transform.scale(water, (120, 110))
wine = pygame.image.load('images/drinks/wine.png')
wine = pygame.transform.scale(wine, (120, 110))
# Load items images and set a size for them
computer = pygame.image.load('images/items/computer.png')
computer = pygame.transform.scale(computer, (160, 150))
first_aid = pygame.image.load('images/items/first_aid.png')
first_aid = pygame.transform.scale(first_aid, (180, 150))
mask = pygame.image.load('images/items/mask.png')
mask = pygame.transform.scale(mask, (100, 100))
musket = pygame.image.load('images/items/musket.png')
musket = pygame.transform.scale(musket, (130, 120))
# Create a window
winWidth = 1200
winHeight = 700
win = pygame.display.set_mode((winWidth, winHeight))
# Create a caption
pygame.display.set_caption("Epidemic")
# Create all the button
# Menu buttons
startButton = button((0, 255, 255), 450, 400, 300, 100, "Start")
quitButton = button((0, 255, 255), 450, 520, 300, 60, "Quit")
# Help button
helpButton = button((0, 255, 255), 1120, 20, 60, 60, "?")
# Character buttons
button1 = button((0, 255, 255), 100, 550, 120, 60, "Ying")
button2 = button((0, 255, 255), 400, 550, 120, 60, "Taylor")
button3 = button((0, 255, 255), 700, 550, 120, 60, "Mizuki")
button4 = button((0, 255, 255), 1000, 550, 120, 60, "Cecilia")
# Item buttons
button5 = button((0, 255, 255), 300, 270, 175, 60, "Computer")
button6 = button((0, 255, 255), 600, 270, 130, 60, "Musket")
button7 = button((0, 255, 255), 300, 570, 120, 60, "Mask")
button8 = button((0, 255, 255), 600, 570, 150, 60, "First-Aid")
# Next day button
nextButton = button((0, 255, 0), 550, 550, 60, 60, ">")
# Game buttons
button9 = button((0, 255, 255), 1020, 610, 160, 80, "Today")
button10 = button((0, 255, 255), 1020, 520, 160, 80, "Yesterday")
# Back button
button11 = button((0, 255, 255), 1020, 430, 160, 80, "Back")
backButton2 = button((0, 255, 255), 760, 530, 50, 50, ">")
# the end button in the game
theEnd = button((0, 255, 255), 580, 600, 100, 34, "Quit")
# take button in the game
takeButton = button((0, 255, 255), 1020, 340, 160, 80, "Take")
# Eat, Drink, and Play button
eatButton = button((0, 255, 255), 20, 430, 160, 80, "Eat")
drinkButton = button((0, 255, 255), 20, 520, 160, 80, "Drink")
playButton = button((0, 255, 255), 20, 610, 160, 80, "Play")
# Scenario buttons for T/F questions
yesButton = button((0, 250, 154), 400, 530, 120, 100, "YES")
noButton = button((255, 69, 0), 700, 530, 120, 100, "NO")
# Scenario buttons for Multiple choices questions
Button1 = button((0, 255, 0), 430, 580, 60, 60, "1")
Button2 = button((0, 255, 0), 530, 580, 60, 60, "2")
Button3 = button((0, 255, 0), 630, 580, 60, 60, "3")
Button4 = button((0, 255, 0), 730, 580, 60, 60, "4")
# item button
first_aid_button = button((0, 255, 255), 1030, 200, 160, 34, "First-Aid")
musketButton = button((0, 255, 255), 1040, 240, 150, 34, "Musket")
maskButton = button((0, 255, 255), 1040, 280, 150, 34, "Mask")


class Game(object):

    def __init__(self):
        self.__world = World()
        self.__menu = 'main'
        # Character
        self.__ying = Ying(5, 6, 5)
        self.__taylor = Taylor(6, 6, 5)
        self.__mizuki = Mizuki(7, 7, 4)
        self.__cecilia = Cecilia(5, 5, 6)
        self.__skeleton = Skeleton(0, 0, 0)
        self.__character = None
        self.__boolean = None
        # Food and drink to start
        self.__foods = 4
        self.__drinks = 5
        # Inventory
        self.__musket = 0
        self.__firstAid = 0
        self.__computer = 0
        self.__gas = 0
        # Value for running the game
        self.__time = 0
        self.__exist = False
        self.__isNumber2 = None
        self.__special = None
        self.__electricity = True

    def main(self):
        """This is the main game loop"""
        run = True
        stages = "menu"
        self.status()
        while run:
            Game.drawWin(self, stages)
            for event in pygame.event.get():
                mousePos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startButton.isOver(mousePos) and stages == 'menu':
                        sound.button_sound()
                        print("clicked")
                        stages = "character"
                        self.drawWin(stages)

                    if stages == "character":
                        if button1.isOver(mousePos):
                            sound.button_sound()
                            print("You chose Ying")
                            self.__character = self.__ying
                            stages = "item"
                        elif button2.isOver(mousePos):
                            sound.button_sound()
                            print("You chose Taylor")
                            self.__character = self.__taylor
                            stages = "item"
                        elif button3.isOver(mousePos):
                            sound.button_sound()
                            print("You chose Mizuki")
                            self.__character = self.__mizuki
                            stages = "item"
                        elif button4.isOver(mousePos):
                            sound.button_sound()
                            print("You chose Cecilia")
                            self.__character = self.__cecilia
                            stages = "item"
                        else:
                            self.drawWin(stages)

                    if stages == 'item':
                        self.__character.get_hunger()
                        self.__character.get_thirst()
                        self.__character.get_happiness()
                        self.__character.__str__()
                        if button5.isOver(mousePos):
                            sound.button_sound()
                            print("You got a computer")
                            self.__computer = self.__computer + 1
                            stages = "nextDay"
                        elif button6.isOver(mousePos):
                            sound.button_sound()
                            print("You got a musket")
                            self.__musket = self.__musket + 1
                            stages = "nextDay"
                        elif button7.isOver(mousePos):
                            sound.button_sound()
                            print("You got a mask")
                            self.__gas = self.__gas + 1
                            stages = "nextDay"
                        elif button8.isOver(mousePos):
                            sound.button_sound()
                            print("You got first-aid kit")
                            self.__firstAid = self.__firstAid + 1
                            stages = "nextDay"
                        else:
                            self.drawWin(stages)

                    if stages == 'scenario':
                        if yesButton.isOver(mousePos):
                            self.__boolean = 'Yes'
                            sound.button_sound()
                            print("Yes")
                            stages = 'nextDay'

                        elif noButton.isOver(mousePos):
                            sound.button_sound()
                            print("No")
                            stages = 'nextDay'
                            self.__boolean = 'No'
                        if Button1.isOver(mousePos) and (self.__world.get_scenario() == 7
                                                         or self.__world.get_scenario() == 11):
                            sound.button_sound()
                            print("1")
                            stages = 'nextDay'
                            self.__boolean = 'No'

                        elif Button2.isOver(mousePos) and (self.__world.get_scenario() == 7
                                                           or self.__world.get_scenario() == 11):
                            sound.button_sound()
                            print("2")
                            stages = 'nextDay'
                            self.__boolean = 'Yes'
                            self.__isNumber2 = True
                        elif Button3.isOver(mousePos) and (self.__world.get_scenario() == 7
                                                           or self.__world.get_scenario() == 11):
                            sound.button_sound()
                            print("3")
                            stages = 'nextDay'
                            self.__boolean = 'Yes'
                        elif Button4.isOver(mousePos) and (self.__world.get_scenario() == 7
                                                           or self.__world.get_scenario() == 11):
                            sound.button_sound()
                            print("4")
                            stages = 'nextDay'
                            self.__boolean = 'Yes'
                        self.status()
                    if nextButton.isOver(mousePos) and stages == "nextDay":
                        sound.button_sound()
                        print("continued")
                        self.__world.next_scenario()
                        self.__world.next_day()

                        self.__character.hungry()
                        self.__character.thirsty()
                        self.__character.bored()
                        print(self.__character.__str__())
                        self.status()
                        stages = "game"
                        self.drawWin(stages)
                    if takeButton.isOver(mousePos) and stages == "game":
                        if self.__special:
                            sound.button_sound()
                            if self.__world.get_scenario() == 6 and self.__time > 0:
                                self.__foods = self.__foods + 2
                                self.__drinks = self.__drinks + 2
                                self.__time = self.__time - 1
                            if self.__world.get_scenario() == 7 and self.__time > 0:
                                self.__foods = self.__foods - 2
                                self.__time = self.__time - 1
                            if self.__world.get_scenario() == 10 and self.__time > 0:
                                self.__firstAid = self.__firstAid + 1
                                self.__time = self.__time - 1
                        else:
                            print("You didn't receive anything")
                    if button9.isOver(mousePos):
                        if self.__character == self.__skeleton:
                            stages = "theEnd"
                        elif self.__exist and self.__time == 0 and (stages == "game" or stages == "scenario"
                                                                    or stages == "endResult" or stages == "surResult"):
                            sound.page_sound()
                            print("scenario clicked")
                            stages = "scenario"
                        elif not self.__exist:
                            print("You have to see what happened yesterday")
                        elif self.__time > 0:
                            print("You have to click the take button first")
                        self.__special = False
                        self.status()

                    if button10.isOver(mousePos) and (stages == "game" or stages == "scenario"
                                                      or stages == "endResult" or stages == "surResult"):
                        sound.page_sound()
                        print("result showed")

                        if self.__boolean == 'Yes':
                            stages = "endResult"
                        elif self.__boolean == 'No':
                            stages = "surResult"
                        if self.__world.get_scenario() == 1:
                            pygame.mixer_music.load('user_interface/sounds/night.wav')
                            pygame.mixer_music.play(-1)
                        if self.__world.get_scenario() == 7:
                            pygame.mixer_music.stop()
                        if self.__world.get_scenario() == 8:
                            pygame.mixer_music.load('user_interface/sounds/rain.wav')
                            pygame.mixer_music.play(-1)
                        if self.__world.get_scenario() == 10:
                            pygame.mixer_music.stop()

                        self.status()
                        self.__exist = True
                        self.drawWin(stages)
                    if button11.isOver(mousePos) and (stages == "game" or stages == "scenario"
                                                      or stages == "endResult" or stages == "surResult"):
                        sound.page_sound()
                        print("backed")
                        self.status()
                        stages = "game"

                    if backButton2.isOver(mousePos) and stages == "help":
                        sound.button_sound()
                        print("backed")
                        stages = 'menu'
                        self.drawWin(stages)

                    # Player Button
                    if eatButton.isOver(mousePos) and stages == 'game':
                        if self.__foods > 0 and self.__time == 0 and self.__exist:
                            sound.button_sound()
                            if self.__character.get_hunger() == 6:
                                print("You are already full")
                            else:
                                self.__character.eat()
                                sound.eat_sound()
                                print("Plus 1 eat point")
                                self.__foods = self.__foods - 1
                                self.drawWin(stages)
                                print(self.__character.__str__())
                        elif not self.__exist:
                            print("You have to check yesterday scenario result first")
                        elif self.__time > 0:
                            print("You have to click take button first")
                        else:
                            print('You dont have any foods left')

                    if drinkButton.isOver(mousePos) and stages == 'game':
                        if self.__drinks > 0 and self.__time == 0 and self.__exist == True:
                            sound.button_sound()
                            if self.__character.get_thirst() == 6:
                                print("You are already full")
                            else:
                                sound.drink_sound()
                                self.__character.drink()
                                print("Plus 1 drink point")
                                self.__drinks = self.__drinks - 1
                                self.drawWin(stages)
                                print(self.__character.__str__())
                        elif not self.__exist:
                            print("You have to check yesterday scenario result first")
                        elif self.__time > 0:
                            print("You have to click take button first")
                        else:
                            print('You dont have any drinks left')

                    if playButton.isOver(mousePos) and stages == 'game':
                        if self.__computer > 0 and self.__electricity == True and self.__time == 0 and self.__exist == True:
                            sound.button_sound()
                            if self.__character.get_happiness() == 5:
                                print("You are already full")
                            else:
                                sound.playSound()
                                self.__character.play()
                                print("Plus 1 happiness")
                                self.drawWin(stages)
                                print(self.__character.__str__())
                        elif not self.__exist:
                            print("You have to check yesterday scenario result first")
                        elif self.__time > 0:
                            print("You have to click take button first")
                        else:
                            print('You need a computer and power in order to play games')

                    if quitButton.isOver(mousePos) and stages == 'menu':
                        sound.button_sound()
                        print("quit")
                        run = False
                        pygame.quit()
                        quit()
                    if helpButton.isOver(mousePos) and (stages == "menu" or stages == "game"):
                        sound.button_sound()
                        print("help")
                        stages = "help"

                    if theEnd.isOver(mousePos) and stages == 'theEnd':
                        sound.button_sound()
                        print("quit")
                        run = False
                        pygame.quit()
                        quit()
                    if first_aid_button.isOver(mousePos):
                        if self.__firstAid > 0 and stages == "scenario":
                            sound.button_sound()
                            # self.__firstAid = self.__firstAid - 1
                        elif stages != "scenario":
                            sound.button_sound()
                            print("You need to be in a scenario")
                        else:
                            sound.button_sound()
                            print("You have no first-aid kit")

                    if musketButton.isOver(mousePos):
                        if self.__musket > 0 and stages == "scenario":
                            sound.button_sound()
                            # self.__musket = self.__musket - 1
                        elif stages != "scenario":
                            sound.button_sound()
                            print("You need to be in a scenario")
                        else:
                            sound.button_sound()
                            print("You have no musket")

                    if maskButton.isOver(mousePos):
                        if self.__gas > 0 and stages == "scenario":
                            sound.button_sound()
                            # self.__gas = self.__gas - 1
                        elif stages != "scenario":
                            sound.button_sound()
                            print("You need to be in a scenario")
                        else:
                            sound.button_sound()
                            print("You have no mask")

                # Change the color of the button if the mouse position is over the button
                if event.type == pygame.MOUSEMOTION:
                    if startButton.isOver(mousePos) and stages == "menu":
                        startButton.color = (255, 0, 0)
                    else:
                        startButton.color = 0, 255, 255

                    if quitButton.isOver(mousePos) and stages == "menu":
                        quitButton.color = (255, 0, 0)
                    else:
                        quitButton.color = 0, 255, 255

                    if button1.isOver(mousePos) and stages == "character":
                        button1.color = (255, 0, 0)
                    else:
                        button1.color = 0, 255, 255

                    if button2.isOver(mousePos) and stages == "character":
                        button2.color = (255, 0, 0)
                    else:
                        button2.color = 0, 255, 255

                    if button3.isOver(mousePos) and stages == "character":
                        button3.color = (255, 0, 0)
                    else:
                        button3.color = 0, 255, 255

                    if button4.isOver(mousePos) and stages == "character":
                        button4.color = (255, 0, 0)
                    else:
                        button4.color = 0, 255, 255

                    if button5.isOver(mousePos) and stages == "item":
                        button5.color = (255, 0, 0)
                    else:
                        button5.color = 0, 255, 255

                    if button6.isOver(mousePos) and stages == "item":
                        button6.color = (255, 0, 0)
                    else:
                        button6.color = 0, 255, 255

                    if button7.isOver(mousePos) and stages == "item":
                        button7.color = (255, 0, 0)
                    else:
                        button7.color = 0, 255, 255

                    if button8.isOver(mousePos) and stages == "item":
                        button8.color = (255, 0, 0)
                    else:
                        button8.color = 0, 255, 255

                    if button9.isOver(mousePos) and stages == "game":
                        button9.color = (220, 20, 60)
                    else:
                        button9.color = (250, 128, 114)

                    if Button1.isOver(mousePos) and stages == "scenario":
                        Button1.color = (60, 179, 113)
                    else:
                        Button1.color = (0, 250, 154)

                    if Button2.isOver(mousePos) and stages == "scenario":
                        Button2.color = (60, 179, 113)
                    else:
                        Button2.color = (0, 250, 154)

                    if Button3.isOver(mousePos) and stages == "scenario":
                        Button3.color = (60, 179, 113)
                    else:
                        Button3.color = (0, 250, 154)

                    if Button4.isOver(mousePos) and stages == "scenario":
                        Button4.color = (60, 179, 113)
                    else:
                        Button4.color = (0, 250, 154)

                    if noButton.isOver(mousePos) and stages == "scenario":
                        noButton.color = (139, 0, 0)
                    else:
                        noButton.color = (255, 69, 0)

                    if yesButton.isOver(mousePos) and stages == "scenario":
                        yesButton.color = (60, 179, 113)
                    else:
                        yesButton.color = (0, 250, 154)

                    if nextButton.isOver(mousePos) and stages == "nextDay":
                        nextButton.color = (139, 0, 139)
                    else:
                        nextButton.color = (186, 85, 211)

                    if button10.isOver(mousePos) and stages == "game":
                        button10.color = (220, 20, 60)
                    else:
                        button10.color = (250, 128, 114)

                    if button11.isOver(mousePos) and stages == "game":
                        button11.color = (220, 20, 60)
                    else:
                        button11.color = (250, 128, 114)

                    if helpButton.isOver(mousePos) and (stages == "menu" or stages == "game"):
                        helpButton.color = (220, 20, 60)
                    else:
                        helpButton.color = (250, 128, 114)

                    if eatButton.isOver(mousePos) and stages == "game":
                        eatButton.color = (220, 20, 60)
                    else:
                        eatButton.color = (250, 128, 114)

                    if drinkButton.isOver(mousePos) and stages == "game":
                        drinkButton.color = (220, 20, 60)
                    else:
                        drinkButton.color = (250, 128, 114)

                    if playButton.isOver(mousePos) and stages == "game":
                        playButton.color = (220, 20, 60)
                    else:
                        playButton.color = (250, 128, 114)

                    if backButton2.isOver(mousePos):
                        backButton2.color = (220, 20, 60)
                    else:
                        backButton2.color = (250, 128, 114)

                    if theEnd.isOver(mousePos):
                        theEnd.color = (220, 20, 60)
                    else:
                        theEnd.color = (250, 128, 114)

                    if first_aid_button.isOver(mousePos):
                        first_aid_button.color = (220, 20, 60)
                    else:
                        first_aid_button.color = (250, 128, 114)

                    if musketButton.isOver(mousePos):
                        musketButton.color = (220, 20, 60)
                    else:
                        musketButton.color = (250, 128, 114)

                    if maskButton.isOver(mousePos):
                        maskButton.color = (220, 20, 60)
                    else:
                        maskButton.color = (250, 128, 114)

                    if takeButton.isOver(mousePos):
                        takeButton.color = (220, 20, 60)
                    else:
                        takeButton.color = (250, 128, 114)

    def status(self):
        """Print our a string representing the status of the world"""
        day = self.__world.get_day()
        scenario = self.__world.get_scenario()
        string = 'Status:   '
        string += f'day: {day}'
        string += f'     scenario: {scenario}'
        print(string)

    def drawWin(self, stages):
        """
        Draw the images for the window
        :param stages: the current window
        :return: None
        """
        # Draw the menu window
        if stages == 'menu':
            win.blit(menu_background, (0, 0))
            startButton.draw(win, (0, 0, 0))
            quitButton.draw(win, (0, 0, 0))
            helpButton.draw(win, (0, 0, 0))
        # Draw the choosing character window
        elif stages == "character":
            win.blit(character_background, (0, 0))
            win.blit(text1, (60, 170))
            win.blit(text2, (350, 170))
            win.blit(text3, (630, 170))
            win.blit(text4, (900, 170))
            win.blit(cecilia, (970, 320))
            win.blit(taylor, (330, 270))
            win.blit(mizuki, (700, 320))
            win.blit(ying, (0, 290))
            button1.draw(win, (0, 0, 0))
            button2.draw(win, (0, 0, 0))
            button3.draw(win, (0, 0, 0))
            button4.draw(win, (0, 0, 0))
        # Draw the choosing item window
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
        # Draw the game window
        elif stages == "game":
            if not self.__electricity:
                win.blit(game_background_rain, (0, 0))
            else:
                win.blit(game_background, (0, 0))
            # Draw the foods and drinks available
            for i in range(self.__computer):
                win.blit(computer, (120 + (i * 158), 280))
            for i in range(self.__musket):
                win.blit(musket, (700 + (i * 60), 470))
            for i in range(self.__gas):
                win.blit(mask, (180 + (i * 80), 480))
            for i in range(self.__firstAid):
                win.blit(first_aid, (700 + (i * 100), 570))
            # The status bar for hunger, thirst, and happiness
            win.blit(bar, (5, 5))
            # Draw the foods and drinks available
            if self.__foods > 0:
                for i in range(self.__foods):
                    win.blit(burger, (115 + (i * 40), 387))
            if self.__drinks > 0:
                for i in range(self.__drinks):
                    win.blit(coca, (790 + (i * 30), 240))
            # Draw the hunger point, thirst point, and happiness point
            if self.__character.get_hunger() > 0:
                for i in range(self.__character.get_hunger()):
                    win.blit(drumStick, (90 + (i * 50), 15))
            elif self.__character.get_hunger() == 0:
                self.__character = self.__skeleton

            if self.__character.get_thirst() > 0:
                for i in range(self.__character.get_thirst()):
                    win.blit(Water, (115 + (i * 45), 81))
            elif self.__character.get_thirst() == 0:
                self.__character = self.__skeleton

            if self.__character.get_happiness() > 0:
                for i in range(self.__character.get_happiness()):
                    win.blit(smile, (150 + (i * 50), 151))
            elif self.__character.get_happiness() == 0:
                self.__character = self.__skeleton
            # Draw the character
            if self.__character == self.__ying:
                win.blit(ying, (430, 130))
            if self.__character == self.__taylor:
                win.blit(taylor, (430, 130))
            if self.__character == self.__mizuki:
                win.blit(mizuki, (500, 220))
            if self.__character == self.__cecilia:
                win.blit(cecilia, (500, 220))
            if self.__character == self.__skeleton:
                win.blit(skeleton, (480, 220))
            # Draw the button
            button9.draw(win, (0, 0, 0))
            button10.draw(win, (0, 0, 0))
            button11.draw(win, (0, 0, 0))
            eatButton.draw(win, (0, 0, 0))
            drinkButton.draw(win, (0, 0, 0))
            playButton.draw(win, (0, 0, 0))
            first_aid_button.draw(win, (0, 0, 0))
            maskButton.draw(win, (0, 0, 0))
            musketButton.draw(win, (0, 0, 0))
            takeButton.draw(win, (0, 0, 0))
        # Draw the scenario
        elif stages == "scenario":
            if self.__world.get_scenario() == 1:
                win.blit(scenario1, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 2:
                win.blit(scenario2, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 3:
                win.blit(scenario3, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 4:
                win.blit(scenario4, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 5:
                win.blit(scenario5, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 6:
                win.blit(scenario6, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 7:
                win.blit(scenario7, (300, 1))
                Button1.draw(win, (0, 0, 0))
                Button2.draw(win, (0, 0, 0))
                Button3.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 8:
                win.blit(scenario8, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 9:
                win.blit(scenario9, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 10:
                win.blit(scenario10, (300, 1))
                yesButton.draw(win, (0, 0, 0))
                noButton.draw(win, (0, 0, 0))
            elif self.__world.get_scenario() == 11:
                win.blit(scenario11, (300, 1))
                Button1.draw(win, (0, 0, 0))
                Button2.draw(win, (0, 0, 0))
                Button3.draw(win, (0, 0, 0))
                Button4.draw(win, (0, 0, 0))
        # Draw the status day
        elif stages == "nextDay":
            if self.__world.get_day() == 0:
                win.blit(day1, (0, 0))
            elif self.__world.get_day() == 1:
                win.blit(day2, (0, 0))
            elif self.__world.get_day() == 2:
                win.blit(day3, (0, 0))
            elif self.__world.get_day() == 3:
                win.blit(day4, (0, 0))
            elif self.__world.get_day() == 4:
                win.blit(day5, (0, 0))
            elif self.__world.get_day() == 5:
                win.blit(day6, (0, 0))
            elif self.__world.get_day() == 6:
                win.blit(day7, (0, 0))
            elif self.__world.get_day() == 7:
                win.blit(day8, (0, 0))
            elif self.__world.get_day() == 8:
                win.blit(day9, (0, 0))
            elif self.__world.get_day() == 9:
                win.blit(day10, (0, 0))
            elif self.__world.get_day() == 10:
                win.blit(day11, (0, 0))
            self.__exist = False
            # Draw the button
            nextButton.draw(win, (0, 0, 0))
        # Draw the End Result for the scenario
        elif stages == "endResult":
            """Displaying the end result of the scenario"""
            # Scenario 1
            if self.__world.get_scenario() == 2:
                win.blit(scenario1end, (300, 1))
                self.__character = self.__skeleton
            # Scenario 2
            if self.__world.get_scenario() == 3:
                win.blit(scenario2end, (300, 1))
                self.__character = self.__skeleton
            # Scenario 3
            if self.__world.get_scenario() == 4:
                win.blit(scenario3end, (300, 1))
                self.__foods = self.__foods - self.__foods
            # Scenario 4
            if self.__world.get_scenario() == 5:
                win.blit(scenario4end, (300, 1))
                self.__character = self.__skeleton
            # Scenario 5
            if self.__world.get_scenario() == 6:
                win.blit(scenario5sur, (300, 1))
                self.__special = True
                self.__time = 1
            # Scenario 6
            if self.__world.get_scenario() == 7:
                win.blit(scenario6end, (300, 1))
                self.__special = True
                self.__time = 1
            # Scenario 7
            if self.__world.get_scenario() == 8 and self.__isNumber2:
                win.blit(scenario7option2, (300, 1))
                self.__character = self.__skeleton
            elif self.__world.get_scenario() == 8:
                win.blit(scenario7option3, (300, 1))
                self.__character = self.__skeleton
            # Scenario 8
            if self.__world.get_scenario() == 9:
                win.blit(scenario8end, (300, 1))
                self.__character = self.__skeleton
            # Scenario 9
            if self.__world.get_scenario() == 10:
                win.blit(scenario9sur, (300, 1))
                self.__special = True
                self.__time = 1
            # Scenario 10
            if self.__world.get_scenario() == 11:
                win.blit(scenario10end, (300, 1))
                self.__foods = self.__foods - 1
                self.__drinks = self.__drinks - 1
            # Scenario 11
            if self.__world.get_scenario() == 12:
                win.blit(scenario11option1, (300, 1))
            if self.__world.get_scenario() == 12:
                win.blit(scenario11option2, (300, 1))
            if self.__world.get_scenario() == 12:
                win.blit(scenario11option3, (300, 1))
            if self.__world.get_scenario() == 12:
                win.blit(scenario11option4, (300, 1))
        # Draw the Survived Result for the scenario
        elif stages == "surResult":
            """Displaying the survive result of the scenario"""
            if self.__world.get_scenario() == 2:
                win.blit(scenario1sur, (300, 1))
            if self.__world.get_scenario() == 3:
                win.blit(scenario2sur, (300, 1))
            if self.__world.get_scenario() == 4:
                win.blit(scenario3sur, (300, 1))
            if self.__world.get_scenario() == 5:
                win.blit(scenario4sur, (300, 1))
            if self.__world.get_scenario() == 6:
                win.blit(scenario5end, (300, 1))
            if self.__world.get_scenario() == 7:
                win.blit(scenario6sur, (300, 1))
            if self.__world.get_scenario() == 8:
                win.blit(scenario7option1, (300, 1))
            if self.__world.get_scenario() == 9:
                win.blit(scenario8sur, (300, 1))
                self.__electricity = False
            if self.__world.get_scenario() == 10:
                win.blit(scenario9end, (300, 1))
            if self.__world.get_scenario() == 11:
                win.blit(scenario10sur, (300, 1))
        # Draw help window
        elif stages == "help":
            win.blit(help, (300, 40))
            backButton2.draw(win, (0, 0, 0))
        # Draw the end window
        elif stages == "theEnd":
            win.blit(the_end, (270, 5))
            theEnd.draw(win, (0, 0, 0))
        # Update the display
        pygame.display.update()


# Run the main game
if __name__ == '__main__':
    game = Game()
    game.main()
