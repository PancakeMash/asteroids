import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable =  pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, bullets)
	
	player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT / 2))
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return		

		screen.fill("black")

		for thing in drawable:
			thing.draw(screen)
		
		for thing in updatable:
			thing.update(dt)
		
		for asteroid in asteroids:
			for bullet in bullets:
				if bullet.collision(asteroid):
					asteroid.kill()
					bullet.kill()
					asteroid.split()


			if player.collision(asteroid):
				sys.exit("Game Over!")


		pygame.display.flip()

		dt = clock.tick(60)/1000
		
if __name__ == "__main__":
    main()
