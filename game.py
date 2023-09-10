import sys
import pygame

class game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Shinobi Sprint")
        self.screen = pygame.display.set_mode((640,480))

        # clock object will be usefull to limit fps to 60 
        self.clock = pygame.time.Clock()

    #  we are running an infinite loop which will change the
    #  content onscreen based on inputs by user.
    #  every frame is basically an iteration of a loop 
    def run(self):
        while True:
            # If the user presses the close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Updates the screen and limits the fps
            pygame.display.update()
            self.clock.tick(60)

game().run()


