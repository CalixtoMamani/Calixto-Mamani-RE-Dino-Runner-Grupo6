import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH,TITLE,FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()#inicializa pygame
        pygame.display.set_caption(TITLE) #se le envia un titulo
        pygame.display.set_icon(ICON) 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#Establece la pantalla con x y
        self.clock = pygame.time.Clock()#contador de tiempo
        self.playing = False #Estado para sabir si se juega
        self.game_speed = 20#Velocidad inicial del juego
        #Establece el fondo de la pantalla
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()  
        pygame.quit() #Se cierra pygame

    def events(self):
        #manejamos los eventos
        for event in pygame.event.get():#Obtiene los eventos
            if event.type == pygame.QUIT:#Si se cumple entonces:
                self.playing = False
    
    def update(self):
        user_input = pygame.key.get_pressed()#reconoce evento tecla
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)#tick -> contador, FPS -> indicador
        self.screen.fill((255,255,255))#fill -> rellena la pantalla con color
        self.draw_background()
        self.player.draw(self.screen)#dibuja el dino
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()#method pygame -> actualizar pantalla
        pygame.display.flip()#"" muestra los elementos actuales en pantalla

    def draw_background(self):
        image_width = BG.get_width()#Acceso a width -> numerico
        self.screen.blit(BG,(self.x_pos_bg, self.y_pos_bg))#muestra un elemento BG en pantalla en pos(x,y)
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))#suma el tam de toda pantalla a pos de BG
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0#reinicia pos x
        self.x_pos_bg -= self.game_speed#desplazamiento del dino <- 

    
        
