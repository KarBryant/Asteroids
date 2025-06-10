# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()

    print("Starting Asteroids!")

    print(f"Screen width: {constants.SCREEN_WIDTH}")

    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    print(f"Game Initialized: {pygame.get_init()}")

## Set Variables For Game

    clock = pygame.time.Clock()

    #Delta-Time
    dt = 0

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    x = constants.SCREEN_WIDTH / 2

    y = constants.SCREEN_HEIGHT / 2


    ## Groups
    
    updatables = pygame.sprite.Group()
   
    drawables = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    

    ## Group Initilization
    
    Player.containers = (updatables,drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables,drawables,shots)
  
    ##Objects

    player = Player(x,y)
    asteroid_field = AsteroidField()

   


## Main Game Loop
    while pygame.get_init():
        dt = 1000 / clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game Over!")
                raise Exception(SystemExit)
            
            for shot in shots:
                if shot.has_collided(asteroid):
                    asteroid.split()
                    shot.kill()
            
        
        updatables.update(dt)

        for object in drawables:
            object.draw(screen)
        
        
        pygame.display.flip()

      

if __name__ == "__main__":
    main()