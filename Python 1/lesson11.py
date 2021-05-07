'''
LESSON 11: ADVENTURE GAME

- Create buttons
- Write text in buttons
- RPG Game

'''

import turtle
import time

screen_width = 800
screen_height = 600

# Screen Setup
screen = turtle.Screen()
screen.title("Game Loop")
screen.bgcolor("white")
screen.tracer(0) # Stops refreshing the screen
screen.setup(screen_width, screen_height)

# Using Turtle Stamp to Create Button
button_stamp = turtle.Turtle()
button_stamp.penup()
button_stamp.hideturtle()
button_stamp.shape("square")
button_stamp.shapesize(stretch_wid=2, stretch_len=5, outline=5)
button_stamp.color("black", "yellow")
button_stamp.goto(-100, 200)
button_stamp.stamp()

# Using Turtle Draw to Create Button
button_draw = turtle.Turtle()
button_draw.penup()
button_draw.hideturtle()
button_draw.pencolor("black")
button_draw.fillcolor("green")
button_draw.pensize(5)
button_draw.goto(50, 180)

button_draw.pendown()
button_draw.begin_fill()
button_draw.goto(50, 220)
button_draw.goto(150, 220)
button_draw.goto(150, 180)
button_draw.goto(50, 180)
button_draw.end_fill()

# Using Turtle to Create Text
button_text = turtle.Turtle()
button_text.hideturtle()
button_text.penup()
button_text.goto(-100, 200)
button_text.write("Left Click", False, align="center", font=("Arial", 13, "bold"))
button_text.goto(100, 200)
button_text.write("Click Me Too", False, align="center", font=("Arial", 13, "bold"))

# This object is used for printing on the screen
text = turtle.Turtle()

def left_button_clicked(x, y):
    if x > -150 and x < -50 and y > 180 and y < 220:
        text.write("Left Clicked", False, align="center", font=("Arial", 30, "bold"))
        #print("left clicked")

def right_button_clicked(x, y):
    if x > 50 and x < 150 and y > 180 and y < 220:
        text.write("Right Clicked", False, align="center", font=("Arial", 30, "bold"))
        #print("right clicked")

# Master Click Function
def on_click(x, y):
    text.undo()
    left_button_clicked(x, y)
    right_button_clicked(x, y)

screen.onclick(on_click)

# Game Loop
while True:
    screen.update() # Refreshes manually

    # Codes

    time.sleep(.01)