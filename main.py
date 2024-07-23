import pygame
import sys
from player import Player
from platform import Platform

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Platformer Game')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load sound
hit_sound = pygame.mixer.Sound('assets/sounds/hit_sound.mp3')

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms (obstacles)
plat1 = Platform(100, 500, 200, 20, movement_range=(100, 700), movement_speed=2)
plat2 = Platform(400, 400, 200, 20, movement_range=(300, 500), movement_speed=1)
platforms.add(plat1, plat2)
all_sprites.add(plat1, plat2)

# Variables for game state
failed = False
victory = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not failed and not victory:
        # Update platforms
        for platform in platforms:
            platform.update()

        # Check for player collisions with platforms
        if pygame.sprite.spritecollide(player, platforms, False):
            hit_sound.play()  # Play sound effect
            failed = True
            pygame.time.delay(500)  # Short delay for sound effect to play

        # Check if player reaches bottom without touching obstacles
        if player.rect.bottom >= height:
            victory = True

    if failed:
        # Display failure message and retry option
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 55)
        text = font.render('Failed! Press R to Retry', True, RED)
        screen.blit(text, (width // 4, height // 2))
        pygame.display.flip()

        # Wait for player to press 'R' to retry
        retry = False
        while not retry:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        retry = True
                        failed = False
                        # Reset player position or game state if needed
                        player.rect.center = (width // 2, height // 2)
                        player.velocity = pygame.Vector2(0, 0)
                        break
        continue

    if victory:
        # Display victory message
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 55)
        text = font.render('Victory! Press R to Retry', True, RED)
        screen.blit(text, (width // 4, height // 2))
        pygame.display.flip()

        # Wait for player to press 'R' to retry
        retry = False
        while not retry:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        retry = True
                        victory = False
                        # Reset player position or game state if needed
                        player.rect.center = (width // 2, height // 2)
                        player.velocity = pygame.Vector2(0, 0)
                        break
        continue

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
