import pygame
from constantes import *
from player import *
from auxiliar import Auxiliar


class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, player, p_scale=1,bandera=False,movimiento=False):
        super().__init__()
        self.player = player
        if(bandera):
           if movimiento:
                self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/POISON/Poison ({0}).png", 0, 10, flip=False, scale=1)
                self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/POISON/Poison ({0}).png", 0, 10, flip=True, scale=1)
           else:
                self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/SWORD/Sword ({0}).png", 0, 3, flip=False, scale=0.4)
                self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/SWORD/Sword ({0}).png", 0, 3, flip=False, scale=0.4) 
        else:
            self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Katana ({0}).png", 1, 4, flip=False, scale=0.6)
            self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Katana ({0}).png", 1, 4, flip=True, scale=0.6)
        self.direccion = direccion
        self.velocidad = 5  # Velocidad de movimiento del objeto
        self.frame = 0
        self.frame_count = 0  # Contador de frames
        self.frame_limit = 6  # Límite de frames para cambiar la imagen
        if direccion == DIRECTION_R:
            self.animaciones = self.disparo_d
        elif direccion == DIRECTION_L:
            self.animaciones = self.disparo_i
            self.velocidad *= -1  # Invierte la velocidad para moverse hacia la izquierda
        else:
            self.animaciones = None
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self,pausa):
        if not pausa:  # Verifica si el juego no está en pausa
            self.rect.x += self.velocidad
            self.frame_count += 1
            if self.frame_count >= self.frame_limit:
                self.frame += 1
                if self.frame >= len(self.animaciones):
                    self.frame = 0
                self.image = self.animaciones[self.frame]
                self.frame_count = 0
            # Si el objeto sale de la ventana, se elimina
            if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
                self.player.attack_launched = False
                self.kill()
