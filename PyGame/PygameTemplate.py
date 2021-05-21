import pygame  # import library
pygame.init()  # initialize pygame

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

while True:
    # If players exit game then exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
