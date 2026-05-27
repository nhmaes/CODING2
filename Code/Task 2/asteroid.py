import pygame
import numpy as np
import math

class Asteroid:
    def __init__(self, x, y, radius, surface):
        # Position of the tip of the asteroid
        self.pos = np.array([x, y])
        # Additional properties goes here:

        # i pick a random angle between 0 and a full circle so each asteroid heads in a different direction
        angle = np.random.uniform(0, 2 * math.pi)

        # i make speed random so asteroids dont all move at the same pace
        speed = np.random.uniform(2.0, 8.0)

        # i use cos and sin to split the angle into left/right and up/down movement then multiply by speed to control how fast it goes
        self.velocity = np.array([math.cos(angle) * speed, math.sin(angle) * speed])

        # Leave the rest of these properties
        self.surface = surface
        self.radius = radius

    def update(self, asteroids):
        # Action required!

        # Set position of asteroid based on given parameter
        # i add velocity to position every frame so the asteroid actually moves instead of staying still
        self.pos = self.pos + self.velocity

        # Leave the rest of the code
        # Wrap asteroid around the edges so it always stay on screen
        if self.pos[0] > self.surface.get_width():
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = self.surface.get_width()

        if self.pos[1] > self.surface.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = self.surface.get_height()

    # Draw the asteroid onto the canvas
    def draw(self):
        pygame.draw.circle(self.surface, (0, 0, 255), (self.pos[0], self.pos[1]), self.radius)