import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform
from estrella import Star
from enemigo import *
from main import main
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/set_bg_01/forest/image.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

def nivel_3():
    estrella = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    player_1 = Player(x=0, y=400, speed_walk=6, speed_run=12, gravity=14, jump_power=30, frame_rate_ms=100,
                      move_rate_ms=50, jump_height=140, p_scale=0.2, interval_time_jump=300, estrella=estrella,enemigos=enemigos)

    enemy_list = []
    enemy_list.append(Enemy(x=800, y=400, speed_walk=10, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
    enemy_list.append(Enemy(x=1000, y=400, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
    enemy_list.append(Enemy(x=1300, y=250, speed_walk=6, speed_run=8, gravity=0, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08,movimiento=True))
    enemy_list.append(Enemy(x=750, y=280, speed_walk=6, speed_run=8, gravity=8, frame_rate_ms=50,
                           move_rate_ms=50, jump_power=30, jump_height=140, p_scale=0.08))
    enemigos.add(enemy_list)

    plataform_list = []
    plataform_list.append(Plataform(x=100, y=500, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=150, y=500, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=200, y=500, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=250, y=500, width=50, height=50, type=14))
    plataform_list.append(Plataform(x=750, y=500, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=800, y=500, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=850, y=500, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=900, y=500, width=50, height=50, type=14))


    plataform_list.append(Plataform(x=900, y=430, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=950, y=430, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=1000, y=430, width=50, height=50, type=14))
    plataform_list.append(Plataform(x=320, y=430, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=350, y=430, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=400, y=430, width=50, height=50, type=14))
    plataform_list.append(Plataform(x=650, y=360, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=700, y=360, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=750, y=360, width=50, height=50, type=14))
    plataform_list.append(Plataform(x=470, y=360, width=50, height=50, type=12))
    plataform_list.append(Plataform(x=500, y=360, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=550, y=360, width=50, height=50, type=13))
    plataform_list.append(Plataform(x=600, y=360, width=50, height=50, type=14))

    star_list = []
    star_list.append(Star(x=610, y=280, width=50, height=50, type=1))
    star_list.append(Star(x=930, y=350, width=50, height=50, type=1))
    star_list.append(Star(x=470, y=510, width=50, height=50, type=1))

    estrella.add(star_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if marco_1_rect.collidepoint(event.pos):
                    main()
                if marco_2_rect.collidepoint(event.pos):
                    nivel_3()
                if marco_3_rect.collidepoint(event.pos):
                    player_1.pausa = False
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, imagen_fondo.get_rect())



        for plataforma in plataform_list:
            plataforma.draw(screen)

        for estrella in star_list:
            estrella.update(delta_ms)
            if estrella.active:
                rotated_image = pygame.transform.rotate(estrella.image, estrella.angle)
                rotated_rect = rotated_image.get_rect(center=estrella.rect.center)
                screen.blit(rotated_image, rotated_rect)

        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataform_list,player_1.pausa,player_1.rect.y, enemy_list, index)
            enemy.draw(screen)

        player_1.events(delta_ms, keys)
        player_1.update(delta_ms, plataform_list)
        player_1.draw(screen)
        player_1.objetos_lanzados.update()
        player_1.objetos_lanzados.draw(screen)
        font_score=pygame.font.SysFont("comicsans", 20, True)
        score_text = font_score.render("Score: " + str(player_1.puntaje), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        if player_1.pausa:
            marco = pygame.image.load(r"C:\Users\thiag\OneDrive\Escritorio\CLASE_23_inicio_juego\images\gui\jungle\level_select\table2.png")
            marco = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
            marco_rect = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

            marco_1_image = pygame.image.load(r"C:\Users\thiag\OneDrive\Escritorio\CLASE_23_inicio_juego\images\gui\jungle\menu\prize.png")
            marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
            marco_1_rect = pygame.Rect(490, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_2_image = pygame.image.load(r"C:\Users\thiag\OneDrive\Escritorio\CLASE_23_inicio_juego\images\gui\jungle\btn\restart.png")
            marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
            marco_2_rect = pygame.Rect(670, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

            marco_3_image = pygame.image.load(r"C:\Users\thiag\OneDrive\Escritorio\CLASE_23_inicio_juego\images\gui\jungle\menu\play.png")
            marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
            marco_3_rect = pygame.Rect(850, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
            
            screen.blit(marco, marco_rect)
            screen.blit(marco_1_image, marco_1_rect)
            screen.blit(marco_2_image, marco_2_rect)
            screen.blit(marco_3_image, marco_3_rect)
        pygame.display.flip()