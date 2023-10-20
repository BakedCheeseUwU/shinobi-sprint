import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    # Load image
    img =  pygame.image.load(BASE_IMG_PATH + path).convert()
    # Make black backgrounds transparent
    img.set_colorkey((0,0,0))
    return img
