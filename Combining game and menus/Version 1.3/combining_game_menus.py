import pygame, sys

from freeplay_mode import freeplay_rungame
from timeLimitMode import timelimit_rungame

pygame.init()  # Initialize all Pygame modules

# --------------------- Window Initialization ---------------------
# Get current screen resolution and use 80% of it for the window
screen_info = pygame.display.Info()
# Calculate window dimensions as 80% of screen width and height
SCREEN_WIDTH = round(screen_info.current_w * 4/5)
SCREEN_HEIGHT = round(screen_info.current_h * 4/5)

# Create a resizable window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menu")  # Set window title

# Ratio of button size relative to the screen size
button_width_ratio = 0.4   # Button width = 40% of screen width
button_height_ratio = 0.1  # Button height = 10% of screen height

# --------------------- Font Scaling Function ---------------------
def get_font(scale, screen_height):
    #Returns a font object with size proportional to screen height. `scale` is a float (e.g., 0.05 for 5% of screen height).
    # Calculate font size based on screen height and scale factor
    size = max(6, int(screen_height * scale))  # Avoid font size too small

    return pygame.font.Font("font.otf", size)# Create and return a font object from specified font file

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

    pygame.draw.rect(SCREEN, current_color, box_rect, 3)
    SCREEN.blit(text_surf, text_rect)

    return box_rect

# --------------------- Freeplay Mode Screen ---------------------
# The Freeplay Mode Screen function used to sit here, but after the changes made, it wasn't necessary anymore

# --------------------- Time Limit Mode Screen ---------------------
# The Time Limit Mode Screen function used to sit here, but after the changes made, it wasn't necessary anymore

# --------------------- Main Menu Screen ---------------------
def main_menu():
    state = "menu"  # State control: menu, freeplay, timelimit. This acts as a placeholder.
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        MENU_MOUSE_POS = pygame.mouse.get_pos()
     # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if freeplay_rect.collidepoint(MENU_MOUSE_POS):
                    freeplay_rungame()
                if timelimit_rect.collidepoint(MENU_MOUSE_POS):
                    timelimit_rungame()
                if quit_rect.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
       
        title_font = get_font(0.2, SCREEN_HEIGHT)
        button_font = get_font(0.075, SCREEN_HEIGHT)
        if state == "menu":
            # Draw the title text
            title = title_font.render("SPELLYMPICS", True, "black")
            SCREEN.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5)))

       

        # Create buttons with dynamic position and size
            button_width = int(SCREEN_WIDTH * 0.5)
            button_height = int(SCREEN_HEIGHT * 0.1)
            button_size = (button_width, button_height)
            
            freeplay_rect = draw_button("FreePlay mode", (SCREEN_WIDTH//2, SCREEN_HEIGHT*3.9//10),
                                        button_font, "black", "gray", MENU_MOUSE_POS, button_size)
            timelimit_rect = draw_button("Time limit mode", (SCREEN_WIDTH//2, SCREEN_HEIGHT*5.9//10),
                                         button_font, "black", "gray", MENU_MOUSE_POS, button_size)
            quit_rect = draw_button("Quit", (SCREEN_WIDTH//2, SCREEN_HEIGHT*7.9//10),
                                    button_font, "black", "gray", MENU_MOUSE_POS, button_size)

        

        # Insert bee image on bottom-left
            bee = pygame.image.load("bee.png")
            bee = pygame.transform.scale(bee, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.2)))
            SCREEN.blit(bee, (20, SCREEN.get_height() - bee.get_height() - 20))

        # Insert man image on bottom-right
            man = pygame.image.load("man.png")
            man = pygame.transform.scale(man, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.3)))
            SCREEN.blit(man, (SCREEN.get_width() - man.get_width() - 20, SCREEN.get_height() - man.get_height() - 20))

       

        pygame.display.update()

# --------------------- Start the Program ---------------------
main_menu()