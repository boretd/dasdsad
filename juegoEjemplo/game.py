import pygame
import sys
import time
from pelota import Pelota
from barra import Barra
from muro import Muro
from ladrillo import Ladrillo
from punto import Punto
from constantes import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_X_SECONDS, COLOR_RGB_BLUE, COLOR_RGB_WHITE

pygame.init() # Necesario para el uso de fuentes
pygame.display.set_caption('Juego de ladrillos en Python')
pygame.key.set_repeat(30)
class Game:
    def __init__(self):
        self.pelota_in_barra  = True
        self.clock            = pygame.time.Clock()
        self.punto            = Punto()
        self.pelota           = Pelota()
        self.barra            = Barra()
        self.muro             = Muro()
        self.window           = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        """ Método Principal loop del juego """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.barra.move(event)
                    if self.pelota_in_barra == True and event.key == pygame.K_SPACE:
                        self.pelota_in_barra = False
            
            self.clock.tick(FRAMES_X_SECONDS)
            self.window.fill(COLOR_RGB_BLUE) 
            self.punto.draw(self.window) 
            self.pelota.draw(self.window) 
            self.barra.draw(self.window) 
            self.muro.draw(self.window)
            self.check_take_out()
            self.check_colicion_pelota_barra()  
            self.check_colicion_pelota_muro() 
            self.check_win_game() 
            self.check_end_game()
            pygame.display.flip() 
   
    def check_take_out(self):
        """ Método de verificación si el jugador sacó la pelota y actualiza eje x y pelota """
        if self.pelota_in_barra:
            self.pelota.rect.midbottom = self.barra.rect.midtop
        else:
            self.pelota.move()
    
    def check_colicion_pelota_barra(self):
        """ Método de verificación si la pelota colisionó con la paleta """
        if pygame.sprite.collide_rect(self.pelota, self.barra):
            # Colición entre pelota y paleta, recibe 2 sprite como agumento
            self.pelota.colision_y()

    def check_colicion_pelota_muro(self):
        """ Se comprueba las coliciones en que eje sucedio para cambiar direccion de la bolita,
            destruyendo el ladrillo afectado en el muro
        """
        lista_ladrillos = pygame.sprite.spritecollide(self.pelota, self.muro, False)
        if lista_ladrillos:
            ladrillo= lista_ladrillos[0]
            pelota_rect_coords_x = self.pelota.rect.centerx
            # Comprobación colición por eje X, Izquierda y Derecha
            if pelota_rect_coords_x < ladrillo.rect.left or pelota_rect_coords_x > ladrillo.rect.right:
                self.pelota.colision_x()
            else:
                self.pelota.colision_y()

            self.muro.remove(ladrillo)  # Eliminar ladrillo del muro Manualmente
            self.punto.puntos += 10  # Al eliminar un ladrillo aumentamos la puntiación en +10

    def check_end_game(self):
        """ Método de verificación si termino el juegó """
        if self.pelota.rect.top > WINDOW_HEIGHT:
            self.finish_game('loss')

    def check_win_game(self):
        """ Método de verificación si gano el juegó """
        if len(self.muro.sprites()) == 0:
            self.finish_game('win')

    def finish_game(self, type_of_completion: str):
        """ Método de visualización de finalización del juego """
        if type_of_completion == "win":
            description = 'Juego Ganado!'
        else:
            description = 'Juego Perdido!'

        font = pygame.font.SysFont('Arial', 72)
        text = font.render(description, True, COLOR_RGB_WHITE)
        text_rect = text.get_rect()
        text_rect.center = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2] # Pos text en el centro del juego
        self.window.blit(text, text_rect) # Dibujamos el texto en la pantalla
        pygame.display.flip()
        time.sleep(3)
        sys.exit()


