import pygame
from katana import *
from constantes import *
from auxiliar import Auxiliar
from player import *


class Enemy(pygame.sprite.Sprite):    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,movimiento=False) -> None:
        super().__init__()
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,flip=True,scale=p_scale)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",0,6,scale=p_scale)
        self.die_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",0,6,flip=True,scale=p_scale)
        self.volar = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/VOLAR/{0}.png",0,15,flip=True,scale=1)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/ATTAK/ATTAK_00{0}.png",0,6,scale=p_scale)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/ATTAK/ATTAK_00{0}.png",0,6,flip=True,scale=p_scale)
        self.contador = 0
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 0
        self.move_y = 0

        self.movimiento=movimiento
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_dead = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.tiempo_muriendo = 0
        self.objetos_lanzados = pygame.sprite.Group()
        self.attack_cooldown = 3000 
        self.last_attack_time = pygame.time.get_ticks()
        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump


    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list, rect_y):
        self.tiempo_transcurrido_move += delta_ms
        if self.lives > 0:
            if self.movimiento and rect_y < 450:
                self.animation = self.volar
                self.direction=DIRECTION_L
                # Realizar cambios de posición aquí sin interferir con la animación
                if self.rect.y < rect_y:
                    self.change_y(2)  # Mover hacia abajo
                elif self.rect.y > rect_y:
                    self.change_y(-2)  # Mover hacia arriba
            else:
                if self.tiempo_transcurrido_move >= self.move_rate_ms:
                    self.tiempo_transcurrido_move = 0

                    if not self.is_on_plataform(plataform_list):
                        if self.move_y == 0:
                            self.is_fall = True
                            self.change_y(self.gravity)
                    else:
                        self.is_fall = False
                        self.change_x(self.move_x)
                        if self.contador <= 50:
                            self.move_x = -self.speed_walk
                            self.animation = self.walk_l
                            self.direction=DIRECTION_L
                            self.contador += 1
                        elif self.contador <= 100:
                            self.move_x = self.speed_walk
                            self.animation = self.walk_r
                            self.direction=DIRECTION_R
                            self.contador += 1
                        else:
                            self.contador = 0
        else:
            if self.movimiento:
                if self.rect.y < 700:
                    self.change_y(2)  # Descender en el eje Y
                else:
                    # Eliminar el enemigo de la lista de enemigos o del grupo de sprites
                    self.kill()

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms, enemy_list, index):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1           
            elif self.frame >= len(self.animation) - 1 :
                if self.lives <= 0:
                    del enemy_list[index]
                else:
                    self.frame=0
    def puede_atacar(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_attack_time
        return elapsed_time >= self.attack_cooldown

    def atacar(self, pause):
        if not pause:
            if self.puede_atacar():
                self.lanzar_objeto()
                self.last_attack_time = pygame.time.get_ticks()
    def lanzar_objeto(self):
        objeto = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.1,bandera=True,movimiento=self.movimiento)

        if self.direction == DIRECTION_R:
            objeto.velocidad_x = objeto.velocidad
        else:
            objeto.velocidad_x = -objeto.velocidad

        self.objetos_lanzados.add(objeto)

    def death_animation(self):
        if self.direction == DIRECTION_R:
            self.animation = self.die_r  # Asigna los sprites o imágenes de la animación de muerte hacia la derecha
        else:
            self.animation = self.die_l  # Asigna los sprites o imágenes de la animación de muerte hacia la izquierda

    def update(self,delta_ms,plataform_list,pause,rect_y,lista_enemigos,index,jugadores):
        if not pause:
            self.do_movement(delta_ms, plataform_list,rect_y)
            self.do_animation(delta_ms,lista_enemigos,index)
            self.atacar(pause)

    def draw(self,screen): 
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
    def receive_shoot(self,lista_enemigos):
        self.lives -= 1
        if self.lives <= 0:
            self.is_dead = True
            self.frame=0
            if not self.movimiento:
                lista_enemigos.remove(self)
                self.death_animation()  # Agrega esta línea para cambiar la animación a la de muerte
