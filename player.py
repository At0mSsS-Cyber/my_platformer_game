import pygame

# Create player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_image = pygame.image.load('assets/images/player.png')
        player_image = pygame.transform.scale(player_image, (100, 100))
        self.image = player_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000 // 2, 15 // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def jump(self):
        self.velocity.y = -10
