import turtle
import time

screen_height = 600
screen_width = 800

# Screen
screen = turtle.Screen()
screen.title("game loop")
screen.tracer(0) # stops the screen from refreshing
screen.setup(screen_width, screen_height) # sets up the size of our screen

# Setup left button
a = turtle.Turtle()
a.penup()
a.pencolor("black")
a.fillcolor("grey")
a.pensize(5)

a.goto(-20, -50)
a.pendown()
a.begin_fill()
a.goto(-300, -50)
a.goto(-300, -200)
a.goto(-20, -200)
a.goto(-20, -50)
a.end_fill()
a.hideturtle()

# Setup right button
b = turtle.Turtle()
b.penup()
b.pencolor("black")
b.fillcolor("grey")
b.pensize(5)

b.goto(20, -50)
b.pendown()
b.begin_fill()
b.goto(300, -50)
b.goto(300, -200)
b.goto(20, -200)
b.goto(20, -50)
b.end_fill()
b.hideturtle()

# Setup click detection
choose_a = False
choose_b = False
def a_clicked(x, y):
    global choose_a
    if x > -300 and x < -20 and y > -200 and y < -50:
        print("a clicked")
        choose_a = True

def b_clicked(x, y):
    global choose_b
    if x > 20 and x < 300 and y > -200 and y < -50:
        print("b clicked")
        choose_b = True

def on_click(x, y):
    a_clicked(x, y)
    b_clicked(x, y)

screen.onclick(on_click)

# Setup writing functions
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

def write_text(text):
    writer.goto(0, 100)
    writer.write(text, False, align="center", font=("Arial", 10, "bold"))

def write_a(text):
    writer.goto(-160, -130)
    writer.write(text, False, align="center", font=("Arial", 8, "normal"))

def write_b(text):
    writer.goto(160, -130)
    writer.write(text, False, align="center", font=("Arial", 8, "normal"))

def write_scene():
    writer.clear()
    print(scene)
    write_a(game[scene]["a"])
    write_b(game[scene]["b"])
    write_text(game[scene]["text"])


# MAIN: Setup your scene functions when the player chooses options

def zero_scene():
    global scene
    scene = "1"

def first_scene_a():
    global scene
    scene = "torch_lit"

def first_scene_b():
    global scene
    scene = "torch_away"

def read_entrance():
    global scene
    global cave_inscription
    cave_inscription = screen.textinput("Inscription", "What does the inscription say?")
    scene = "continue_in_cave"

def bleeding_knee():
    global scene
    global is_bleeding
    is_bleeding = True
    scene = "continue_in_cave"

def cave_forward1():
    global scene
    scene = "continue_in_cave"

def do_nothing():
    pass

# MAIN: Setup your scenes using the dictionary
game = {
    "0": {
        "text": "You stumble upon a cave opening in the cliffside. What do you do?",
        "a": "Go in of course.",
        "b": "Sorry, you're going in.",
        "a_action": zero_scene,
        "b_action": zero_scene
    },
    "1": {
        "text": "As you enter the cave you find a torch. Do you light it?",
        "a": "Light it up!",
        "b": "Let's put it away for now",
        "a_action": first_scene_a,
        "b_action": first_scene_b
    },
    "torch_lit": {
        "text": "With your torch lit, you see carved letters in the ground.",
        "a": "Read what is says",
        "b": "Ignore it and continue forward",
        "a_action": read_entrance,
        "b_action": cave_forward1
    },
    "torch_away": {
        "text": "You put the torch in your bag. As you continue forward your trip on the floor and scrape your knee.",
        "a": "You continue limping off through the cave",
        "b": "You pause to stop the bleeding",
        "a_action": bleeding_knee,
        "b_action": cave_forward1
    },
    "continue_in_cave": {
        "text": "What now?",
        "a": "",
        "b": "",
        "a_action": do_nothing,
        "b_action": do_nothing
    }
    
}

# MAIN: Game variables
scene = "0"
cave_inscription = ""
is_bleeding = False

# Game loop
write_scene()
while True:
    screen.update() # refreshes the screen manually
    
    if choose_a or choose_b:
        if choose_a:
            game[scene]["a_action"]()
        if choose_b:
            game[scene]["b_action"]()
        choose_a = False
        choose_b = False
        write_scene()

    
    time.sleep(.01) # Speed of game loop (lower is faster)
