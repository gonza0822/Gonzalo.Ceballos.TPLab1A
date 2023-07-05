import pygame
from piso import Piso
from config import *
from animaciones import animaciones_personaje

class Personaje(pygame.sprite.Sprite):
    def __init__(self, medio_piso:tuple, altura_maxima:int, piso:Piso, gravedad:float, plataformas, desplazamiento:int):
        super().__init__()

        self.animaciones = animaciones_personaje()
        self.indice = 2
        self.image = self.animaciones[self.indice]
        self.rect = self.image.get_rect()

        self.rect.midbottom = medio_piso 
        self.altura_maxima = altura_maxima
        self.piso = piso
        self.plataformas = plataformas
        self.desplazamiento = desplazamiento

        self.sonido_salto = pygame.mixer.Sound("./src/sonidos/salto.mp3")
        self.sonido_salto.set_volume(0.3)
        self.movimiento_x = 0
        self.movimiento_y = 0
        self.velocidad_y = 0
        self.gravedad = gravedad
        self.caigo_al_piso = True
        self.puntaje = 0

    def update(self):

        if(self.indice == 0):
            self.indice = 2
        elif(self.indice == 1):
            self.indice = 3

        self.desplazamiento = 0
        self.rect.x += self.movimiento_x

        if self.rect.right <= 0:
            self.rect.left = WIDTH
        elif self.rect.left >= WIDTH:
            self.rect.right = 0

        self.velocidad_y += self.gravedad
        self.movimiento_y += self.velocidad_y

        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(self.rect.x, self.rect.y + self.movimiento_y, self.rect.width, self.rect.height):
                if self.rect.bottom < plataforma.rect.centery:
                    if self.velocidad_y > 0:
                        self.rect.bottom = plataforma.rect.top
                        self.sonido_salto.play()
                        if(self.indice == 2):
                            self.indice = 0
                        else:
                            self.indice = 1
                        self.movimiento_y = 0
                        self.velocidad_y = -self.altura_maxima

        if(self.caigo_al_piso):
            if(self.rect.bottom + self.movimiento_y > (HEIGHT - self.piso.rect.height)):  
                self.movimiento_y = 0
                self.sonido_salto.play()
                if(self.indice == 2):
                    self.indice = 0
                else:
                    self.indice = 1
                self.velocidad_y = -self.altura_maxima
        
        if(self.rect.top <= ALTURA_DESPLAZAMIENTO):
            self.caigo_al_piso = False
            if(self.velocidad_y < 0):
                self.desplazamiento = -self.movimiento_y
        
        if(self.rect.top < ALTURA_DESPLAZAMIENTO):
            self.puntaje += 1

        self.rect.y += self.movimiento_y + self.desplazamiento
             
        self.movimiento_x = 0
        self.movimiento_y = 0

        self.image = self.animaciones[self.indice]

        return self.desplazamiento
                
