'''
NOTE: Place code into Visual Studio to run

LESSON 10: Improved Turtle Movement

Primarily learned about turtle movements in the past that utilizes forward, backward, left, right...

Now we will focus on moving the turtle by setting its coordinates and using it in a game loop.

---

MOVING TURTLE WITH COORDINATES:

# Get/Set both X and Y coordinates
    print("Pos =", t.pos())
    t.setpos(100, 100)
    print("Pos = ", t.pos())

# Get/Set the X coordinate
    print("X = ", t.xcor())
    t.setx(-50)
    print("X = ", t.xcor())

# Get/Set the Y coordinate
    print("Y = ", t.ycor())
    t.sety(35)
    print("Y = ", t.ycor())

---

COLLISION DETECTION:

How do we detect collision when our turtle collides with something in the game?

There are plenty of things we can think of when it comes to the turtle colliding:
- Bouncing off walls
- Colliding with other players

By default our turtle can run outside of the screen boundaries, so we want confine the turtle inside by having it bouncing back.
'''
import turtle
import time

# Screen Setup
screen_width = 800
screen_height = 600

bottom_screen = -(screen_height / 2)
top_screen = screen_height / 2
left_screen = -(screen_width / 2)
right_screen = screen_width / 2

screen = turtle.Screen()
screen.title("Lesson 10")
screen.bgcolor("PeachPuff2")
screen.tracer(0) # Stops the screen from refreshing
screen.setup(screen_width, screen_height)

# Turtle Setup
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.up()

# Turtle Controls
def player_up():
    # Move turtle up
    y = t.ycor()
    y += 5
    t.sety(y)

def player_down():
    # Move turtle down
    y = t.ycor()
    y -= 5
    t.sety(y)

def player_left():
    # Move turtle left
    x = t.xcor()
    x -= 5
    t.setx(x)

def player_right():
    #Move turtle right
    x = t.xcor()
    x += 5
    t.setx(x)

screen.listen() # Need this or the key press will not work
screen.onkeypress(player_up, "Up")
screen.onkeypress(player_down, "Down")
screen.onkeypress(player_left, "Left")
screen.onkeypress(player_right, "Right")

x_move = 3
y_move = 3

def t_move():
    x = t.xcor()
    x += x_move
    t.setx(x)

    y = t.ycor()
    y += y_move
    t.sety(y)

def t_collision():
    global x_move
    global y_move

    x = t.xcor()
    y = t.ycor()

    if y >= top_screen:
        y_move = -1 * y_move
    
    if y <= bottom_screen:
        y_move = -1 * y_move

    if x >= right_screen:
        x_move = -1 * x_move

    if x <= left_screen:
        x_move = -1 * x_move

# Game Loop
while True:
    screen.update() # Refreshes the screen manually
    t_move()
    t_collision()
    time.sleep(.01) # Speed of game loop (lower is faster)