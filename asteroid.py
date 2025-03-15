from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            ran_angle = random.uniform(20, 50)
            for i in range(2):
                asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                asteroid.velocity = self.velocity.rotate(ran_angle * ((-1) ** (i+1))) * random.uniform(0.75, 1.25)
        self.kill()