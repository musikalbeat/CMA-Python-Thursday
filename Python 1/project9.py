'''
Copy this to Visual Studio

Project 9: Click Training Game

Test click speed and accuracy.

Main:
- Provide targets to click on
- Make target disappear after some time
- Have target appear in different locations

Side:
- Keep track of how many targets have been hit
    - Can also track missed target

---
Pseudocode:

    setup game screen
    start scores and misses at 0
    create target to start
    run game loop
        keep track of time target has been up
        if target has been clicked
            create a new target
            **add one to the score
            reset the target timer
        if the target timer ends
            **add one to misses
            create a new target
            reset timer

Timer Example:
    target_countdown = 1
    time.sleep(1)

    target_countdown = 10
    time.sleep(.1)

    target_countdown = 100
    time.sleep(.01)
'''

import turtle
import time
import random

# Turtle Screen Setup
screen_width = 800
screen_height = 600

screen = turtle.Screen()
screen.title("Click Trainer")
screen.bgcolor("PeachPuff2")
screen.tracer(0) # Stop the screen from refreshing
screen.setup(screen_width, screen_height) # Sets up the size of our screen

#Functions
def hit(x, y):
    print("Target Hit!")
    global target
    global target_countdown
    reset_target(target)
    target = create_target()
    target_countdown = 100

# Turtle Target Setup
def create_target():
    t = turtle.Turtle()
    t.penup()
    t.shape("circle")
    t.color("red")
    t.speed(0)
    t.onclick(hit)
    x = random.randint(-screen_width / 2, screen_width / 2)
    y = random.randint(-screen_height / 2, screen_height / 2)
    t.setpos(x, y)
    return t

def reset_target(t):
    t.reset()
    t.hideturtle()

target = create_target()
target_countdown = 100

# Game Loop
while True:
    screen.update() # Refreshes the screen manually

    # Reset everything when the timer finishes
    if target_countdown == 0:
        reset_target(target)
        target = create_target()
        target_countdown = 100

    target_countdown -= 1
    time.sleep(.01) # Speed of the game loop (lower is faster)
