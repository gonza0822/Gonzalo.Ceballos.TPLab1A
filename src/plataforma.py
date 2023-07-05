import pygame
from config import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, tamaño:tuple, ruta_img:str, posicion:tuple, se_mueve:bool):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(ruta_img).convert_alpha(), tamaño)
        self.rect = self.image.get_rect()

        self.rect.center = posicion

        self.se_mueve = se_mueve
        self.velocidad_x = VELOCIDAD_PLATAFORMA
    
    def update(self, desplazamiento):
        
        if (self.se_mueve):
            self.rect.x += self.velocidad_x
            if(self.rect.right > WIDTH):
                self.velocidad_x = -VELOCIDAD_PLATAFORMA
                self.rect.right = WIDTH
            elif(self.rect.left < 0):
                self.velocidad_x = VELOCIDAD_PLATAFORMA
                self.rect.left = 0

        self.rect.y += desplazamiento

        if(self.rect.top > HEIGHT):
            self.kill()
        
            

