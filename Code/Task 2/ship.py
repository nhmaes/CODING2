import pygame
import numpy as np
import math
import utils

class Ship:
    def __init__(self, x, y, surface):
        # Position of the tip of the ship
        self.pos = np.array([x, y])
        # Rotation angle of the ship relative to the tip of the ship
        self.angle = 0.0
        # Additional properties goes here:

        # i store the velocity as a zero vector to start so the ship isnt moving when the game loads
        self.velocity = np.array([0.0, 0.0])

        # Leave the rest of these properties
        self.surface = surface
        self.radius = 20
        self.color = (0, 0, 0)
        self.collided = False

    # Update properties of the ship
    def update(self, mouse_pos, asteroids, game_status):
        # Action required!

        # Set position of ship based on given parameter
        # i set the ship position directly to wherever the mouse is so it follows the cursor
       # i calculate the angle first while self.pos is still the old position so the subtraction actually gives a real gap
        # i negate the y difference to correct for pygame flipping the y axis downward
        self.angle = math.atan2(-(mouse_pos[1] - self.pos[1]), mouse_pos[0] - self.pos[0])

# i blend the ship position towards the mouse instead of snapping to it so the movement feels smooth
        self.pos = self.pos + (mouse_pos - self.pos) * 0.2
        # Leave the rest of the code
        # Check for collision
        if game_status == "started":
            self.collision(asteroids, game_status)

    # Draw the ship onto the canvas
    def draw(self):
        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    # Detect whether ship has collided with an asteroid
    def collision(self, asteroids, game_status):
        for asteroid in asteroids:
            if np.linalg.norm(asteroid.pos - self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 0, 0)
                self.collided = True
                break