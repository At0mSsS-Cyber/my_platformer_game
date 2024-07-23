import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, movement_range, movement_speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))  # Set the color to black
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.original_x = x
        self.movement_range = movement_range
        self.movement_speed = movement_speed
        self.direction = 1  # 1 for right, -1 for left

    def update(self):
        # Move platform left and right
        self.rect.x += self.movement_speed * self.direction
        
        # Reverse direction if the platform hits the edge of its movement range
        if self.rect.left <= self.movement_range[0] or self.rect.right >= self.movement_range[1]:
            self.direction *= -1
