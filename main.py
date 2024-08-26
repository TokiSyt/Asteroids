import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.time.Clock
	dt = 0
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	updatable.add(player)
	drawable.add(player)
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		for items in updatable:
			items.update(dt)
		screen.fill("black")
		for draws in drawable:
			draws.draw(screen)
		pygame.display.flip()
		clock = pygame.time.Clock()
		dt = clock.tick(60) / 1000

	
if __name__ == "__main__":
	main()
