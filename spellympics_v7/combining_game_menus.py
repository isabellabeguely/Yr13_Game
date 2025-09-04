import pygame, sys, os

from freeplayMode import freeplay_mode
from timeLimitMode import timelimit_rungame
from saveloadtest import running_save_load_system, SaveLoadSystem

#from saveloadtest import SaveLoadSystem

pygame.init()  # Initialize all Pygame modules

def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS  # Temporary path after packing
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    try:
        base_path = sys._MEIPASS  # PyInstaller临时路径
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# --------------------- Window Initialization ---------------------

# Get screen dimensions
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
# Create a resizable window and setting up window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)


pygame.display.set_caption("Menu")  # Set window title

# Ratio of button size relative to the screen size
button_width_ratio = 0.4   # Button width = 40% of screen width
button_height_ratio = 0.1  # Button height = 10% of screen height

# --------------------- Font Scaling Function ---------------------
def get_font(scale, screen_height):
    #Returns a font object with size proportional to screen height. `scale` is a float (e.g., 0.05 for 5% of screen height).
    # Calculate font size based on screen height and scale factor
    size = max(6, int(screen_height * scale))  # Avoid font size too small

    return pygame.font.Font(resource_path("assets/font.otf"), size)# Create and return a font object from specified font file

# --------------------- Button Drawing Function ---------------------
# This function draws a button with text, changing color on hover
def draw_button(text, center_pos, font, base_color, hover_color, MOUSE_POS, box_size):
    is_hovered = pygame.Rect(0, 0, *box_size).move(
        center_pos[0] - box_size[0] // 2,
        center_pos[1] - box_size[1] // 2
    ).collidepoint(MOUSE_POS)

    current_color = hover_color if is_hovered else base_color

    # Create a rectangle for the button with specified size
    box_rect = pygame.Rect(0, 0, *box_size)
    box_rect.center = center_pos

    # Render the text and center it within the button
    text_surf = font.render(text, True, current_color)
    text_rect = text_surf.get_rect(center=center_pos)

    pygame.draw.rect(screen, current_color, box_rect, 3)
    screen.blit(text_surf, text_rect)

    return box_rect

# --------------------- Freeplay Mode Screen ---------------------
# The Freeplay Mode Screen function used to sit here, but after the changes made, it wasn't necessary anymore

# --------------------- Time Limit Mode Screen ---------------------
# The Time Limit Mode Screen function used to sit here, but after the changes made, it wasn't necessary anymore

# --------------------- Main Menu Screen ---------------------
def main_menu():
    state = "menu"
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT

    while True:
        screen.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Get fonts
        title_font = get_font(0.2, SCREEN_HEIGHT)
        button_font = get_font(0.075, SCREEN_HEIGHT)

        if state == "menu":
            # Draw the title
            title = title_font.render("SPELLYMPICS", True, "black")
            screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5)))
            # Create buttons first (before event handling!)
            button_width = int(SCREEN_WIDTH * 0.5)
            button_height = int(SCREEN_HEIGHT * 0.1)
            button_size = (button_width, button_height)

            freeplay_rect = draw_button("FreePlay mode", (SCREEN_WIDTH//2, SCREEN_HEIGHT*3.9//10),
                                        button_font, "black", "gray", MENU_MOUSE_POS, button_size)
            timelimit_rect = draw_button("Time limit mode", (SCREEN_WIDTH//2, SCREEN_HEIGHT*5.9//10), 
                                         button_font, "black", "gray", MENU_MOUSE_POS, button_size)
            quit_rect = draw_button( "Quit", (SCREEN_WIDTH//2, SCREEN_HEIGHT*7.9//10),
                                    button_font, "black", "gray", MENU_MOUSE_POS, button_size)

            # Draw bee image
            bee = pygame.image.load(resource_path("assets/bee.png"))
            bee = pygame.transform.scale(bee, (int(screen.get_width() * 0.2), int(screen.get_width() * 0.2)))
            screen.blit(bee, (20, screen.get_height() - bee.get_height() - 20))

            # Draw man image
            man = pygame.image.load(resource_path("assets/man.png"))
            man = pygame.transform.scale(man, (int(screen.get_width() * 0.2), int(screen.get_width() * 0.3)))
            screen.blit(man, (screen.get_width() - man.get_width() - 20, screen.get_height() - man.get_height() - 20))

        # Now handle events (after button rects are defined)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                running_save_load_system(values={}, file_name='high_scores.txt', save_value=SaveLoadSystem.save_value)
            elif event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if freeplay_rect.collidepoint(MENU_MOUSE_POS):
                    freeplay_mode(screen, SCREEN_WIDTH, SCREEN_HEIGHT, back_to_menu=main_menu)
                elif timelimit_rect.collidepoint(MENU_MOUSE_POS):
                    timelimit_rungame(screen, SCREEN_WIDTH, SCREEN_HEIGHT, back_to_menu=main_menu)
                elif quit_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    running_save_load_system(values={}, file_name='high_scores.txt', save_value=SaveLoadSystem.save_value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running_save_load_system(values={}, file_name='high_scores.txt', save_value=SaveLoadSystem.save_value)
        pygame.display.update()

# --------------------- Start the Program ---------------------
main_menu()
