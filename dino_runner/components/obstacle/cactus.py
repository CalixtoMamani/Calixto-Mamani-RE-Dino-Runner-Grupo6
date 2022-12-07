from dino_runner.components.obstacle.obstacle import Obstacle
import random
'''
La clase Obstacle hereda a Cactus ademas con todos las propiedades y metodos
'''
class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)#entero randomico entre(a, b)
        super().__init__(image, self.type)#invocamos al constrcutor de la clase superior con super
        self.rect.y = 325#Establece la pos del obstaculo
        