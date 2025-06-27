# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {constants.SCREEN_WIDTH}")
  print(f"Screen height: {constants.SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

  its_running = True
  while its_running == True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    pygame.display.flip()

    



if __name__ == "__main__":
    
    main()
