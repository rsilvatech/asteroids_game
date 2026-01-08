import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius == ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_1.velocity += self.velocity + pygame.Vector2(0, 100).rotate(random_angle)
            asteroid_2.velocity += self.velocity + pygame.Vector2(0, 100).rotate(-random_angle)

