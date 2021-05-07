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

# Turtle Setup (Ball(b) / Paddle(t))
b = turtle.Turtle()
b.shape("circle")
b.color("red")
b.up()
b.setpos(0, 50)

t = turtle.Turtle()
t.shape("square")
t.color("green")
t.up()
t.shapesize(stretch_wid=1, stretch_len=10)
t.sety(bottom_screen + 20)

# Player Controls
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

# Collision Setup
x_move = 3
y_move = 3
ball_in_air = True

# Checks collision between player and ball
def ball_player_collision():
    player_left = t.xcor() - 10 * 10 # Account for size stretch
    player_right = t.xcor() + 10 * 10 # Account for size stretch
    player_bottom = t.ycor() - 10
    player_top = t.ycor() + 10

    ball_left = b.xcor() - 10
    ball_right = b.xcor() + 10
    ball_bottom = b.ycor() - 10
    ball_top = b.ycor() + 10

    x_axis = False
    y_axis = False

    if ball_bottom <= player_top and ball_top >= player_bottom:
        x_axis = True
    if ball_left <= player_right and ball_right >= player_left:
        y_axis = True

    return x_axis and y_axis # This will return the condition result

def ball_move():
    x = b.xcor()
    x += x_move
    b.setx(x)

    y = b.ycor()
    y += y_move
    b.sety(y)

def ball_collision():
    global x_move
    global y_move
    global ball_in_air
    x = b.xcor()
    y = b.ycor()

    if y >= top_screen:
        y_move = -1 * y_move
    elif x >= right_screen:
        x_move = -1 * x_move
    elif x <= left_screen:
        x_move = -1 * x_move
    elif ball_player_collision():
        y_move = -1 * y_move
    elif y <= bottom_screen:
        ball_in_air = False # Ends the game


screen.listen() # Need this or the key press will not work
screen.onkeypress(player_left, "Left")
screen.onkeypress(player_right, "Right")

# Game Loop
while ball_in_air:
    screen.update() # Refreshes the screen manually
    
    ball_move()
    ball_collision()
    
    time.sleep(.01) # Speed of game loop (lower is faster)