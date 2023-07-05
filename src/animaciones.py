import pygame

from config import *

def animaciones_personaje():
    animaciones = [pygame.transform.scale(pygame.image.load("./src/imagenes/personaje_parado_derecha.png").convert_alpha(), TAMAÑO_NINJA),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/personaje_parado_izquierda.png").convert_alpha(), TAMAÑO_NINJA),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/personaje_saltando_derecha.png").convert_alpha(), TAMAÑO_NINJA),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/personaje_saltando_izquierda.png").convert_alpha(), TAMAÑO_NINJA)]
    return animaciones


def animaciones_ave_nocturna():
    animaciones = [pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_0.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_1.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_2.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_3.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_4.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_5.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_6.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_7.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_8.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_9.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_10.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_11.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_12.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_13.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_14.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_aven_15.png").convert_alpha(), TAMAÑO_ENEMIGO)]
    return animaciones

def animaciones_ave():
    animaciones = [pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_0.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_1.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_2.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_3.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_4.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_5.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_6.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_7.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_8.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_9.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_10.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_11.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_12.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_13.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_14.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_ave_15.png").convert_alpha(), TAMAÑO_ENEMIGO)]
    return animaciones

def animaciones_nave():
    animaciones = [pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_0.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_1.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_2.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_3.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_4.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_5.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_6.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_7.png").convert_alpha(), TAMAÑO_ENEMIGO),
                    pygame.transform.scale(pygame.image.load("./src/imagenes/animacion_nave_8.png").convert_alpha(), TAMAÑO_ENEMIGO)]
    return animaciones