from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite
''''
La Clase Obstacle muestra los elementos objetos obstaculos en el juego
'''
class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacle):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle.pop()#Por defecto sale el ultimo de la lista

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)