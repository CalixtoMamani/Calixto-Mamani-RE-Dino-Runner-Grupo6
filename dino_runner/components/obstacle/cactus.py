from dino_runner.components.obstacle.obstacle import Obstacle
import random
'''
La clase Obstacle hereda a Cactus ademas con todos las propiedades y metodos
'''
class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)#entero randomico entre(a, b)
        #self.type_of_cactus = random.randint(0,1)
        super().__init__(image, self.type)#invocamos al constrcutor de la clase superior con super
        if self.type > 2:
           self.rect.y = 300
        else: 
           self.rect.y = 325#Establece la pos del obstaculo
        