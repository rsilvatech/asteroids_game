import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, position, velocity, radius):
        super().__init__(position, velocity, radius)
        

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

        
