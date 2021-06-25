import pygame  # import library
import random
from os import path
pygame.init()  # initialize pygame

img_dir = path.join(path.dirname(__file__), 'img')


screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

bg = pygame.image.load(path.join(img_dir, "Full-Background.png")).convert()
bg_rect = bg.get_rect(center = (screen_width/2, -100))
player_img = pygame.image.load(path.join(img_dir, "Basket.png")).convert()
enemy_img = pygame.image.load(path.join(img_dir, "egg1.png")).convert()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Set player image to basket image
        self.image = player_img
        # Get rid of black outline
        self.image.set_colorkey((0,0,0))

        # Create rect object that has dimension of the image
        self.rect = self.image.get_rect(
            center=(screen_width/2, screen_height - 30))

        # Initialize speed on x and y for sprite
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        # Values to 0 other sprite fly off screen
        self.x_speed = 0
        self.y_speed = 0
        speed = 7

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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img, (42, 48))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.minSpeed = 5
        self.maxSpeed = 5
        self.y_speed = random.randint(self.minSpeed, self.maxSpeed)

    def update(self):
        self.rect.y += self.y_speed
        if self.rect.top > screen_height + 10:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.y_speed = random.randint(self.minSpeed, self.maxSpeed)


all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)

enemies = pygame.sprite.Group()

for i in range(5):
    e = Enemy()
    all_sprite.add(e)
    enemies.add(e)

score = 0

while True:
    # If players exit game then exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    all_sprite.update()

    hits = pygame.sprite.spritecollide(player, enemies, True)

    # Spawn new enemy for each one that gets deleted
    for hit in hits:
        score += 8000000
        e = Enemy()
        all_sprite.add(e)
        enemies.add(e)

    # Draw/Render
    screen.fill((0, 0, 0))
    screen.blit(bg, bg_rect)
    all_sprite.draw(screen)
    draw_text(screen, str(score), 18, screen_width/2, 10)

    # Mandatory otherwise sprites won't show
    pygame.display.flip()
