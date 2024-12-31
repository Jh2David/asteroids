import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        position = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
