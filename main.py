# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  ### putting the player and other objects into groups! to call them all at once.
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  asteroid_field = AsteroidField()
  Shot.containers = (shots, updateable, drawable)
  ### 
  #have an ingame clock for the fps, to save ressources
  #dt, delta time, saves the time passed. 
  fps = pygame.time.Clock() 
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  dt = 0
  
  its_running = True
  while its_running == True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updateable.update(dt)
    
    for asteroid in asteroids:
      if asteroid.collision(player):
        print("Game over!")
        sys.exit()
      for shot in shots:
        if asteroid.collision(shot):
          asteroid.split()
          shot.kill()
    
    
    screen.fill("black")
    
    for object in drawable:
      object.draw(screen)
    
    #player.draw(screen)
    
    pygame.display.flip()

    dt = fps.tick(60) / 1000

    #print (dt)

    

if __name__ == "__main__":
    
    main()
