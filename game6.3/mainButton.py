import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.current_color = self.base_color

        self.text = self.font.render(self.text_input, True, self.current_color)

        if self.image is None:
            self.image = self.text  # Backup image as text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen, font):
        self.font = font
        self.text = self.font.render(self.text_input, True, self.current_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        # Button border size (increase margin based on text size)
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

    def checkForInput(self, position):
        #Allow detection of the range of 'boxes'
        padding_x, padding_y = 20, 10
        box_rect = pygame.Rect(
            self.text_rect.left - padding_x,
            self.text_rect.top - padding_y,
            self.text_rect.width + 2 * padding_x,
            self.text_rect.height + 2 * padding_y
        )
        return box_rect.collidepoint(position)

    def changeColor(self, position):
        if self.checkForInput(position):
            self.current_color = self.hovering_color
        else:
            self.current_color = self.base_color
