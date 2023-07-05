import pygame
import sys
import random

from config import *
from personaje import Personaje
from piso import Piso
from plataforma import Plataforma
from enemigo import Enemigo
from objeto import Objeto

class Juego:
    def __init__(self):
        pygame.init()

        self.reloj = pygame.time.Clock()

        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jumper")

        self.fondo = pygame.transform.scale(pygame.image.load("./src/imagenes/fondo_cielo.png").convert(), (WIDTH, HEIGHT))

        self.fuente_titulo = pygame.font.Font("./src/fuente de texto/NoticiaText-Regular.ttf", 48)
        self.fuente_chica = pygame.font.Font("./src/fuente de texto/NoticiaText-Regular.ttf", 20)
        self.fuente_grande = pygame.font.Font("./src/fuente de texto/NoticiaText-Regular.ttf", 24)

        self.sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.objetos = pygame.sprite.Group()

        self.archivo_puntaje = "./src/puntaje.txt"

        with open(self.archivo_puntaje, "r") as archivo:
            self.max_puntaje = int(archivo.read())

        self.vidas = 3
        self.armadura = False

        self.desplazamiento = 0
        self.desplazamiento_fondo = 0
        self.referencia_plataforma = False
        self.menu = True
        self.menu_mapas = False
        self.juego_terminado = False
        self.juego_pausado = False
        self.posicion_x_vidas = 0
        self.posicion_y_boton = 0
        self.boton_jugar = 0
        self.boton_salir = 0
        self.boton_salir_menu = 0
        self.boton_continuar = 0
        self.boton_reiniciar = 0
        self.boton_sonido = 0
        self.estado_sonido = True
        self.mapa_cielo = 0
        self.mapa_espacio = 0
        self.mapa_nada = 0
        self.img_plataforma = 0 
        self.tipo_enemigo= 0
        self.puntaje_momento_armadura = 0

        self.sonido_juego = pygame.mixer.Sound("./src/sonidos/juego.mp3")
        self.sonido_juego.set_volume(0.3)
        self.activar_sonido = False

        self.sonido_choque = pygame.mixer.Sound("./src/sonidos/choque.mp3")
        self.sonido_choque.set_volume(0.3)

        self.sonido_item = pygame.mixer.Sound("./src/sonidos/item.mp3")
        self.sonido_choque.set_volume(0.3)

    
    def jugar(self):
        while True:
            self.reloj.tick(FPS)
            self.manejar_eventos()
            if not self.juego_terminado and not self.menu and not self.menu_mapas and not self.juego_pausado:
                self.actualizar()
            self.renderizar()

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if(self.menu):
                    if(self.boton_jugar.collidepoint(pygame.mouse.get_pos())):
                        self.menu_mapas = True
                        self.menu = False
                    elif(self.boton_salir.collidepoint(pygame.mouse.get_pos())):
                        pygame.quit()
                        sys.exit()
                    elif(self.boton_sonido.collidepoint(pygame.mouse.get_pos())):
                        if(self.estado_sonido == True):
                            self.estado_sonido = False
                        else:
                            self.estado_sonido = True
                elif(not self.menu and self.menu_mapas):
                    if(self.boton_salir_menu.collidepoint(pygame.mouse.get_pos())):
                        self.menu_mapas = False
                        self.menu = True
                    elif(self.mapa_cielo.collidepoint(pygame.mouse.get_pos())):
                        self.fondo = pygame.transform.scale(pygame.image.load("./src/imagenes/fondo_cielo.png").convert(), (WIDTH, HEIGHT))
                        self.img_plataforma = "./src/imagenes/plataforma_cielo.png"
                        self.tipo_enemigo= "ave"
                        self.img_piso = "./src/imagenes/plataforma_piso_cielo.png"
                        self.piso = Piso(TAMAÑO_PISO, self.img_piso, MEDIO_INFERIOR)
                        self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso,GRAVEDAD, self.plataformas, self.desplazamiento)
                        self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                        self.sprites.add(self.piso)
                        self.menu_mapas = False
                    elif(self.mapa_espacio.collidepoint(pygame.mouse.get_pos())):
                        self.fondo = pygame.transform.scale(pygame.image.load("./src/imagenes/fondo_espacio.png").convert(), (WIDTH, HEIGHT))
                        self.img_plataforma = "./src/imagenes/plataforma_espacio.png"
                        self.tipo_enemigo= "nave"
                        self.img_piso = "./src/imagenes/plataforma_piso_espacio.png"
                        self.piso = Piso(TAMAÑO_PISO, self.img_piso, MEDIO_INFERIOR)
                        self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso,GRAVEDAD, self.plataformas, self.desplazamiento)
                        self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                        self.sprites.add(self.piso)
                        self.menu_mapas = False
                    elif(self.mapa_nada.collidepoint(pygame.mouse.get_pos())):
                        self.fondo = pygame.transform.scale(pygame.image.load("./src/imagenes/fondo_noche.png").convert(), (WIDTH, HEIGHT))
                        self.img_plataforma = "./src/imagenes/plataforma_cielo.png"
                        self.tipo_enemigo= "ave_nocturna"
                        self.img_piso = "./src/imagenes/plataforma_piso_cielo.png"
                        self.piso = Piso(TAMAÑO_PISO, self.img_piso, MEDIO_INFERIOR)
                        self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso,GRAVEDAD, self.plataformas, self.desplazamiento)
                        self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                        self.sprites.add(self.piso)
                        self.menu_mapas = False
                elif(self.juego_pausado):
                    if(self.boton_continuar.collidepoint(pygame.mouse.get_pos())):
                        self.juego_pausado = False
                    elif(self.boton_reiniciar.collidepoint(pygame.mouse.get_pos())):
                        self.vidas = 3
                        self.personaje.puntaje = 0
                        self.plataformas.empty() 
                        self.enemigos.empty() 
                        self.objetos.empty() 
                        self.piso = Piso(TAMAÑO_PISO, self.img_plataforma, MEDIO_INFERIOR)
                        self.desplazamiento = 0
                        self.desplazamiento_fondo = 0
                        self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso, GRAVEDAD, self.plataformas, self.desplazamiento)
                        self.referencia_plataforma = False
                        self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                        self.juego_pausado = False
                        self.sprites.add(self.piso)
                        pygame.time.delay(200)
                    elif(self.boton_salir_menu.collidepoint(pygame.mouse.get_pos())):
                        self.juego_pausado = False
                        self.menu_mapas = False
                        self.menu = True
                        self.vidas = 3
                        self.plataformas.empty() 
                        self.enemigos.empty() 
                        self.objetos.empty() 
                    elif(self.boton_sonido.collidepoint(pygame.mouse.get_pos())):
                        if(self.estado_sonido == True):
                            self.estado_sonido = False
                        else:
                            self.estado_sonido = True
                elif(self.juego_terminado):
                    if(self.boton_reiniciar.collidepoint(pygame.mouse.get_pos())):
                        self.vidas = 3
                        self.personaje.puntaje = 0
                        self.plataformas.empty() 
                        self.enemigos.empty() 
                        self.objetos.empty() 
                        self.piso = Piso(TAMAÑO_PISO, self.img_piso, MEDIO_INFERIOR)
                        self.desplazamiento = 0
                        self.desplazamiento_fondo = 0
                        self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso, GRAVEDAD, self.plataformas, self.desplazamiento)
                        self.referencia_plataforma = False
                        self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                        self.juego_terminado = False
                        self.sprites.add(self.piso)
                        pygame.time.delay(200)
                    elif(self.boton_salir_menu.collidepoint(pygame.mouse.get_pos())):
                        self.menu = True
                        self.juego_terminado = False
                        self.vidas = 3
                        self.plataformas.empty() 
                        self.enemigos.empty() 
                        self.objetos.empty() 
        key = pygame.key.get_pressed()
        if(key[pygame.K_LEFT]):
            self.personaje.movimiento_x = -VELOCIDAD_PERSONAJE
            self.personaje.indice = 3
        if(key[pygame.K_RIGHT]):
            self.personaje.movimiento_x = VELOCIDAD_PERSONAJE
            self.personaje.indice = 2
        if(key[pygame.K_p]):
            self.juego_pausado = True
        if(self.juego_terminado):
            if(key[pygame.K_SPACE]):
                self.vidas = 3
                self.personaje.puntaje = 0
                self.plataformas.empty() 
                self.enemigos.empty() 
                self.objetos.empty() 
                self.piso = Piso(TAMAÑO_PISO, self.img_plataforma, MEDIO_INFERIOR)
                self.desplazamiento = 0
                self.desplazamiento_fondo = 0
                self.personaje = Personaje(MEDIO_PISO, ALTURA_MAXIMA, self.piso, GRAVEDAD, self.plataformas, self.desplazamiento)
                self.referencia_plataforma = False
                self.plataforma_generada = Plataforma((40, 10), self.img_plataforma, (0, HEIGHT), False)
                self.juego_terminado = False
                self.sprites.add(self.piso)
                pygame.time.delay(200)

    def actualizar(self):
        lista_obtener_objetos = pygame.sprite.spritecollide(self.personaje, self.objetos, True)
        if(len(lista_obtener_objetos) == 1):
            self.sonido_item.play()
            if(lista_obtener_objetos[0].es_vida):
                self.vidas += 1
            else:
                self.armadura = True
                self.puntaje_momento_armadura = self.personaje.puntaje
        if(self.personaje.puntaje > self.puntaje_momento_armadura + 500):
            self.armadura = False
        lista_choque_con_enemigos = pygame.sprite.spritecollide(self.personaje, self.enemigos, True)
        if(len(lista_choque_con_enemigos) == 1):
            self.sonido_choque.play()
            if(not self.armadura):
                self.vidas -= 1
        self.generar_plataformas()
        self.perdiste()
        self.desplazamiento = self.personaje.update()   
        self.sprites.update(self.desplazamiento)

    def renderizar(self):
        if(self.menu):
            self.pantalla.fill(COLOR_NEGRO)
            titulo = self.fuente_titulo.render("JUMPER", True, COLOR_BLANCO)
            self.pantalla.blit(titulo, (WIDTH/2 - titulo.get_width()/2, 20))
            for i in range(2):
                match(i):
                    case 0:
                        texto = "JUGAR"
                    case 1:
                        texto = "SALIR"
                self.generar_boton(texto, self.fuente_grande, COLOR_BLANCO, 150, 50, 200, (255,0,0))
                self.posicion_y_boton += 100
            self.posicion_y_boton = 0
            self.boton_sonido = pygame.rect.Rect(WIDTH - 20,HEIGHT - 20, 20,20)   
            if(self.estado_sonido):
                pygame.draw.rect(self.pantalla, (255,255,255), self.boton_sonido)
                imagen_sonido = pygame.transform.scale(pygame.image.load("./src/imagenes/sonido_on.png").convert_alpha(), (20,20))
                self.pantalla.blit(imagen_sonido, (WIDTH-20, HEIGHT-20))
                if(not self.activar_sonido):
                    self.activar_sonido = True
                    self.sonido_juego.play(-1, 0)
            else:
                pygame.draw.rect(self.pantalla, (255,255,255), self.boton_sonido)
                imagen_sonido = pygame.transform.scale(pygame.image.load("./src/imagenes/sonido_off.png").convert_alpha(), (20,20))
                self.pantalla.blit(imagen_sonido, (WIDTH-20, HEIGHT-20))
                self.sonido_juego.stop()
                self.activar_sonido = False
        elif(self.menu_mapas):
            self.pantalla.fill(COLOR_NEGRO)
            for i in range(4):
                match(i):
                    case 0:
                        color = "rojo"
                        ruta_img = "./src/imagenes/fondo_cielo.png"
                    case 1:
                        color = "verde"
                        ruta_img = "./src/imagenes/fondo_espacio.png"
                    case 2:
                        color = "azul"
                        ruta_img = "./src/imagenes/fondo_noche.png"
                    case 3:
                        texto = "SALIR"
                if(i == 0 or i == 1 or i == 2):
                    self.generar_boton_img(ruta_img,90, 90,90, color)
                else:
                    self.generar_boton("SALIR AL MENU", self.fuente_grande, COLOR_BLANCO, 200,50,100, (255,0,0))
                self.posicion_y_boton += 120
            self.posicion_y_boton = 0
        elif(self.juego_pausado):
            self.pantalla.fill(COLOR_NEGRO)
            for i in range(3):
                match(i):
                    case 0:
                        texto = "CONTINUAR"
                    case 1:
                        texto = "REINICIAR"
                    case 2:
                        texto = "SALIR AL MENU"
                self.generar_boton(texto, self.fuente_grande, COLOR_BLANCO, 200, 50, 200, (255,0,0))
                self.posicion_y_boton += 100
            self.posicion_y_boton = 0
            self.boton_sonido = pygame.rect.Rect(WIDTH - 20,HEIGHT - 20, 20,20)   
            if(self.estado_sonido):
                pygame.draw.rect(self.pantalla, (255,255,255), self.boton_sonido)
                imagen_sonido = pygame.transform.scale(pygame.image.load("./src/imagenes/sonido_on.png").convert_alpha(), (20,20))
                self.pantalla.blit(imagen_sonido, (WIDTH-20, HEIGHT-20))
                if(not self.activar_sonido):
                    self.activar_sonido = True
                    self.sonido_juego.play(-1, 0)
            else:
                pygame.draw.rect(self.pantalla, (255,255,255), self.boton_sonido)
                imagen_sonido = pygame.transform.scale(pygame.image.load("./src/imagenes/sonido_off.png").convert_alpha(), (20,20))
                self.pantalla.blit(imagen_sonido, (WIDTH-20, HEIGHT-20))
                self.sonido_juego.stop()
                self.activar_sonido = False
        else:
            self.dibujar_fondo(self.desplazamiento)
            self.pantalla.blit(self.piso.image, self.piso.rect)
            self.pantalla.blit(self.personaje.image, self.personaje.rect)
            self.generar_texto(f'Puntaje: {self.personaje.puntaje}', self.fuente_chica, COLOR_BLANCO, (WIDTH - 150, 0))
            for plataforma in self.plataformas:
                self.pantalla.blit(plataforma.image, plataforma.rect)
            for enemigo in self.enemigos:
                self.pantalla.blit(enemigo.image,enemigo.rect)
            for objeto in self.objetos:
                self.pantalla.blit(objeto.image,objeto.rect)
            if(self.vidas > 4):
                self.vidas = 4
            for i in range(self.vidas):
                imagen_vidas = pygame.transform.scale(pygame.image.load("./src/imagenes/vidas.png").convert_alpha(), (20, 20))
                self.pantalla.blit(imagen_vidas, (self.posicion_x_vidas, 0))
                self.posicion_x_vidas += 30
            self.posicion_x_vidas = 0
            if(self.armadura):
                imagen_armadura = pygame.transform.scale(pygame.image.load("./src/imagenes/item_armadura.png").convert_alpha(), (20, 20))
                self.pantalla.blit(imagen_armadura, (WIDTH/2-10, 0))
        if(self.juego_terminado):
            self.armadura = False
            self.pantalla.fill(COLOR_NEGRO)
            self.generar_texto("PERDISTE!", self.fuente_grande, COLOR_BLANCO, (150,100))
            self.generar_texto(f'MAX SCORE: {str(self.max_puntaje)}', self.fuente_grande, COLOR_BLANCO, (150,150))
            self.generar_texto(f'PUNTAJE: {str(self.personaje.puntaje)}', self.fuente_grande, COLOR_BLANCO, (150,200))
            for i in range(2):
                match(i):
                    case 0:
                        texto = "VOLVER A JUGAR"
                    case 1:
                        texto = "SALIR AL MENU"
                self.generar_boton(texto, self.fuente_grande, COLOR_BLANCO, 200, 50, 300, (255,0,0))
                self.posicion_y_boton += 100
            self.posicion_y_boton = 0
        pygame.display.flip()

    def generar_plataformas(self):
        if(not self.referencia_plataforma):
            plataforma = self.plataforma_generada
            self.referencia_plataforma = True
        elif(len(self.plataformas) < CANTIDAD_MAXIMA_PLATAFORMAS):
            anchura_plataforma = random.randint(60, 80)
            altura_plataforma = self.plataforma_generada.rect.y  - random.randrange(80, 120)
            posicion = (random.randrange(0 + anchura_plataforma, WIDTH - anchura_plataforma), altura_plataforma)
            tipo_plataforma = random.randint(1, 10)
            if((tipo_plataforma == 1 or tipo_plataforma == 2) and self.personaje.puntaje > 100):
               se_mueve = True
            else:
                if((tipo_plataforma == 5 and self.personaje.puntaje > 0) and (not self.plataforma_generada.se_mueve)):
                    enemigo = Enemigo(self.tipo_enemigo, self.plataforma_generada.rect.topleft, self.plataforma_generada)
                    self.enemigos.add(enemigo)
                    self.sprites.add(enemigo)
                if(tipo_plataforma == 3):
                    tipo_objeto = random.randint(1, 2)
                    if(tipo_objeto == 1):
                        es_vida = True
                    else:
                        es_vida = False
                    objeto = Objeto(TAMAÑO_OBJETO, self.plataforma_generada.rect.midtop, es_vida)
                    self.objetos.add(objeto)
                    self.sprites.add(objeto)
                se_mueve = False
            plataforma = Plataforma((anchura_plataforma, 10), self.img_plataforma, posicion, se_mueve)
            self.plataformas.add(plataforma)
            self.sprites.add(plataforma)
            self.plataforma_generada = plataforma

    def dibujar_fondo(self, desplazamiento:int):
        self.desplazamiento_fondo += desplazamiento
        if(self.desplazamiento_fondo >= HEIGHT):
            self.desplazamiento_fondo = 0
        self.pantalla.blit(self.fondo, (0, 0 + self.desplazamiento_fondo))
        self.pantalla.blit(self.fondo, (0, -HEIGHT + self.desplazamiento_fondo))

    def perdiste(self):
        if self.personaje.rect.top > HEIGHT:
            if(self.personaje.puntaje > self.max_puntaje):
                with open(self.archivo_puntaje, "w") as archivo:
                    archivo.write(str(self.personaje.puntaje))
                self.max_puntaje = self.personaje.puntaje
            self.personaje.kill()
            self.juego_terminado = True 
        elif(self.vidas == 0):
            self.juego_terminado = True 
    
    def generar_texto(self, texto:str, fuente, color:tuple, posicion:tuple):
        texto_generado = fuente.render(texto, True, color)
        self.pantalla.blit(texto_generado, posicion)

    def generar_boton(self, texto:str, fuente, color_texto:tuple, anchura_boton:int, altura_boton:int,distancia_top:int, color_boton:tuple):
        boton_rectangulo = pygame.rect.Rect((WIDTH / 2) - anchura_boton/2, self.posicion_y_boton + distancia_top,anchura_boton, altura_boton)
        pygame.draw.rect(self.pantalla, color_boton, boton_rectangulo)
        texto_generado = fuente.render(texto, True, color_texto)
        if(boton_rectangulo.collidepoint(pygame.mouse.get_pos())):
            pygame.draw.rect(self.pantalla, (0,255,0), boton_rectangulo)
        else:
            pygame.draw.rect(self.pantalla, color_boton, boton_rectangulo)
        self.pantalla.blit(texto_generado, (boton_rectangulo.x+(boton_rectangulo.width-texto_generado.get_width())/2, boton_rectangulo.y + (boton_rectangulo.height-texto_generado.get_height())/2))
        if(texto == "JUGAR"):
            self.boton_jugar = boton_rectangulo
        elif(texto == "SALIR"):
            self.boton_salir = boton_rectangulo
        elif(texto == "SALIR AL MENU"):
            self.boton_salir_menu = boton_rectangulo
        elif(texto == "CONTINUAR"):
            self.boton_continuar = boton_rectangulo
        elif(texto == "REINICIAR" or texto == "VOLVER A JUGAR"):
            self.boton_reiniciar = boton_rectangulo
    
    def generar_boton_img(self, ruta_img:str, anchura_boton:int, altura_boton:int, distancia_top:int, color:str):   
        self.image = pygame.transform.scale(pygame.image.load(ruta_img).convert_alpha(), (anchura_boton, altura_boton))
        self.pantalla.blit(self.image, ((WIDTH / 2) - anchura_boton/2, self.posicion_y_boton + distancia_top))
        if(color == "rojo"):
            self.mapa_cielo = pygame.rect.Rect((WIDTH / 2) - anchura_boton/2, self.posicion_y_boton + distancia_top, anchura_boton, altura_boton)
        if(color == "verde"):
            self.mapa_espacio = pygame.rect.Rect((WIDTH / 2) - anchura_boton/2, self.posicion_y_boton + distancia_top, anchura_boton, altura_boton)
        if(color == "azul"):
            self.mapa_nada = pygame.rect.Rect((WIDTH / 2) - anchura_boton/2, self.posicion_y_boton + distancia_top, anchura_boton, altura_boton)
        
        



