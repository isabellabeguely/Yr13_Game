import pygame, sys
from mainButton import Button

pygame.init()

# Initial screen settings
screen_info = pygame.display.Info()
SCREEN_WIDTH = round(screen_info.current_w * 4/5)
SCREEN_HEIGHT = round(screen_info.current_h * 4/5)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menu")

# Load font function
def get_font(scale, screen_height):
    size = max(12, int(screen_height * scale))
    return pygame.font.Font("assets/font.otf", size)

def play():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        font = get_font(0.075, SCREEN_HEIGHT)

        PLAY_TEXT = font.render("This is the PLAY screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3),
                           text_input="BACK", font=font, base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        font = get_font(0.075, SCREEN_HEIGHT)

        OPTIONS_TEXT = font.render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3),
                              text_input="BACK", font=font, base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        title_font = get_font(0.2, SCREEN_HEIGHT)
        button_font = get_font(0.075, SCREEN_HEIGHT)

        MENU_TEXT = title_font.render("SPELLYMPICS", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*5//10),
                             text_input="FreePlay mode", font=button_font,
                             base_color="#000000", hovering_color="Grey")

        OPTIONS_BUTTON = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*7//10),
                                text_input="Time limit mode", font=button_font,
                                base_color="#000000", hovering_color="Grey")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN, button_font)
        # Insert the bee image in the bottom left corner
        bee_img = pygame.image.load("assets/bee.png")
        bee_img = pygame.transform.scale(bee_img, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.2)))
        bee_width = bee_img.get_width()
        bee_height = bee_img.get_height()
        SCREEN.blit(bee_img, (20, SCREEN.get_height() - bee_height-20))
        # Insert the man image in the bottom right corner
        man_img = pygame.image.load("assets/man.png")
        man_img = pygame.transform.scale(man_img, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.3)))
        man_width = man_img.get_width()
        man_height = man_img.get_height()
        SCREEN.blit(man_img,(SCREEN.get_width()-man_width-20, SCREEN.get_height() - man_height-20)) 

        for event in pygame.event.get():
            # Set refresh rate
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()

        pygame.display.update()

main_menu()
