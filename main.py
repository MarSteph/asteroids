import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    #pygame.display.set_caption("Hello Pygame")
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    #print(pygame.display.get_window_size())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()