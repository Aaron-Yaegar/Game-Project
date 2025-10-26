from settings import *


class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        # size expected as a (width, height) tuple passed from caller
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)