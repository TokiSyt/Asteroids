import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
	def __init__(self, position, velocity):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(sreen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position *= (self.position * dt)
