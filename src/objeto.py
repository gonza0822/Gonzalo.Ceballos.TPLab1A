import pygame
from config import *

class Objeto(pygame.sprite.Sprite):
    def __init__(self, tamaño:tuple, posicion:tuple, es_vida:bool):
        super().__init__()
        self.es_vida = es_vida
        if(self.es_vida):
            self.image = pygame.transform.scale(pygame.image.load("./src/imagenes/item_vida.png").convert_alpha(), tamaño)
        else:
            self.image = pygame.transform.scale(pygame.image.load("./src/imagenes/item_armadura.png").convert_alpha(), tamaño)
        self.rect = self.image.get_rect()

        self.rect.midbottom = posicion
    
    def update(self, desplazamiento):

        self.rect.y += desplazamiento

        if(self.rect.top > HEIGHT):
            self.kill()