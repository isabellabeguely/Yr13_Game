import pygame, sys
import math

# setup display
pygame.init()

clock = pygame.time.Clock()
FPS = 60
running = True

countdown_clock = pygame.time.Clock()
counter, text = 30, '30'
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width-10, screen_height-50),pygame.RESIZABLE)

#Game Variables
BLACK = (0,0,0)
GREY = (133, 133, 133)
GAP = 20
square_size = 30
mode = "Timelimit"

#load in images
home_icon = pygame.image.load("homepage-icon.png")

#font
LETTER_FONT = pygame.font.Font("font.otf",40)
WORD_FONT = pygame.font.Font("font.otf",90)
#def get_font(scale, SCREEN_HEIGHT):  
#    size = max(12, int(SCREEN_HEIGHT * scale))
#    return pygame.font.Font("assets/font.ttf", size)

#button var's
RAD = 32
GAP = 20
A = 65   #every charc on keyboard is defined by a unique number and capital A is '65'



#worbank setup
words = []
def load_words_from_file(filename):
    with open(filename, 'r') as file:
        for line in file: #goes thru each line of the file
            #the strip removes the \n and spaces and the strip(".",1) = splits the number and word into 2 and the 1 says only split after the 1st fullstop
            parts = line.strip().split('.',1)  
            if len(parts) == 2:  #checks that the line was split into exactly 2 parts
                word_asked = parts[1].strip()  #removes spaces in the 2nd part so ["1", "developer"] takes developer part
                words.append(word_asked)  #adds the word to the list
    return words  #return a list of all the words
load_words_from_file("word_bank.txt")


current_word_index = 0

word = words[0]

#classes
class TimeLimitMode:
    global text
    def __init__(self, screen,font_letter,font_word,startx,starty,word):
        self.screen = screen
        self.font_letter = font_letter
        self.font_word = font_word
        self.home_btn = pygame.transform.scale(home_icon,(45,45))
        self.startx = startx
        self.starty = starty
        self.letters = [] #letters stores the x_pos , y_pos, "the letter" , and boolean value 
        self.create_letters_list()

        self.show_word = False
        self.word_asked = ""
        self.display_duration = 700
        self.word_display_start_time = None

        self.score = 0
        self.score_increment = 5
        self.word = word 
        self.guessed = []
        #self.current_word_index = 0
        #letters = [] #where all btns are stored, will store the xPos, yPos and letter

    def draw_game_info(self):
        #draw info such as the score, the lives, home btn etc.

        #draw home icon
        self.screen.blit(self.home_btn,(screen_width-(screen_width*7/8)-70,screen_height-(screen_height-50)))

        #draw score info
        score_text = self.font_letter.render(f"Score: {self.score}",1,BLACK)
        self.screen.blit(score_text,(screen_width-(screen_width*2/8),screen_height-(screen_height-50)))

        #draw game mode
        if mode == "Timelimit":
            mode_text = self.font_letter.render("TIME LIMIT MODE",1,BLACK)
            self.screen.blit(mode_text,(screen_width-(screen_width*7/8),screen_height-(screen_height-50)))

            countdown_title = self.font_letter.render("REMAINING TIME: ",1,BLACK)
            self.screen.blit(countdown_title,(screen_width-(screen_width*3/8),screen_height*1/8))
            countdown_text = self.font_letter.render(text,1,BLACK)
            self.screen.blit(countdown_text,(screen_width-(screen_width*1/9),screen_height*1/8))


    def create_letters_list(self):
        for i in range(26):
            #determine x pos and y pos of each btn with complex math
            # implementing gap btw left and right of screen in the calculation             distance between each 2 btns                                                simulates having 2 rows
            x_pos = self.startx + GAP * 2 + ((RAD * 2 + GAP) * (i % 9))
            y_pos = self.starty + ((i//9)*(GAP + RAD * 2))

            #pairs of x,y values and letter being represented , all this info is added to the letters list made in class initialiser
            #getting every charcater represnetation number thru 'char(A+i) below as well

            #the boolean value stores whether the btn has been clciked b4 so we can cross out a letter based on whether ot not it's in the word
            # the boolean starts as true to say that "the letter does exist in the word so that when the game starts it exists ,but if it's clicked and the letter doesn't exist in the word, it will change to false"
            self.letters.append([x_pos,y_pos,chr(A+i),True]) 

    def draw_letters(self):
    #draw word for specific duration
        #only show the word if the timer hasn't expired
        if self.show_word:
            if self.word_display_start_time is None:
                self.word_display_start_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.word_display_start_time < self.display_duration:

                text_draw = self.font_word.render(self.word_asked,1,BLACK)
                self.screen.blit(text_draw,((screen_width/2)-(text_draw.get_width()/2),(screen_height//2)-(screen_height*2/8)))
            else: 
                self.show_word = False
                self.word_display_start_time = None
    #draw word
        display_word = ""
        for letter in self.word:   #looping thru every letter of the actual word
            #check if we have guessed the letter yet
            if letter in self.guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text_entered = self.font_word.render(display_word,1,BLACK)
        
        self.screen.blit(text_entered,((screen_width/2)-(text_entered.get_width()/2),(screen_height//2)-(screen_height*1/8)))

    #draw btns / letters
        for x, y, ltr, visible in self.letters:
            #splitting letter coord into 2 var's
            #x,y, ltr,visible = letter  
            if visible:  #by default all btns are visible
                pygame.draw.circle(self.screen,BLACK,(x,y), RAD, 3)
                text = self.font_letter.render(ltr, 1,BLACK)
                #displaying letters
                self.screen.blit(text, (x-text.get_width()/2,y-text.get_height()/2))
            
            if not visible:
                pygame.draw.circle(self.screen,GREY,(x,y), RAD, 3)
                text = self.font_letter.render(ltr, 1,GREY)
                #displaying letters
                self.screen.blit(text, (x-text.get_width()/2,y-text.get_height()/2))
    def hande_clicks(self,pos):
        global current_word_index
        m_x, m_y = pos 
        for letter in self.letters:
            x,y,ltr,visible = letter
            if visible and math.hypot(x-m_x,y-m_y) < RAD:
                letter [3] = False
                self.guessed.append(ltr)   #adds correctly guessed letter to scren
                if ltr in self.word:
                    self.score += self.score_increment
                    
                    #below checking if each letter is in guessed list
                    if all (ltr in self.guessed for ltr in self.word):
                        current_word_index+=1
                        
                        if current_word_index < len(words):
                            self.word = words[current_word_index]
                            self.guessed = [] #reset gessed letters
                            for l in self.letters:
                                l[3] = True
                            
                            self.show_word = True
                            self.word_display_start_time = pygame.time.get_ticks()
                            self.word_asked = self.word
                        else:
                            print("no more words")
                    
                else:
                    self.score -= self.score_increment

        
#get starting position of where the circles/btns will be drawn
startx = round((screen_width - (RAD*2 + GAP)*9)/2)   
starty = screen_height - (screen_height*2/5)
grid = TimeLimitMode(screen,LETTER_FONT,WORD_FONT,startx,starty,words[current_word_index])
grid.show_word = True
grid.word_display_start_time = pygame.time.get_ticks()
grid.word_asked = grid.word

def timelimit_rungame():
    global text, counter
    # GAME LOOP
    timelimit_running = True
    while timelimit_running:
        screen.fill("white")

        #EVENT HANDLING
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                timelimit_running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid.hande_clicks(pygame.mouse.get_pos())
            if event.type ==  pygame.USEREVENT: 
                counter -= 1
                text = str(counter) if counter > 0 else 'GAME OVER'
        

        # RENDER YOUR GAME HERE
        grid.draw_letters()
        grid.draw_game_info()

        pygame.display.update()

        clock.tick(FPS)  #setting frame rate

pygame.QUIT
