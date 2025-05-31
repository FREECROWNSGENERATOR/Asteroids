import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from shot import Shot

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = (updatables)
Shot.containers = (shots, updatables, drawables)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in drawables:
            sprite.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            player.collision(asteroid)
            if player.collision(asteroid) == True:
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main() 
