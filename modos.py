import pygame
from constantes import *
def pause(screen):
    marco_1_image_nivel = pygame.image.load("images/gui/jungle/btn/menu.png")
    marco_1_image_nivel = pygame.transform.scale(marco_1_image_nivel, (100, 100))
    marco_1_rect_nivel = pygame.Rect(530, 160, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_nivel = pygame.image.load("images/gui/jungle/btn/restart.png")
    marco_2_image_nivel = pygame.transform.scale(marco_2_image_nivel, (100, 100))
    marco_2_rect_nivel = pygame.Rect(700, 160, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_3_image_nivel = pygame.image.load("images/gui/jungle/menu/play.png")
    marco_3_image_nivel = pygame.transform.scale(marco_3_image_nivel, (100, 100))
    marco_3_rect_nivel = pygame.Rect(880, 160, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
    
    screen.blit(marco_1_image_nivel, marco_1_rect_nivel)
    screen.blit(marco_2_image_nivel, marco_2_rect_nivel)
    screen.blit(marco_3_image_nivel, marco_3_rect_nivel)
    return marco_1_rect_nivel,marco_2_rect_nivel,marco_3_rect_nivel

def muerto(screen,instancia_de_jugador):
    ruta_imagen = pygame.image.load("images/gui/jungle/you_win/star_({0}).png".format(instancia_de_jugador.score)) 
    ruta_imagen = pygame.transform.scale(ruta_imagen, (300, 200))  # Ajusta el tamaño a 150x150 píxeles
    rec_ruta_imagen = ruta_imagen.get_rect(center=(740,275))

    you_lose = pygame.image.load("images/gui/jungle/you_lose/header.png")
    you_lose = pygame.transform.scale(you_lose, (640, 200))  # Ajusta el tamaño de la imagen según sea necesario
    rect_you_lose = you_lose.get_rect(center=(730, 100))

    marco_principal = pygame.image.load("images/gui/jungle/level_select/bg.png")
    marco_principal = pygame.transform.scale(marco_principal, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
    marco_rect_principal = marco_principal.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

    marco = pygame.image.load("images/gui/jungle/level_select/table2.png")
    marco = pygame.transform.scale(marco, (550, 350))  # Ajusta el tamaño de la imagen según sea necesario
    marco_rect = marco.get_rect(center=(740, 270))
    
    marco_1_image_derrota = pygame.image.load("images/gui/jungle/btn/menu.png")
    marco_1_image_derrota = pygame.transform.scale(marco_1_image_derrota, (100, 100))
    marco_1_rect_derrota = pygame.Rect(630, 450, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_derrota = pygame.image.load("images/gui/jungle/btn/restart.png")
    marco_2_image_derrota = pygame.transform.scale(marco_2_image_derrota, (100, 100))
    marco_2_rect_derrota = pygame.Rect(770, 450, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
    
    screen.blit(marco_principal, marco_rect_principal)
    screen.blit(marco, marco_rect)
    screen.blit(marco_1_image_derrota, marco_1_rect_derrota)
    screen.blit(marco_2_image_derrota, marco_2_rect_derrota)
    screen.blit(you_lose,rect_you_lose)
    screen.blit(ruta_imagen, rec_ruta_imagen)
    return marco_1_rect_derrota,marco_2_rect_derrota

def victoria(screen,instancia_de_jugador,bandera=False):

    ruta_imagen = pygame.image.load("images/gui/jungle/you_win/star_({0}).png".format(instancia_de_jugador.score)) 
    ruta_imagen = pygame.transform.scale(ruta_imagen, (300, 200))  # Ajusta el tamaño a 150x150 píxeles
    rec_ruta_imagen = ruta_imagen.get_rect(center=(740,275))

    you_lose = pygame.image.load("images/gui/jungle/you_win/header.png")
    you_lose = pygame.transform.scale(you_lose, (640, 200))  # Ajusta el tamaño de la imagen según sea necesario
    rect_you_lose = you_lose.get_rect(center=(730, 100))

    marco_principal = pygame.image.load("images/gui/jungle/you_win/bg.png")
    marco_principal = pygame.transform.scale(marco_principal, (600, 650))  # Ajusta el tamaño de la imagen según sea necesario
    marco_rect_principal = marco_principal.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

    marco = pygame.image.load("images/gui/jungle/level_select/table2.png")
    marco = pygame.transform.scale(marco, (550, 500))  # Ajusta el tamaño de la imagen según sea necesario
    marco_rect = marco.get_rect(center=(740, 350))

    marco_1_image_victoria = pygame.image.load("images/gui/jungle/btn/menu.png")
    marco_1_image_victoria = pygame.transform.scale(marco_1_image_victoria, (100, 100))
    marco_1_rect_victoria = pygame.Rect(510, 590, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_victoria = pygame.image.load("images/gui/jungle/btn/restart.png")
    marco_2_image_victoria = pygame.transform.scale(marco_2_image_victoria, (100, 100))
    marco_2_rect_victoria = pygame.Rect(680, 590, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
    if not bandera:
        marco_3_image_victoria = pygame.image.load("images/gui/jungle/btn/next.png")
    else:
        marco_3_image_victoria = pygame.image.load("images/gui/jungle/btn/close.png")
    marco_3_image_victoria = pygame.transform.scale(marco_3_image_victoria, (100, 100))
    marco_3_rect_victoria = pygame.Rect(860, 590, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
    
    # Crear la fuente para el texto del puntaje
    font_score_1 = pygame.font.SysFont("comicsans", 20, True)
    score_text_1 = font_score_1.render("You Score ", True, (0, 0, 0))

    # Mostrar el texto del puntaje en la pantalla
    

    # Obtener el puntaje de la instancia del jugador (asumiendo que instancia_de_jugador.puntaje es válido)
    puntaje = instancia_de_jugador.puntaje

    # Crear la fuente para el puntaje
    font_score = pygame.font.SysFont("comicsans", 50, True)
    score_text = font_score.render("{0}".format(puntaje), True, (0, 0, 0))

    # Mostrar el puntaje en la pantalla
    

    screen.blit(marco_principal, marco_rect_principal)
    screen.blit(marco, marco_rect)
    screen.blit(marco_1_image_victoria, marco_1_rect_victoria)
    screen.blit(marco_2_image_victoria, marco_2_rect_victoria)
    screen.blit(marco_3_image_victoria, marco_3_rect_victoria)
    screen.blit(you_lose,rect_you_lose)
    screen.blit(ruta_imagen, rec_ruta_imagen)
    screen.blit(score_text_1, (695, 430))
    screen.blit(score_text, (700, 460))
    return marco_1_rect_victoria,marco_2_rect_victoria,marco_3_rect_victoria

def menu_select_level(screen,victoria_lv1,victoria_lv2):


    main_frame = pygame.image.load("images/gui/jungle/you_win/bg.png")
    main_frame = pygame.transform.scale(main_frame, (600, 650))
    main_frame_rect = main_frame.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

    header = pygame.image.load("images/gui/jungle/level_select/header.png")
    header = pygame.transform.scale(header, (640, 200))
    header_rect = header.get_rect(center=(730, 100))

    level_table = pygame.image.load("images/gui/jungle/level_select/table2.png")
    level_table = pygame.transform.scale(level_table, (490, 600))
    level_table_rect = level_table.get_rect(center=(740, 390))

    table_1_image = pygame.image.load("images/gui/jungle/level_select/table.png")
    table_1_image = pygame.transform.scale(table_1_image, (100, 100))
    table_1_rect = pygame.Rect(530, 300, 90, 90)

    table_2_image = pygame.image.load("images/gui/jungle/level_select/table.png")
    table_2_image = pygame.transform.scale(table_2_image, (100, 100))
    table_2_rect = pygame.Rect(690, 300, 90, 90)

    table_3_image = pygame.image.load("images/gui/jungle/level_select/table.png")
    table_3_image = pygame.transform.scale(table_3_image, (100, 100))
    table_3_rect = pygame.Rect(840, 300, 90, 90)
    if not victoria_lv1:
        level_1_number = pygame.image.load("images/gui/jungle/bubble/1.png")
        level_2_number = pygame.image.load("images/gui/jungle/level_select/lock.png")
        level_3_number = pygame.image.load("images/gui/jungle/level_select/lock.png")
    elif victoria_lv2:
        level_1_number = pygame.image.load("images/gui/jungle/bubble/1.png")
        level_2_number = pygame.image.load("images/gui/jungle/bubble/2.png")
        level_3_number = pygame.image.load("images/gui/jungle/bubble/3.png")
    else:
        level_1_number = pygame.image.load("images/gui/jungle/bubble/1.png")
        level_2_number = pygame.image.load("images/gui/jungle/bubble/2.png")
        level_3_number = pygame.image.load("images/gui/jungle/level_select/lock.png")

    level_1_number = pygame.transform.scale(level_1_number, (35, 70))
    level_1_rect = pygame.Rect(560, 315, 90, 90)
    level_2_number = pygame.transform.scale(level_2_number, (70, 70))
    level_2_rect = pygame.Rect(705, 315, 90, 90)
    level_3_number = pygame.transform.scale(level_3_number, (70, 70))
    level_3_rect = pygame.Rect(855, 315, 90, 90)

    screen.blit(main_frame, main_frame_rect)
    screen.blit(level_table, level_table_rect)
    screen.blit(table_1_image, table_1_rect)
    screen.blit(table_2_image, table_2_rect)
    screen.blit(table_3_image, table_3_rect)
    screen.blit(level_1_number, level_1_rect)
    screen.blit(level_2_number, level_2_rect)
    screen.blit(level_3_number, level_3_rect)
    screen.blit(header, header_rect)
    return table_1_rect,table_2_rect,table_3_rect