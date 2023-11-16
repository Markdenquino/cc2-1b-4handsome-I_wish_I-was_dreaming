#BASE BASE
setup_game()
while True:
    cmd = get_player_input()
    do_stuff_with_player_input(cmd)
    update_state_of_the_game()
    if game_won() or game_lost():
        break
    show_game_state_to_player()
    
#ito ang base base

import pygame
import sys

# Initialize Pygame
pygame.init()

# uhh the screen
WIDTH, HEIGHT = 900, 650
CELL_SIZE = 40

# color picker
BLACK = (28, 26, 25)
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.fullscreen)
pygame.display.set_caption("Your Mother")

# Position 69
character_position = [0, 0]

# Main game loop and controls
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and character_position[1] > 0:
                character_position[1] -= 1
            elif event.key == pygame.K_s and character_position[1] < HEIGHT // CELL_SIZE - 1:
                character_position[1] += 1
            elif event.key == pygame.K_a and character_position[0] > 0:
                character_position[0] -= 1
            elif event.key == pygame.K_d and character_position[0] < WIDTH // CELL_SIZE - 1:
                character_position[0] += 1

    #Background
    screen.fill(BLACK)

    # Draw the character
    pygame.draw.rect(screen, WHITE, (character_position[0] * CELL_SIZE, character_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
