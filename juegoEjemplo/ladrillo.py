import pygame

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image        = pygame.image.load('imagenes/ladrillo.png')
        self.rect         = self.image.get_rect()
        self.rect.topleft = position