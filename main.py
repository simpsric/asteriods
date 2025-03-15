import pygame
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables,)
    
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidField1 = AsteroidField()
    
    while(True):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
            
        for asteroid in asteroids:
            if player1.check_collision(asteroid):
                print("Game Over!")
                pygame.quit()
                return
            
        pygame.display.flip()
        gameClock.tick(FPS)
        dt = gameClock.get_time() / 1000
                
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")



if __name__ == '__main__':
    main()