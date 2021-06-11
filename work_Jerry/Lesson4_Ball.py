import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Movement in PyGames")

class Ball:

    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y_speed -= self.speed
                elif event.key == pygame.K_DOWN:
                     self.y_speed += self.speed
                elif event.key == pygame.K_LEFT:
                     self.x_speed -= self.speed
                elif event.key == pygame.K_RIGHT:
                     self.x_speed += self.speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.y_speed += self.speed
                elif event.key == pygame.K_DOWN:
                     self.y_speed -= self.speed
                elif event.key == pygame.K_LEFT:
                     self.x_speed += self.speed
                elif event.key == pygame.K_RIGHT:
                     self.x_speed -= self.speed


        self.x += self.x_speed
        self.y += self.y_speed

turquoise = (3, 252, 232)
ball = Ball(225, 225, 20, turquoise, screen)

while True:
    screen.fill((0, 0, 0))

    ball.draw()
    ball.handle_keys()

    pygame.display.update()
