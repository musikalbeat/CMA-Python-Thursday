import pygame  # import library
pygame.init()  # initialize pygame

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

white = (255,255,255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([30, 40])
        self.image.fill(white)

        self.rect = self.image.get_rect(center = (screen_width/2, screen_height - 30))

        self.x_speed = 0
        self.y_speed = 0
        speed = 1

    def update(self):
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

        if self.rect.right >= screen_width:
            self.rect.right = screen_width

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0

class Enemy(pygame.sprite.Sprite):

    def__init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 40])
        self.imgae = fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.y.speed = random.randrange(1, 3)

    def update(self):
        self.rect.y = self.y_speed
        if self.rect.top > screen_height + 10:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.y.speed = random.randrange(1, 3)

all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)

enemies = pygame.sprite.Group()

for i in range(5):
    e = Enemy()
    all_sprite.add(e)
    enemies.add(e)

            
while True:
    # If players exit game then exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    all_sprite.update()

    hits = pygame.sprite.spritecollide(player, enemies, True)

    for hit in hits:
        e = Enemy()
        all_sprite.add(e)
        enemies.add(e)

    #draw/render 
    screen.fill((0, 0, 0))
    all_sprite.draw(screen)

    pygame.display.flip()