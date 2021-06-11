import pygame
from pygame.constants import K_RIGHT
pygame.init

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

white = (255, 255, 255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([30, 40])
        self.image.fill(white)

        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/30))

        self.x_speed = 0
        self.y_speed = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
             self.x_speed -= speed

            elif keystate[pygame.K_DOWN]:
                self.x_speed += speed

                  elif keystate[pygame.K_LEFT]:
                self.x_speed -= speed

 elif keystate[pygame.K_RIGHT]:
                self.x_speed += speed
self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Keep player inside screen bounds
        if self.rect.right >= screen_width:
            self.rect.right = screen_width

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0


    while True:
        # If players exit game then exit game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()