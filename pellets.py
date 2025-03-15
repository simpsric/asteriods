from constants import *
import pygame
from circleshape import CircleShape

class Pellet(CircleShape):
    containers = None
    
    def __init__(self, x, y, rotation):
        super().__init__(x, y, PELLET_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PELLET_SPEED
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt