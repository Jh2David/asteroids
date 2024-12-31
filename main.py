import pygame

from circleshape import CircleShape
from constants import *
from player import Player


def main():
    pygame.init()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    circle = CircleShape(x=100, y=100, radius=30)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            clock.tick(60)

        # Update
        for thing in updatable:
            thing.update(dt)

        # Draw
        screen.fill((0, 0, 0))
        for thing in drawable:
            thing.draw(screen)

        # Refresh
        pygame.display.flip()

        # FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
