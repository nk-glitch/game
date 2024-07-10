import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Set up the screen
pygame.display.set_caption('SNAKE GAME')
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Player properties
player_x = 100
player_y = 100
player_velocity = [0, 0]  # [x_velocity, y_velocity]
player_size = 20

#Change this to make snake go faster or slower
speed = 0.1


#Item x and y pos
item_x=0
item_y=0
def create_item():
    global item_y
    global item_x
    item_x = randint(0,800)
    item_y = randint(0,600)
create_item()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity[0] = -speed
                player_velocity[1] = 0
            elif event.key == pygame.K_RIGHT:
                player_velocity[0] = speed
                player_velocity[1] = 0
            elif event.key == pygame.K_UP:
                player_velocity[1] = -speed
                player_velocity[0] = 0
            elif event.key == pygame.K_DOWN:
                player_velocity[1] = speed
                player_velocity[0] = 0

    # Update player position
    player_x += player_velocity[0]
    player_y += player_velocity[1]

    # Keep player within screen bounds
    if player_x < 0:
        player_x = 0
    elif player_x + player_size > screen_width:
        player_x = screen_width - player_size
    if player_y < 0:
        player_y = 0
    elif player_y + player_size > screen_height:
        player_y = screen_height - player_size


    # Check for colliosion
    if player_y - item_y <= 10 or player_x - item_x <= 10:
        create_item()

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_size, player_size))

    # Item picked up
    pygame.draw.rect(screen, (149, 200, 160), (item_x, item_y, 10, 10))


    pygame.display.flip()




# Quit Pygame
pygame.quit()
