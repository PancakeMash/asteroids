import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity or pygame.math.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "grey", (self.position.x, self.position.y) , self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_angle) * SPEED_MULTIPLIER
        vector2 = self.velocity.rotate(-random_angle) * SPEED_MULTIPLIER
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, vector1)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, vector2)