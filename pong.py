
import turtle

# --- Main Menu Implementation ---


def show_main_menu(screen):
    screen.title("Pong-Ping Main Menu")
    screen.bgcolor("black")
    screen.tracer(0)

    # Title
    title = turtle.Turtle()
    title.hideturtle()
    title.color("white")
    title.penup()
    title.goto(0, 120)
    title.write("PONG-PING", align="center", font=("Courier", 40, "bold"))

    # Play Button
    play_btn = turtle.Turtle()
    play_btn.hideturtle()
    play_btn.penup()
    play_btn.goto(0, 40)
    play_btn.shape("square")
    play_btn.shapesize(stretch_wid=2, stretch_len=8)
    play_btn.color("#4444ff")
    play_btn.showturtle()
    play_btn.write("Play", align="center", font=("Courier", 24, "normal"))

    # Settings Button
    settings_btn = turtle.Turtle()
    settings_btn.hideturtle()
    settings_btn.penup()
    settings_btn.goto(0, -40)
    settings_btn.shape("square")
    settings_btn.shapesize(stretch_wid=2, stretch_len=8)
    settings_btn.color("#44ff44")
    settings_btn.showturtle()
    settings_btn.write("Settings", align="center", font=("Courier", 24, "normal"))

    # Exit Button
    exit_btn = turtle.Turtle()
    exit_btn.hideturtle()
    exit_btn.penup()
    exit_btn.goto(0, -120)
    exit_btn.shape("square")
    exit_btn.shapesize(stretch_wid=2, stretch_len=8)
    exit_btn.color("#ff4444")
    exit_btn.showturtle()
    exit_btn.write("Exit", align="center", font=("Courier", 24, "normal"))

    menu_state = {'running': True}

    # Button click logic
    def on_click(x, y):
        # Play button area
        if -80 < x < 80 and 20 < y < 60:
            # Clear menu and start game
            title.clear()
            play_btn.clear()
            settings_btn.clear()
            exit_btn.clear()
            screen.onclick(None)
            menu_state['running'] = False
        # Settings button area
        elif -80 < x < 80 and -60 < y < -20:
            title.clear()
            play_btn.clear()
            settings_btn.clear()
            exit_btn.clear()
            title.goto(0, 0)
            title.write("Settings (Not implemented)", align="center", font=("Courier", 24, "normal"))
        # Exit button area
        elif -80 < x < 80 and -140 < y < -100:
            turtle.bye()
            import sys
            sys.exit()

    screen.onclick(on_click)
    screen.listen()
    while menu_state['running']:
        screen.update()


# Set up the screen (shared for menu and game)
wn = turtle.Screen()
wn.setup(width=800, height=600)

# Show main menu before starting the game
show_main_menu(wn)

# Now set up the game screen
wn.title("Pong")
wn.bgcolor("black")
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("purple")  # Set ball color to purple
ball.penup()
ball.goto(0, 0)
ball.dx = 0.175
ball.dy = 0.175

# Score
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


# Main game loop with win condition
def main_game_loop():
    global score_a, score_b
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            update_score()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            update_score()

        # Paddle and ball collisions
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60):
            ball.setx(340)
            ball.dx *= -1

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
            ball.setx(-340)
            ball.dx *= -1

        # Win condition
        if score_a >= 10 or score_b >= 10:
            winner = "Player A" if score_a >= 10 else "Player B"
            score_display.goto(0, 0)
            score_display.color("yellow")
            score_display.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
            break

main_game_loop()
