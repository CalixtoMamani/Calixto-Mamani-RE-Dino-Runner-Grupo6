import pygame

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
'''
Maneja los obstaculos en el juego de alguna forma
'''
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
           
    def update(self, game):
        if len(self.obstacles) == 0:
            
            self.obstacles.append(Cactus(SMALL_CACTUS+LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):#detecta colicion
                #pygame.time.delay(500)#Retardamos tiempo
                #game.playing = False
                #break
                pygame.time.delay(100)
                self.obstacles = []

                game.player_heart_manager.reduce_heart()#Reduce los corazones
                if game.player_heart_manager.heart_count > 0:
                    game.player.shield = True#Activado
                    game.player.show_text = False
                    start_time = pygame.time.get_ticks()#dev registro de time
                    game.player.shield_time_up = start_time + 1000#equiv 1 seg
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1#Contador de muertes
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def recet_obstacles(self, self1):#Reinicia los obst una vez terminado el juego
        self.obstacles = []
