import pygame
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

#font
LETTER_FONT = pygame.font.Font("assets/font.otf",40)
def get_font(scale, SCREEN_HEIGHT):  # scale 是比例，比如 0.05 表示高度的 5%
    size = max(12, int(SCREEN_HEIGHT * scale))
    return pygame.font.Font("assets/font.ttf", size)

#button var's
RAD = 32
GAP = 20
A = 65   #every charc on keyboard is defined by a unique number and capital A is '65'

#classes
class Alphabet_Grid:
    def __init__(self, screen,font,startx,starty):
        self.screen = screen
        self.font = font
        self.startx = startx
        self.starty = starty
        self.letters = [] #letters stores the x_pos , y_pos, "the letter" , and boolean value 
        self.create_letters_list()
        #the boolean value stores whether the btn has been clciked b4 so we can cross out a letter based on whether ot not it's in the word
        #letters = [] #where all btns are stored, will store the xPos, yPos and letter

    def create_letters_list(self):
        for i in range(26):
            #determine x pos and y pos of each btn with complex math
            # implementing gap btw left and right of screen in the calculation             distance between each 2 btns                                                simulates having 2 rows
            x_pos = self.startx + GAP * 2 + ((RAD * 2 + GAP) * (i % 9))
            y_pos = self.starty + ((i//9)*(GAP + RAD * 2))

            #pairs of x,y values and letter being represented , all this info is added to the letters list made in class initialiser
            #getting every charcater represnetation number thru 'char(A+i) below as well
            # the boolean starts as true to say that "the letter does exist in the word so that when the game starts it exists ,but if it's clicked and the letter doesn't exist in the word, it will change to false"
            self.letters.append([x_pos,y_pos,chr(A+i),True]) 

    def draw_letters(self):
    #draw btns / letters
        for x, y, ltr, visible in self.letters:
            #splitting letter coord into 2 var's
            #x,y, ltr,visible = letter  
            if visible:  #by default all btns are visible
                pygame.draw.circle(self.screen,BLACK,(x,y), RAD, 3)
                text = self.font.render(ltr, 1,BLACK)
                #displaying letters
                self.screen.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

    def hande_clicks(self,pos):
        m_x, m_y = pos
        for letter in self.letters:
            x,y,ltr,visible = letter
            if visible and math.hypot(x-m_x,y-m_y) < RAD:
                letter [3] = False
        
#get starting position of where the circles/btns will be drawn
startx = round((screen_width - (RAD*2 + GAP)*9)/2)   
starty = screen_height - (screen_height*2/5)
grid = Alphabet_Grid(screen,LETTER_FONT,startx,starty)

# GAME LOOP
running = True
while running:
    screen.fill("white")

    #EVENT HANDLING
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.hande_clicks(pygame.mouse.get_pos())
    

    # RENDER YOUR GAME HERE
    grid.draw_letters()

    pygame.display.update()

    clock.tick(FPS)  #setting frame rate

pygame.quit()
