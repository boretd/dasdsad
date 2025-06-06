import pygame
from ladrillo import Ladrillo
from constantes import WINDOW_WIDTH

class Muro(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.pos_x = 0
        self.pos_y = 20
        # Construcción de muro
        # Cantidad de ladrillos múltiplos de 16 , 4 filas 64
        for x in range(0, 64):
            if self.pos_x >= WINDOW_WIDTH:
                self.pos_x = 0
                self.pos_y = self.pos_y + ladrillo.rect.height
            ladrillo = Ladrillo((self.pos_x, self.pos_y))
            # Agregar Sprite al grupo
            self.add(ladrillo)
            self.pos_x = self.pos_x + ladrillo.rect.width
