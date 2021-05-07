import turtle
import time

# turtle screen setup
screen = turtle.Screen()
screen.title("Turtle Loop")
screen.bgcolor("yellow_orange")
screen.tracer(0) # stops the screen from refreshing
screen.setup(800, 600) # sets up the size of our screen

# setup some code and graphics
count = 0
t = turtle.Turtle()

# game loop
while True:
    screen.update() # refreshes the screen manually
    
    # Code goes here
    count += 1
    print(count)
    t.forward(1)
    
    time.sleep(.01) # Speed of game loop (lower is faster)

# screen.mainloop() replaced so we can make updates