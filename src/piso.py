import pygame
from config import *

class Piso(pygame.sprite.Sprite):
    def __init__(self, tamaño:tuple, ruta_img, medio_inferior:tuple):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(ruta_img).convert_alpha(), tamaño)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()

        self.rect.midbottom = medio_inferior
    
    def update(self, desplazamiento):
        self.rect.y += desplazamiento

        if(self.rect.top > HEIGHT):
            self.kill()
        


    
    