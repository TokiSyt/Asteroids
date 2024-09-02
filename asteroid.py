import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.velocity = pygame.Vector2(0, 0)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		old_radius = self.radius

		asteroid_one = Asteroid(self.position.x, self.position.y, old_radius / 2)
		asteroid_two = Asteroid(self.position.x, self.position.y, old_radius / 2)

		random_angle = random.uniform(20, 50)
		velocity_one = self.velocity.rotate(random_angle) * 1.2
		velocity_two = self.velocity.rotate(-random_angle)

		asteroid_one.velocity = velocity_one
		asteroid_two.velocity = velocity_two

		Asteroid.containers[2].add(asteroid_one)
		Asteroid.containers[2].add(asteroid_two)
