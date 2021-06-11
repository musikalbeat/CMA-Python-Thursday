'''
Lesson 5: Boundaries and Collisions

In this lesson you will learn how to create sprites and keep them within the screen boundaries. Moreover, we will cover new sprite methods and a new way of moving sprites around the screen with user input. Lastly, we will cover how to detect if two sprites collide with one another.
'''
import pygame  # import library
pygame.init()  # initialize pygame

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

white = (255, 255, 255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block and fill with color
        self.image = pygame.Surface([30, 40])
        self.image.fill(white)

        # Create rect object that has dimension of the image
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height - 30))

        # Initialize speed on x and y for sprite
        self.x_speed = 0
        self.y_speed = 0
    
    def update(self):
        # Values to 0 other sprite fly off screen
        self.x_speed = 0
        self.y_speed = 0
        speed = 1

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.y_speed -= speed

        elif keystate[pygame.K_DOWN]:
            self.y_speed += speed

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
