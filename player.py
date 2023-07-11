import pygame
from constantes import *
from auxiliar import Auxiliar
from score import Star_Score
from estrella import *
from katana import Objeto
from enemigo import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,estrella=None,enemigos= None) -> None:
        super().__init__()
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''

        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Idle ({0}).png",1,10,flip=False,scale=0.4)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Idle ({0}).png",1,10,flip=True,scale=0.4)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Walk ({0}).png",0,9,flip=False,scale=0.4)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Walk ({0}).png",0,9,flip=True,scale=0.4)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Walk ({0}).png",0,9,flip=False,scale=0.4)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Walk ({0}).png",0,9,flip=True,scale=0.4)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Shoot ({0}).png",1,5,flip=False,scale=0.4)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Shoot ({0}).png",1,5,flip=True,scale=0.4)
        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Dead ({0}).png",0,9,flip=False,scale=0.4)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/ninja/Dead ({0}).png",0,9,flip=True,scale=0.4)
        self.enemigos=enemigos
        self.frame = 0
        self.lives = 6
        self.score = 0
        self.move_x = 0
        self.move_y = 0
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
        self.estrella=estrella
        self.objetos_lanzados = pygame.sprite.Group()
        self.attack_launched = False
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_dead = False
        self.pausa = False
        self.victoria_1 = False
        self.puntaje = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.invulnerable = False  # Variable de estado de invulnerabilidad
        self.invulnerable_timer = 0  # Temporizador de invulnerabilidad
        self.invulnerable_duration = 600  # Duración en milisegundos de la invulnerabilidad
    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False and not self.is_dead):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                    
                else:
                    self.animation = self.knife_l
    def lanzar_objeto(self):
        objeto = Objeto(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.1)

        if self.direction == DIRECTION_R:
            objeto.velocidad_x = objeto.velocidad
        else:
            objeto.velocidad_x = -objeto.velocidad

        self.objetos_lanzados.add(objeto)
                                

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l and not self.is_dead):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms and not self.is_dead):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

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

    def do_animation(self,delta_ms,player):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            elif self.frame >= len(self.animation) - 1 :
                if self.animation==self.dead_r or self.animation==self.dead_l:
                    del player
                else:
                    self.frame=0
            

    def dibujar_estrella(self,screen):
        score=self.score
        lives=self.lives
        if not self.is_dead and not self.score==3:
            ruta_imagen = pygame.image.load("images/gui/jungle/you_win/star_({0}).png".format(score)) 
            imagen_escala = pygame.transform.scale(ruta_imagen, (150, 150))  # Ajusta el tamaño a 150x150 píxeles
            ruta_imagen2 = pygame.image.load("images/caracters/players/ninja/Heart ({0}).png".format(lives)) 
            imagen_escala2 = pygame.transform.scale(ruta_imagen2, (400, 150))  # Ajusta el tamaño a 100x100 píxeles
            screen.blit(imagen_escala, (1325, 10))
            screen.blit(imagen_escala2, (550, 10))

 
    def update(self, delta_ms, plataform_list, lista_enemigos,player):
        if not self.pausa:
            self.do_movement(delta_ms, plataform_list)
            self.do_animation(delta_ms,player)
        if self.lives<=0:
            self.is_dead=True
            if self.direction == DIRECTION_R:
                self.animation = self.dead_r  # Asigna los sprites o imágenes de la animación de muerte hacia la derecha
            else:
                self.animation = self.dead_l  # Asigna los sprites o imágenes de la animación de muerte hacia la izquierda

        colisiones = pygame.sprite.spritecollide(self, self.estrella, True)
        if colisiones:
            estrella = colisiones[0]  # Tomamos la primera estrella en caso de colisión múltiple
            self.score += 1
            self.puntaje += 10
            estrella.desactive()
            self.estrella.remove(estrella)
            return self.score

        for objeto in self.objetos_lanzados:
            colisiones_enemigos = pygame.sprite.spritecollide(objeto, self.enemigos, False)
            if colisiones_enemigos:
                for enemigo in colisiones_enemigos:
                    enemigo.receive_shoot(self.enemigos)
                    self.attack_launched = False
                    objeto.kill()
                    self.puntaje += 10
        if not self.is_dead and not self.score==3:
            for enemy in lista_enemigos:
                for objeto in enemy.objetos_lanzados:
                    if self.collition_rect.colliderect(objeto.rect):                       
                        objeto.kill()
                        self.lives -= 1

    def is_colliding_enemy(self):
        colisiones = pygame.sprite.spritecollide(self, self.enemigos, False)
        return len(colisiones) > 0
                
            
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
        self.dibujar_estrella(screen)
    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not self.pausa and not self.is_dead):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not self.pausa and not self.is_dead):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not self.is_dead):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not self.is_dead):
            self.stay()  

        if(keys[pygame.K_SPACE] and not self.pausa and not self.is_dead):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido 
        if not self.is_colliding_enemy():  # Verificar colisión con enemigos
            if(keys[pygame.K_z] and not self.attack_launched and not self.pausa and not self.is_dead):
                self.knife()
                self.lanzar_objeto()
                self.attack_launched = True

        if(not keys[pygame.K_z]):
            self.knife(False)

        if keys[pygame.K_ESCAPE] :
           self.pausa = True



