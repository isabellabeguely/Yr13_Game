import pygame
import os
import math

# setup display
pygame.init()

clock = pygame.time.Clock()
FPS = 60
running = True

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width-10, screen_height-50),pygame.RESIZABLE)

#Game Variables
BLACK = (0,0,0)
GAP = 20
square_size = 30

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
#button var's
RAD = 32
GAP = 20
letters = [] #where all btns are stored, will store the xPos, yPos and letter
startx = round((screen_width - (RAD*2 + GAP)*9)/2)
starty = screen_height - (screen_height*2/5)
A = 65   #every charc on keyboard is defined by a unique number

#classes
class Alphabet_Grid:
    def __init__(self):
        pass

    def create_letters_list(self):
        for i in range(26):
            #determine x pos and y pos of each btn
            # so there's gap btw left and right of screen              distance between each 2 btns                                                simulates having 2 rows
            x_pos = startx + GAP * 2 + ((RAD * 2 + GAP) * (i % 9))
            y_pos = starty + ((i//9)*(GAP + RAD * 2))
            letters.append([x_pos,y_pos,chr(A+i)]) #pairs of x,y values and letter, getting charcater represnetation

    def draw_letters(self):
    #draw btns / letters
        for letter in letters:
            #splitting letter coord into 2 var's
            x,y, ltr = letter  
            pygame.draw.circle(screen,BLACK,(x,y), RAD, 3)
            text = LETTER_FONT.render(ltr, 1,BLACK)
            #displaying letters
            screen.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

while running:
    #EVENT HANDLING
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    alphabet_grid = Alphabet_Grid()
    alphabet_grid.create_letters_list()
    alphabet_grid.draw_letters()

    pygame.display.update()

    clock.tick(FPS)  #setting frame rate

pygame.quit()
