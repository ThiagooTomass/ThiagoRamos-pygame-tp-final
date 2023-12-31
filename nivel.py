import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform
from estrella import Star
from enemigo import *
from main import main
from modos import *
from nivel2 import *
import json
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/set_bg_01/forest/image.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

def nivel_1():
    estrella = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()

    player_1 = Player(x=0, y=400, speed_walk=6, speed_run=12, gravity=14, jump_power=30, frame_rate_ms=100,
                      move_rate_ms=50, jump_height=140, p_scale=0.2, interval_time_jump=300, estrella=estrella,enemigos=enemigos)
    jugadores.add(player_1)
    enemy_list = []
    enemy_list.append(Enemy(x=800, y=450, speed_walk=10, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08,movimiento=False))
    enemy_list.append(Enemy(x=1000, y=450, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08,movimiento=False))
    enemy_list.append(Enemy(x=750, y=280, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08,movimiento=False))
    enemy_list.append(Enemy(x=1300, y=250, speed_walk=6, speed_run=8, gravity=0, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08,movimiento=True))
    enemigos.add(enemy_list)

    with open("nivel1.json", "r") as archivo:
        contenido_json = json.load(archivo)

    # Obtener las plataformas del nivel 1
    plataformas_nivel_1 = contenido_json["plataformas"]

    # Crear una lista de plataformas
    plataformas = []

    # Recorrer las plataformas del nivel 1
    for plataforma in plataformas_nivel_1:
        x = plataforma["x"]
        y = plataforma["y"]
        width = plataforma["width"]
        height = plataforma["height"]
        type = plataforma["type"]

    #Crear la plataforma y agregarla a la lista
        nueva_plataforma = Plataform(x, y, width, height, type)
        plataformas.append(nueva_plataforma)


    star_list = []
    star_list.append(Star(x=610, y=280, width=50, height=50, type=1))
    star_list.append(Star(x=930, y=350, width=50, height=50, type=1))
    star_list.append(Star(x=470, y=510, width=50, height=50, type=1))

    estrella.add(star_list)

    marco_1_rect_nivel = None
    marco_2_rect_nivel = None
    marco_3_rect_nivel = None
    marco_1_rect_victoria = None
    marco_2_rect_victoria = None
    marco_3_rect_victoria = None
    marco_1_rect_derrota = None
    marco_2_rect_derrota = None
    marco_lv_1 = None
    marco_lv_2 = None
    marco_lv_3 = None
    bandera_lv=False

    global victoria_lv_1
    global victoria_lv_2
    global victoria_lv_3
    victoria_lv1=False
    victoria_lv2=False
    victoria_lv3=False

    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if marco_1_rect_nivel is not None :
                    
                    if marco_1_rect_nivel.collidepoint(event.pos):
                        bandera_lv=True
                    if marco_2_rect_nivel.collidepoint(event.pos):
                        nivel_1()
                    if marco_3_rect_nivel.collidepoint(event.pos):
                        player_1.pausa = False
                        
                if marco_1_rect_derrota is not None:
                    if marco_1_rect_derrota.collidepoint(event.pos):
                        bandera_lv=True
                    if marco_2_rect_derrota.collidepoint(event.pos):
                        nivel_1()
                        player_1.frame = 0

                if marco_1_rect_victoria is not None :                    
                    if marco_1_rect_victoria.collidepoint(event.pos):
                        bandera_lv=True
                    if marco_2_rect_victoria.collidepoint(event.pos):
                        nivel_1()
                    if marco_3_rect_victoria.collidepoint(event.pos):
                        nivel_2()
                if marco_lv_1 is not None :
                    if victoria_lv1:
                        if marco_lv_1.collidepoint(event.pos):
                            nivel_1()
                        if marco_lv_2.collidepoint(event.pos):
                            nivel_2() 
                    else:
                        if marco_lv_1.collidepoint(event.pos):
                            nivel_1()                                              

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, imagen_fondo.get_rect())

        for plataforma in plataformas:
            plataforma.draw(screen)

        for estrella in star_list:
            estrella.update(delta_ms)
            if estrella.active:
                rotated_image = pygame.transform.rotate(estrella.image, estrella.angle)
                rotated_rect = rotated_image.get_rect(center=estrella.rect.center)
                screen.blit(rotated_image, rotated_rect)

        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataformas,player_1.pausa,player_1.rect.y, enemy_list, index)
            enemy.draw(screen)
            if not player_1.pausa:
                enemy.objetos_lanzados.update(player_1.pausa)
            enemy.objetos_lanzados.draw(screen)

        player_1.events(delta_ms, keys)
        player_1.update(delta_ms, plataformas,enemy_list,player_1)
        player_1.draw(screen)
        player_1.objetos_lanzados.update(player_1.pausa)
        player_1.objetos_lanzados.draw(screen)

        font_score=pygame.font.SysFont("comicsans", 20, True)
        score_text = font_score.render("Score: " + str(player_1.puntaje), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        

        if player_1.pausa and player_1.lives > 0:
            marco_1_rect_nivel, marco_2_rect_nivel, marco_3_rect_nivel = pause(screen)
        
        if player_1.lives <= 0:
            marco_1_rect_derrota,marco_2_rect_derrota = muerto(screen,player_1)
        if player_1.score==3:
            victoria_lv1=True
            marco_1_rect_victoria, marco_2_rect_victoria, marco_3_rect_victoria = victoria(screen,player_1)
        if bandera_lv:
            marco_lv_1,marco_lv_2,marco_lv_3 = menu_select_level(screen,victoria_lv1,victoria_lv2)        
        pygame.display.flip()


