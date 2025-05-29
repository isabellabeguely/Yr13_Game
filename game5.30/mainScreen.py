import pygame, sys
from mainButton import Button
pygame.init()

# 获取当前屏幕尺寸
screen_info = pygame.display.Info()
SCREEN_WIDTH = round(screen_info.current_w * 4/5)  # 屏幕宽度的4/5
SCREEN_HEIGHT = round(screen_info.current_h * 4/5)  # 屏幕高度的2/5
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)



pygame.display.set_caption("Menu")
SCREEN.fill("white")

def get_font(scale, SCREEN_HEIGHT):  # scale 是比例，比如 0.05 表示高度的 5%
    size = max(12, int(SCREEN_HEIGHT * scale))
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        # 使用动态计算的屏幕尺寸
        PLAY_TEXT = get_font(0.075, SCREEN_HEIGHT).render("This is the PLAY screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3), 
                            text_input="BACK", font=get_font(0.075, SCREEN_HEIGHT), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        # 使用动态计算的屏幕尺寸
        OPTIONS_TEXT = get_font(0.075, SCREEN_HEIGHT).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3), 
                            text_input="BACK", font=get_font(0.075, SCREEN_HEIGHT), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT  
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()  # 每次循环获取当前窗口大小
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(0.1, SCREEN_HEIGHT).render("SPELLYMPICS", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), 
                            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*5//10), 
                            text_input="FreePlay mode", font=get_font(0.075, SCREEN_HEIGHT), 
                            base_color="#000000", hovering_color="Grey")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), 
                            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*7//10), 
                            text_input="Time limit mode", font=get_font(0.075, SCREEN_HEIGHT), 
                            base_color="#000000", hovering_color="Grey")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
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