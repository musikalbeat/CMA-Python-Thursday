'''
Lesson 3: Shapes with Object Oriented Programming
'''
import pygame #import library
pygame.init() #initialize pygame

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

# Colors
white = (255, 255, 255)
turquiose = (3, 252, 232)
lime_green = (3, 252, 48)
red = (252, 3, 3)
orange = (252, 169, 3)

# Rectangle Class
class Rectangle:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen

    def draw(self):
        # pygame.draw.rect(surface, color, rectangle tuple, thickness(optional))
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

class Circle:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        # pygame.draw.circle(surface, color, center point pair, radius, thickness(optional))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Ellipse:
    def __init__(self, x1, y1,  width, height, color, screen):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen

    def draw(self):
        # pygame.draw.ellipse(surface, color, bounding rectangle)
        pygame.draw.ellipse(self.screen, self.color, (self.x1, self.y1, self.width, self.height))

class Line:
    def __init__(self, x1, y1, x2, y2, color, screen):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.screen = screen

    def draw(self):
        # pygame.draw.line(surface, color, (start point), (end point), thickness(optional))
        pygame.draw.line(self.screen, self.color, (self.x1, self.y1), (self.x2, self.y2))

white_rect = Rectangle(200, 200, 100, 100, white, screen)
white_circle = Circle(300, 100, 100, white, screen)
white_ellipse = Ellipse(0, 250, 500, 250, white, screen)
red_line = Line(250, 0, 250, 500, red, screen)

while True:
    # If players exit game then exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Call draw method on rect and circle object
    white_rect.draw()
    white_circle.draw()
    white_ellipse.draw()
    red_line.draw()

    # Render shapes on screen
    pygame.display.update()
