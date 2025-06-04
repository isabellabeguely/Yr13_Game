import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale_width=None, scale_height=None):
        self.image = image
        self.x_pos = pos[0]# Center x position
        self.y_pos = pos[1]# Center y position
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.current_color = self.base_color
        self.scale_width = scale_width
        self.scale_height = scale_height

        self.text = self.font.render(self.text_input, True, self.current_color)

        if self.image is None:
            self.image = self.text  # Backup image as text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen, font):
        self.font = font
        self.text = self.font.render(self.text_input, True, self.current_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        screen_width, screen_height = screen.get_size()# Get screen dimensions
        # If scale_width and scale_height are provided, calculate button size based on screen dimensions
        if self.scale_width is not None and self.scale_height is not None:
            button_width = int(screen_width * self.scale_width)
            button_height = int(screen_height * self.scale_height)
            box_rect = pygame.Rect(0, 0, button_width, button_height)
            box_rect.center = (self.x_pos, self.y_pos)

        else:# Button border size (increase margin based on text size)
            padding_x, padding_y = 20, 10
            box_rect = pygame.Rect(
                self.text_rect.left - padding_x,
                self.text_rect.top - padding_y,
                self.text_rect.width + 2 * padding_x,
                self.text_rect.height + 2 * padding_y
        )
        

        # Draw button border (color follows hover)
        pygame.draw.rect(screen, self.current_color, box_rect, width=4)

        

        # display text
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):# Check if the mouse position is within the button area
        # Get the current screen size
        screen_width, screen_height = pygame.display.get_surface().get_size()
        if self.scale_width is not None and self.scale_height is not None: # If scale_width and scale_height are provided, calculate button size based on screen dimensions
            # Calculate button size based on screen dimensions
            button_width = int(screen_width * self.scale_width)
            button_height = int(screen_height * self.scale_height)
            box_rect = pygame.Rect(0, 0, button_width, button_height)
            box_rect.center = (self.x_pos, self.y_pos)
        else:
        # If no fixed size, use text size for the button
            padding_x, padding_y = 20, 10# Increase margin based on text size
            # Create a rectangle around the text with padding
            box_rect = pygame.Rect(
                self.text_rect.left - padding_x,
                self.text_rect.top - padding_y,
                self.text_rect.width + 2 * padding_x,
                self.text_rect.height + 2 * padding_y
        )
        return box_rect.collidepoint(position)# Check if the mouse position is within the button area

    def changeColor(self, position):# Change the button color based on mouse position
        # Check if the mouse position is within the button area
        if self.checkForInput(position):
            self.current_color = self.hovering_color
        else:
            self.current_color = self.base_color

