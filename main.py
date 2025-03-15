import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    
    Player.containers = (updateables, drawables)
    
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while(True):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()
        gameClock.tick(FPS)
        dt = gameClock.get_time() / 1000
                
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")



if __name__ == '__main__':
    main()