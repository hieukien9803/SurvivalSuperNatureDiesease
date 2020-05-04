import pygame
import winsound
pygame.init()

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        """Draw a button with a text"""
        # This is the information far the button and the outline
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        # This is the information for the text inside of the button
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, position):
        # This function will check if the mouse is on top of the button
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True

        return False


# This is a small test for the button
def drawWin():
    win.fill((255, 255, 255))
    startButton.draw(win, (0, 0, 0))
    quitButton.draw(win, (0, 0, 0))


#background = pygame.image.load('background.png')

pygame.display.set_caption("Super Nature Disease")
winWidth = 1700
winHeight = 900
win = pygame.display.set_mode((winWidth, winHeight))
win.fill((255, 255, 255))

run = True
startButton = button((0, 255, 255), 300, 200, 300, 100, "Start")
quitButton = button((0, 255, 255), 300, 320, 300, 60, "Quit")
#winsound.PlaySound("gameMusic", winsound.SND_FILENAME)
while run:
    drawWin()
    pygame.display.update()
    # Check the event for the button

    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(mousePos):
                print("clicked")

            if quitButton.isOver(mousePos):
                print("quit")
                run = False
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEMOTION:
            if startButton.isOver(mousePos):
                startButton.color = (255, 0, 0)
            else:
                startButton.color = 0, 255, 255

            if quitButton.isOver(mousePos):
                quitButton.color = (255, 0, 0)
            else:
                quitButton.color = 0, 255, 255
