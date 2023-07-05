import pygame
from config import *
from animaciones import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,tipo_enemigo:str, posicion:tuple, plataforma):
        super().__init__()

        self.tipo_enemigo = tipo_enemigo
        if(tipo_enemigo == "ave"):
            self.animaciones = animaciones_ave()
        if(tipo_enemigo == "ave_nocturna"):
            self.animaciones = animaciones_ave_nocturna()
        if(tipo_enemigo == "nave"):
            self.animaciones = animaciones_nave()
        
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()

        self.rect.midbottom = posicion

        self.velocidad_x = VELOCIDAD_ENEMIGO
        self.plataforma = plataforma
    
    def update(self, desplazamiento):

        self.rect.x += self.velocidad_x
        if(self.rect.right > self.plataforma.rect.right + 60):
            self.velocidad_x = -VELOCIDAD_ENEMIGO
        elif(self.rect.left < self.plataforma.rect.left - 60):
            self.velocidad_x = VELOCIDAD_ENEMIGO

        if(self.velocidad_x < 0):
            if(self.tipo_enemigo == "nave"):
                if(self.indice > 5):
                    self.indice = 0
                self.indice += 1
                if(self.indice > 5):
                    self.indice = 0
            else:
                if(self.indice < 8):
                    self.indice = 8
                self.indice += 1
                if(self.indice > 15):
                    self.indice = 8
        else:
            if(self.tipo_enemigo == "nave"):
                if(self.indice < 5):
                    self.indice = 5
                self.indice += 1
                if(self.indice > 8):
                    self.indice = 5
            else:
                if(self.indice > 7):
                    self.indice = 0
                self.indice += 1
                if(self.indice > 7):
                    self.indice = 0

        self.image = self.animaciones[self.indice]

        self.rect.y += desplazamiento

        if(self.rect.top > HEIGHT):
            self.kill()