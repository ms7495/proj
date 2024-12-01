import pygame
from constants import *

# Initialize Pygame
pygame.init()

def loop(screen):

    # Create a surface
    surface = pygame.Surface((200, 150))
    surface.fill((0, 0, 0))  # Fill surface with black

    # Blit the surface onto the screen
    screen.blit(surface, (100, 100))  # Position the surface at (100, 100)

    # Update the display
    pygame.display.flip()

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Run the game loop logic
        loop(screen)


if __name__ == "__main__":
    main()
