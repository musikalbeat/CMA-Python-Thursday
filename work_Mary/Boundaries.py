import pygame
pygame.init

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

white = (255, 255, 255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self)

    pygame.sprite.Sprite.__init__(self)


    self.image = pygame.Surface([30, 40])
    self.image.fill(white)



    self.rect = self.image.get_rect(center = (screen_width/2, screen_height/30))


    self.x_speed = 0
    self.y_speed = 0

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]: