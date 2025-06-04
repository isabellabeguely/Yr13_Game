import pygame, sys
from mainButton import Button  # Import custom Button class from external file

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
    """
    Returns a font object with size proportional to screen height.
    `scale` is a float (e.g., 0.05 for 5% of screen height).
    """
     # Calculate font size based on screen height and scale factor
    size = max(12, int(screen_height * scale))  # Avoid font size too small

    return pygame.font.Font("assets/font.otf", size)# Create and return a font object from specified font file

# --------------------- Freeplay Mode Screen ---------------------
def freeplay():
    # Initialize global variables for screen and dimensions
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")  # Fill background
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()  # Update current screen size
        freeplay_MOUSE_POS = pygame.mouse.get_pos()  # Track mouse position
        font = get_font(0.07, SCREEN_HEIGHT)  # Get dynamic font size

        # Display screen title
        freeplay_TEXT = font.render("This is the PLAY screen.", True, "Black")
        freeplay_RECT = freeplay_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(freeplay_TEXT, freeplay_RECT)# Render text and get its rectangle for positioning

        # Create BACK button
        freeplay_BACK = Button(
            image=None,# No image, use text only
            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3),
            text_input="BACK",
            font=font,
            base_color="Black",
            hovering_color="Green"
        )
        # Update button color based on mouse position
        freeplay_BACK.changeColor(freeplay_MOUSE_POS)
        # Update button display
        freeplay_BACK.update(SCREEN, font)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Exit app
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if freeplay_BACK.checkForInput(freeplay_MOUSE_POS):
                    main_menu()  # Return to main menu

        pygame.display.update()  # Refresh screen

# --------------------- Time Limit Mode Screen ---------------------
def timelimit():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        timelimit_MOUSE_POS = pygame.mouse.get_pos()# Track mouse position
        font = get_font(0.075, SCREEN_HEIGHT)

        # Display screen title
        timelimit_TEXT = font.render("This is the OPTIONS screen.", True, "Black")
        timelimit_RECT = timelimit_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        SCREEN.blit(timelimit_TEXT, timelimit_RECT)

        # Create BACK button
        timelimit_BACK = Button(
            image=None,
            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3),
            text_input="BACK",
            font=font,
            base_color="Black",
            hovering_color="Green"
        )

        timelimit_BACK.changeColor(timelimit_MOUSE_POS)# Change button color based on mouse position
        timelimit_BACK.update(SCREEN, font)# Update button display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                # Adjust screen size on window resize
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if timelimit_BACK.checkForInput(timelimit_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# --------------------- Main Menu Screen ---------------------
def main_menu():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    while True:
        SCREEN.fill("white")
        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        title_font = get_font(0.2, SCREEN_HEIGHT)
        button_font = get_font(0.075, SCREEN_HEIGHT)

        # Display the game title
        MENU_TEXT = title_font.render("SPELLYMPICS", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Create buttons with dynamic position and size
        freeplay_BUTTON = Button(
            image=None,
            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*3.9//10),
            text_input="FreePlay mode",
            font=button_font,
            base_color="#000000",
            hovering_color="Grey",
            scale_width=button_width_ratio,
            scale_height=button_height_ratio
        )

        timelimit_BUTTON = Button(
            image=None,
            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*5.9//10),
            text_input="Time limit mode",
            font=button_font,
            base_color="#000000",
            hovering_color="Grey",
            scale_width=button_width_ratio,
            scale_height=button_height_ratio
        )

        QUIT_BUTTON = Button(
            image=None,
            pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT*7.9//10),
            text_input="Quit",
            font=button_font,
            base_color="#000000",
            hovering_color="Grey",
            scale_width=button_width_ratio,
            scale_height=button_height_ratio
        )

        # Update and draw all buttons
        for button in [freeplay_BUTTON, timelimit_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN, button_font)

        # Insert bee image on bottom-left
        bee_img = pygame.image.load("assets/bee.png")
        bee_img = pygame.transform.scale(
            bee_img, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.2))
        )
        bee_width = bee_img.get_width()
        bee_height = bee_img.get_height()
        SCREEN.blit(bee_img, (20, SCREEN.get_height() - bee_height - 20))

        # Insert man image on bottom-right
        man_img = pygame.image.load("assets/man.png")
        man_img = pygame.transform.scale(
            man_img, (int(SCREEN.get_width() * 0.2), int(SCREEN.get_width() * 0.3))
        )
        man_width = man_img.get_width()
        man_height = man_img.get_height()
        SCREEN.blit(man_img, (SCREEN.get_width() - man_width - 20, SCREEN.get_height() - man_height - 20))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if freeplay_BUTTON.checkForInput(MENU_MOUSE_POS):
                    freeplay()
                if timelimit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    timelimit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# --------------------- Start the Program ---------------------
main_menu()
