import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH,TITLE,FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager
from dino_runner.components.score_menu.text_utils import *
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

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
        self.points = 0
        self.running = True
        self.death_count = 0
        self.player_heart_manager = PlayerHeartManager()

    def run(self):
        self.obstacle_manager.recet_obstacles(self)
        self.player_heart_manager.reset_hearts()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()  
        #pygame.quit() #Se cierra pygame3

    def events(self):
        #manejamos los eventos
        for event in pygame.event.get():#Obtiene los eventos
            if event.type == pygame.QUIT:#Si se cumple entonces:
                self.playing = False
                self.running = False
    
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
        self.score()
        self.player_heart_manager.draw(self.screen)
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

    def score(self):
        self.points += 1

        if self.points % 100 == 0:#incrementa velocidad a lo sumo 1 si llega a 100
            self.game_speed += 1 
        
        score, score_rect = get_score_elements(self.points)
        self.screen.blit(score, score_rect)

    def show_menu(self):
        self.running = True
        
        white_color = (255,255,255)
        self.screen.fill(white_color)#Pantalla de inicio
        self.print_menu_elements(self.death_count)
        pygame.display.update()#Actualiza los elementos de pantalla
        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count = 0):
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if death_count == 0:
            text, text_rect = get_centered_message('Press any key to start')
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            text, text_rect = get_centered_message('Press any key to restart')
            score, score_rect = get_centered_message('Your Score: ' + str(self.points), heigth=half_screen_heigth + 50)#establece por debajo de linea 94
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Dino Good Bye!!")
                self.running = False
                self.playing = False
                pygame.display.quit()#Cerramos la pantalla
                pygame.quit()#cierra proceso de pygame
                exit()#cierra el proceso de las ventana
            if event.type == pygame.KEYDOWN:#cualquier tecla valida
                self.restart_game()
                self.run()

    def restart_game(self):
        self.game_speed = 20
        self.points = 0