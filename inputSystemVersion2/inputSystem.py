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

#fonts
#LETTER_FONT = pygame.font.SysFont('comicsans', 30)
LETTER_FONT = pygame.font.Font("assets/font.otf",40)
def get_font(scale, SCREEN_HEIGHT):  # scale 是比例，比如 0.05 表示高度的 5%
    size = max(12, int(SCREEN_HEIGHT * scale))
    return pygame.font.Font("assets/font.ttf", size)

#button var's
RAD = 32
GAP = 20
#letters stores the x_pos , y_pos, "the letter" , and boolean value 
#the boolean value stores whether the btn has been clciked b4 so we can cross out a letter based on whether ot not it's in the word
letters = [] #where all btns are stored, will store the xPos, yPos and letter

#get starting position of where the circles/btns will be drawn
startx = round((screen_width - (RAD*2 + GAP)*9)/2)   
starty = screen_height - (screen_height*2/5)
A = 65   #every charc on keyboard is defined by a unique number and capital A is '65'

#classes
class Alphabet_Grid:
    def __init__(self):
        pass

    def create_letters_list(self):
        for i in range(26):
            #determine x pos and y pos of each btn with complex math
            # implementing gap btw left and right of screen in the calculation             distance between each 2 btns                                                simulates having 2 rows
            x_pos = startx + GAP * 2 + ((RAD * 2 + GAP) * (i % 9))
            y_pos = starty + ((i//9)*(GAP + RAD * 2))

            #pairs of x,y values and letter being represented , all this info is added to the character list
            #getting every charcater represnetation number thru 'char(A+i) below as well
            # the boolean starts as true to say that "the letter does exist in the word so that when the game starts it exists ,but if it's clicked and the letter doesn't exist in the word, it will change to false"
            letters.append([x_pos,y_pos,chr(A+i),True]) 

    def draw_letters(self):
    #draw btns / letters
        for letter in letters:
            #splitting letter coord into 2 var's
            x,y, ltr,visible = letter  
            if visible:  #by default all btns are visible
                pygame.draw.circle(screen,BLACK,(x,y), RAD, 3)
                text = LETTER_FONT.render(ltr, 1,BLACK)
                #displaying letters
                screen.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

#the below must be called outside main loop- so it only runs once -  so that the on click functions of clicking a letter and something happening shows
alphabet_grid = Alphabet_Grid()
alphabet_grid.create_letters_list()

while running:
    #EVENT HANDLING
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get position of mouse on click
            m_x, m_y = pygame.mouse.get_pos()   
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:  #if the btn is visible, check for click
                    #using hypotenuse to get distance btw 2 points, basically calculating if the moucclick is on/within an actual circle btn
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < RAD:   #less than or equal to RAD of circle, if more than circle Rad then not clicking on btn
                        letter[3] = False  #3rd pos is the visible handler
                        #once a btn is pressed and set to false, it will disapear from the screen

    screen.fill("white")

    # RENDER YOUR GAME HERE
    alphabet_grid.draw_letters()

    pygame.display.update()

    clock.tick(FPS)  #setting frame rate

pygame.quit()
