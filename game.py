import sys
import pygame

class game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Shinobi Sprint")
        # Creates a window
        self.screen = pygame.display.set_mode((640,480))

        # clock object will be usefull to limit fps to 60 
        self.clock = pygame.time.Clock()

        # Loads image
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        # Makes the background of the image transparent
        self.img.set_colorkey((0,0,0))
        self.img_pos = [160,260]
        self.movement = [False,False]

        # Creates a Rectangle on screen 
        self.collision_area = pygame.Rect(50,50,300,50)


    #  we are running an infinite loop which will change the
    #  content onscreen based on inputs by user.
    #  every frame is basically an iteration of a loop 
    def run(self):
        while True:
            # Clear the screen by filing with a colour
            self.screen.fill((14,219,248))

            # Create a rectangle around image in current frame
            img_r = pygame.Rect(self.img_pos[0],self.img_pos[1],self.img.get_width(),self.img.get_height())

            # Check if both collide and change colours
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen,(0,100,255),self.collision_area)
            else:
                pygame.draw.rect(self.screen,(0,50,155),self.collision_area)

            # Trick to  change position of image on input
            self.img_pos[1] += (self.movement[1] - self.movement [0])*5
            # Display image on screen(blit)
            self.screen.blit(self.img,self.img_pos)

            # If the user presses the close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Move Stuff around
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            # Updates the screen and limits the fps
            pygame.display.update()
            self.clock.tick(60)

game().run()


