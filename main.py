import pygame

from constants import *
from circleshape import CircleShape
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    circle = CircleShape(x=100, y=100, radius=30)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            clock.tick(60)

        circle.update(dt)
        screen.fill((0, 0, 0))
        circle.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
