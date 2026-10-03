import random

import pygame
from circleshape import CircleShape
from constants import *
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw (self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and we're done"
        log_event("asteroid_split")
        angle =random.uniform(20, 50)
        first_velocity=self.velocity.rotate(angle)
        second_velocity=self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2= Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = first_velocity * 1.2
        new_asteroid_2.velocity = second_velocity
