'''
Lesson 4: Key Events and Movement

You will learn how to move sprites in your game window by using coordinates and key bindings.

Coordinates

In math class, you (will) learned about graphs and plotting poiunts on graphs then you most likely know what coordinates are. In math class, the origin point of a graph is (0,0) which is located at the center of the + plus shaped graph.

In PyGame, the screen coordinates work quite differently. You may think of the origin point is located in the center, but it is located on the top left.

Key Binding

Key binding means that when a specific key is pressed it is going to cause an effect on the game or game object(s). We also use predefined variables that PyGame has created for us to check if either the up, down, left, or right arrow key was pressed.

Reference Link to All the Keys: https://www.pygame.org/docs/ref/key.html?highlight=key

Movement


'''
import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Movement in PyGame")

class Ball:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.x_speed = 0
        self.y_speed = 0

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def handle_keys(self):
        # Handle player input to move ball around screen 
        # We will be using arrow keys to move accordingly 
        # We can also handle closing the window here if player quits game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # Check which arrow key was pressed and move in that direction
                if event.key == pygame.K_UP:
                    # Decrease y_speed in y axis to move up
                    self.y_speed -= 1
                elif event.key == pygame.K_DOWN:
                    # Increase y_speed in y axis to move down
                    self.y_speed += 1
                elif event.key == pygame.K_LEFT:
                    # Decrease x_speed in x axis to move left
                    self.x_speed -= 1
                elif event.key == pygame.K_RIGHT:
                    # Increase x_speed in x axis to move right
                    self.x_speed += 1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.y_speed += 1
                elif event.key == pygame.K_DOWN:
                    self.y_speed -= 1
                elif event.key == pygame.K_LEFT:
                    self.x_speed += 1
                elif event.key == pygame.K_RIGHT:
                    self.x_speed -= 1

        # Apply speed to ball in respective directions
        self.x += self.x_speed
        self.y += self.y_speed

turquoise = (3, 252, 232)

# Create ball object
ball = Ball(225, 225, 20, turquoise, screen)

while True:
    # Used fill to draw new ball on top of old when moving
    screen.fill((0,0,0))

    ball.draw()
    ball.handle_keys()

    pygame.display.update()
