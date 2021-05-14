'''
Lesson 1: PyGame Introduction

PyGame is cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

PyGame Draw Reference: https://www.pygame.org/docs/ref/draw.html
'''

import pygame #import library
pygame.init() #initialiaze pygame

screen_width = 500
screen_height = 500

#Create window using variables above
window = pygame.display.set_mode((screen_width, screen_height))
#Display name of your game at the top of the window
pygame.display.set_caption("My First PyGame")

#Colors using RGB values
white = (255, 255, 255)
green = (50, 168, 82)
blue = (20, 24, 255)
red = (255, 20, 20)
pink = (255, 3, 226)
orange = (255, 143, 51)

#Changes background color for window
window.fill(white)

#Draws a rectangle using pygame.draw.rect(surface, color, rectangle dimensions, thickness(optional))
#                                 x    y   w   h
pygame.draw.rect(window, green, (300, 100, 50, 70))

#draw a circle using pygame.draw.circle(surface, color, center point, radius, thickness(optional))
#                                   x    y    size(radius)
pygame.draw.circle(window, pink, (225, 300), 10)

#draw a line using pygame.draw.line(surface, color, start point, end point, thickness(optional))
#                             (x1, y1)    (x2, y2)    thickness of line
pygame.draw.line(window, red, (150, 400), (250, 400), 5)

#In this loop we can render all game components and handle events
while True:

    #If players exits game then the exit game loop will execute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #Must call update on window to render bg color and shapes
    pygame.display.update()