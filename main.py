import pygame
from constantes import *
from nivel import *

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ninja Game")

# Cargar las imágenes
background = pygame.image.load("images/gui/jungle/menu/bg.png").convert()
background = pygame.transform.scale(background, (ANCHO_VENTANA, ALTO_VENTANA))

header = pygame.image.load("images/gui/jungle/level_select/header.png")
header = pygame.transform.scale(header, (640, 200))
header_rect = header.get_rect(center=(730, 100))

main_frame = pygame.image.load("images/gui/jungle/you_win/bg.png")
main_frame = pygame.transform.scale(main_frame, (600, 650))
main_frame_rect = main_frame.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

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

level_1_number = pygame.image.load("images/gui/jungle/bubble/1.png")
level_2_number = pygame.image.load("images/gui/jungle/level_select/lock.png")
level_3_number = pygame.image.load("images/gui/jungle/level_select/lock.png")

level_1_number = pygame.transform.scale(level_1_number, (35, 70))
level_1_rect = pygame.Rect(560, 315, 90, 90)
level_2_number = pygame.transform.scale(level_2_number, (70, 70))
level_2_rect = pygame.Rect(705, 315, 90, 90)
level_3_number = pygame.transform.scale(level_3_number, (70, 70))
level_3_rect = pygame.Rect(855, 315, 90, 90)


def main():
    # Lógica del juego

    # Importar los niveles
    from nivel import nivel_1
    from nivel2 import nivel_2
    from nivel3 import nivel_3

    running = True
    current_level = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_1_rect.collidepoint(event.pos):
                    current_level = 1

        print(current_level)

        # Ejecutar el nivel seleccionado
        if current_level == 1:
            nivel_1()

        # Renderizar los elementos en la pantalla
        screen.blit(background, (0, 0))
        screen.blit(main_frame, main_frame_rect)
        screen.blit(level_table, level_table_rect)
        screen.blit(table_1_image, table_1_rect)
        screen.blit(table_2_image, table_2_rect)
        screen.blit(table_3_image, table_3_rect)
        screen.blit(level_1_number, level_1_rect)
        screen.blit(level_2_number, level_2_rect)
        screen.blit(level_3_number, level_3_rect)
        screen.blit(header, header_rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
