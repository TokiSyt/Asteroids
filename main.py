import pygame
import sys
from shot import *
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.time.Clock
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = updatable
	Player.containers = updatable, drawable
	Shot.containers = (shots, drawable, updatable)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		for items in updatable:
			items.update(dt)

		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.split()

		screen.fill("black")

		for draws in drawable:
			draws.draw(screen)

		pygame.display.flip()
		clock = pygame.time.Clock()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
