import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_vector = random.uniform(20, 50)
            vect_1 = self.velocity.rotate(rand_vector)
            vect_2 = self.velocity.rotate(-rand_vector)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
            new_asteroid.velocity = vect_1 * 1.2
            new_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
            new_asteroid.velocity = vect_2 * 1.2
            
