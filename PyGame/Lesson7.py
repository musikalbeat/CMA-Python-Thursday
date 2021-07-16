import pygame  # import library
pygame.init()  # initialize pygame
from os import path

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Buttons and Sounds")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (66, 135, 245)
pink = (255, 0, 212)

font_name = pygame.font.match_font('arial')

sound_dir = path.join(path.dirname(__file__), 'sounds')

applause = path.join(sound_dir, "applause.wav")
burp = path.join(sound_dir, "burp.mp3")
alarm = path.join(sound_dir, "alarm.mp3")

applauseSound = pygame.mixer.Sound(applause)
burpSound = pygame.mixer.Sound(burp)
alarmSound = pygame.mixer.Sound(alarm)

class Button():
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outlineColor = None):
        if outlineColor:
            pygame.draw.rect(screen, outlineColor, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '': # ! + = --> != 
            font = pygame.font.Font(font_name, 18)
            text_surface = font.render(self.text, True, black)
            screen.blit(text_surface, ( self.x + (self.width/2 - text_surface.get_width()/2),
                                        self.y + (self.height/2 - text_surface.get_height()/2)))

    def inBoundaries(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

alarmButton = Button(red, 50, 50, 100, 100, "Alarm")
burpButton = Button(blue, 200, 50, 100, 100, "Burp")
applauseButton = Button(pink, 350, 50, 100, 100, "Applause")

while True:
    # If players exit game then exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if alarmButton.inBoundaries(pos):
                print("Red button clicked")
                alarmSound.play(0,800) # Loop number, How long to play sound
            if burpButton.inBoundaries(pos):
                print("Blue button clicked")
                burpSound.play()
            if applauseButton.inBoundaries(pos):
                print("Pink button clicked")
                applauseSound.play(0, 1000)

    alarmButton.draw(screen, white)
    burpButton.draw(screen, white)
    applauseButton.draw(screen, white)

    pygame.display.update()
