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

def victoria(screen,instancia_de_jugador):

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

    marco_3_image_victoria = pygame.image.load("images/gui/jungle/btn/next.png")
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
    score_text = font_score.render("{}".format(puntaje), True, (0, 0, 0))

    # Mostrar el puntaje en la pantalla
    

    screen.blit(marco_principal, marco_rect_principal)
    screen.blit(marco, marco_rect)
    screen.blit(marco_1_image_victoria, marco_1_rect_victoria)
    screen.blit(marco_2_image_victoria, marco_2_rect_victoria)
    screen.blit(marco_3_image_victoria, marco_3_rect_victoria)
    screen.blit(you_lose,rect_you_lose)
    screen.blit(ruta_imagen, rec_ruta_imagen)
    screen.blit(score_text_1, (680, 430))
    screen.blit(score_text, (700, 460))
    return marco_1_rect_victoria,marco_2_rect_victoria,marco_3_rect_victoria