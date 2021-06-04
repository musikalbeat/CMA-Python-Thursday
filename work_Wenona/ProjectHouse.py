import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("House Key Binding")

#Colors
gray = (145, 143, 140)
dark_brown = (94, 56, 0)
light_brown = (94, 56, 0)
lime_green = (3, 252, 48)

#Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(
            quit()
            )

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                #draw building
                pygame.draw.rect(screen, gray, (25, 150, screen_width - 200, screen_height))

            if event.key == pygame.K_d:
                #draw door
                pygame.draw.rect(screen, dark_brown, (125, 325, 100, 200))

            if event.key == pygame.K_w:
                #draw windows
                pygame.draw.circle(screen, light_brown, (100, 225), 30)
                pygame.draw.circle(screen, light_brown, (250, 225), 30)

            if event.key == pygame.K_c:
                #draw chimney
                pygame.draw.rect(screen, gray, (225, 50, 25, 100))

            if event.key == pygame.K_r:
                #draw roof
                pygame.draw.polygon(screen, dark_brown, [(25, 150), (162, 50), (324, 150)])

            if event.key == pygame.K_t:
                #draw tree
                pygame.draw.rect(screen, dark_brown, (400, 300, 50,200))
                pygame.draw.circle(screen, lime_green, (425, 300), 70)

    pygame.display.update()
