import pygame
from constantes import *
from auxiliar import Auxiliar


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y,width, height,  type=1):
        super().__init__()
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images\estrellas\image ({0}).png",1,4,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.active = True
        self.angle = 0  # Nuevo atributo para la rotación
    def update(self, delta_ms):
    # Lógica de actualización de la estrella
    # Aquí puedes modificar el ángulo de rotación
        self.angle += 1  # Incrementa el ángulo en cada actualización
    def desactive(self):
        self.active = False    
    def draw(self,screen):
        if self.active:
            screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)