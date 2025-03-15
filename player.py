from circleshape import CircleShape
import pygame
from constants import *

class Player(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        elif keys[pygame.K_e]:
            self.rotation += PLAYER_TURN_SPEED * dt
        
        if keys[pygame.K_COMMA]:
            self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
            self.move(dt)
        elif keys[pygame.K_o]:
            self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SPEED
            self.move(dt)
        else:
            self.velocity = self.velocity * 0.99
        
    def move(self, dt):
        self.position += self.velocity * dt * PLAYER_SPEED