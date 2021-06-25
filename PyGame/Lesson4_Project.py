import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("House Key Binding")

# Colors
turquoise = (3, 252, 232)
lime_green = (3, 252, 48)
red = (252, 3, 3)
grey = (145, 143, 140)
light_brown = (130, 102, 61)
dark_brown = (94, 56, 0)

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                # Draw building
                pygame.draw.rect(screen, grey, (25, 150, screen_width - 200, screen_height) )

            if event.key == pygame.K_d:
                # Draw door
                pygame.draw.rect(screen, light_brown, (125, 325, 100, 200) )

            if event.key == pygame.K_w:
                # Draw windows
                pygame.draw.circle(screen, turquoise, (100, 225), 30)
                pygame.draw.circle(screen, turquoise, (250, 225), 30)

            if event.key == pygame.K_c:
                # Draw chimney
                pygame.draw.rect(screen, light_brown, (225, 50, 25, 100) )

            if event.key == pygame.K_r:
                # Draw roof
                pygame.draw.polygon(screen, red, [(25, 150), (162, 50),(324, 150)] )
            
            if event.key == pygame.K_t:
                # Draw tree
                pygame.draw.rect(screen, dark_brown, (400, 300, 50, 200) )
                pygame.draw.circle(screen, lime_green, (425, 300), 70)

    pygame.display.update()