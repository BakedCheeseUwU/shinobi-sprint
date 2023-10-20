import sys
import pygame

from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Shinobi Sprint")
        # Creates a window
        self.screen = pygame.display.set_mode((640,480))
        # Loads empty surface and then we upscale it for pixel art
        self.display = pygame.Surface((320,240))

        self.clock = pygame.time.Clock()
        

        self.movement = [False,False]


        self.assets = {
            'player' : load_image('entities/player.png')
        }

        # Create player
        self.player = PhysicsEntity(self,'player',(50,50),(8,15))

    #  we are running an infinite loop which will change the
    #  content onscreen based on inputs by user.
    #  every frame is basically an iteration of a loop 
    def run(self):
        while True:
            # Clear the screen by filing with a colour
            self.display.fill((14,219,248))

            self.player.update((self.movement[1] - self.movement[0],0))
            self.player.render(self.display)

            # If the user presses the close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Move Stuff around
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            # Updates the screen and limits the fps
            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))
            pygame.display.update()
            self.clock.tick(60)

game().run()


