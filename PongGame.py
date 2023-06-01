import turtle
import random
import time
import winsound

borderX = 550  # Spielzohne
border_X = -550  #
borderY = 250  #
border_Y = -250  #

bg_color = ["black", "Lavender", "salmon", "green"]

ball_color = ["red", "white", "gray", "pink", "blue", "cyan", "purple", "navy"]
ball_speedX = list(range(-15, 15))  # Geschwindigkeit des Balls
ball_speedY = list(range(-15, 15))

score_a = 0  # Zähler
score_b = 0

player1 = input("Player Name 1: ")
player2 = input("Player Name 2: ")
finish = int(input("Punkte bis GameOver: "))

# Window
window = turtle.Screen()  # Window erstellen
window.setup(width=1200, height=600)  #
window.bgcolor("black")  #
window.title("MyPong")  #
window.tracer(1)  #

# Spielfeld
worker = turtle.Turtle()
worker.speed(0)
worker.begin_fill()
worker.color(random.sample(bg_color, 1))
worker.goto(border_X, borderY)
worker.goto(borderX, borderY)
worker.goto(borderX, border_Y)
worker.goto(border_X, border_Y)
worker.goto(border_X, borderY)
worker.end_fill()
worker.goto(0, borderY)
worker.pensize(5)
worker.setheading(90)
worker.pencolor("white")
worker.goto(0, border_Y)
worker.penup()
worker.goto(35, 0)
worker.pendown()
worker.begin_fill()  # Zufall ! Nachfragen warum so
worker.circle(35)  # Zufall ! Nachfragen warum so
worker.end_fill()  # Zufall ! Nachfragen warum so
worker.hideturtle()

# Rocket_L
Lrocket = turtle.Turtle()
Lrocket.speed(3)
Lrocket.color("white")
Lrocket.shape("square")
Lrocket.shapesize(stretch_wid=5, stretch_len=0.5)  # 50 pix, 5pix
Lrocket.penup()
Lrocket.goto(border_X, 0)

# Rocket_R
Rrocket = turtle.Turtle()
Rrocket.speed(3)
Rrocket.color("white")
Rrocket.shape("square")
Rrocket.shapesize(stretch_wid=5, stretch_len=0.5)  # 50pix, 5pix
Rrocket.penup()
Rrocket.goto(borderX, 0)

# Ball
ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(1)
ball.color("white")
ball.CorX = random.choice(ball_speedX)  # x veränderung per Schritt
ball.CorY = random.choice(ball_speedY)  # y veränderung per Schritt

# Score_b
scoreB = turtle.Turtle()
scoreB.speed(0)
scoreB.hideturtle()
scoreB.color("white")
scoreB.penup()
scoreB.goto(borderX / 2, borderY + 25)
scoreB.write(score_b, font=("calibri", 18))

# Name2
name2 = turtle.Turtle()
name2.speed(0)
name2.hideturtle()
name2.color("gold")
name2.penup()
name2.goto(borderX / 2 + 40, borderY + 25)
name2.write(player2, font=("calibri", 18))

# Score_a
scoreA = turtle.Turtle()
scoreA.speed(0)
scoreA.hideturtle()
scoreA.color("white")
scoreA.penup()
scoreA.goto(border_X / 2, borderY + 25)
scoreA.write(score_a, font=("calibri", 18))

# Name
name = turtle.Turtle()
name.speed(0)
name.hideturtle()
name.color("gold")
name.penup()
name.goto(border_X / 2 + 40, borderY + 25)
name.write(player1, font=("calibri", 18))


def move_up():
    y = Lrocket.ycor() + 25  # Koordinaten auslesen und 25 addieren
    if y > 200:  # Grenze die nict überschritten werden darf
        y = 200  # Schläger auf Grenzwert setzen
    Lrocket.sety(y)  #


def move_down():
    y = Lrocket.ycor() - 25
    if y < -200:
        y = -200
    Lrocket.sety(y)


def move_down2():
    y = Rrocket.ycor() - 25
    if y < -200:
        y = -200
    Rrocket.sety(y)


def move_up2():
    y = Rrocket.ycor() + 25
    if y > 200:
        y = 200
    Rrocket.sety(y)


window.listen()  # damit Window auf erreignisse reagiert
window.onkeypress(move_up, "w")  # Funktion aufrufen wenn taste gedrückt ist
window.onkeypress(move_down, "s")

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")

while True:
    ball.setx(ball.xcor() + ball.CorX)  # Geschwindigkeit des Balls festlegen
    ball.sety(ball.ycor() + ball.CorY)

    if ball.ycor() >= 240:  # Aufprall von der oberen und unteren Grenze
        ball.CorY = -ball.CorY
    if ball.ycor() <= -240:
        ball.CorY = -ball.CorY

    if ball.xcor() >= 550:  # Wenn der Ball nicht zurückgeschlagen wurde
        scoreA.clear()
        score_a = score_a + 1
        scoreA.write(score_a, font=("calibri", 18))
        ball.speed(0)
        ball.goto(0, random.randrange(-237, 237))
        ball.color(random.sample(ball_color, 1))
        ball.CorX = random.choice(ball_speedX)
        if ball.CorX == 0:
            ball.CorX = random.choice(ball_speedX)
        ball.CorY = random.choice(ball_speedY)
        if ball.CorY == 0:
            ball.CorY = random.choice(ball_speedX)

    if ball.xcor() <= -550:
        scoreB.clear()
        score_b = score_b + 1
        scoreB.write(score_b, font=("calibri", 18))
        ball.speed(0)
        ball.goto(0, random.randrange(-237, 237))
        ball.color(random.sample(ball_color, 1))
        ball.CorX = random.choice(ball_speedX)
        if ball.CorX == 0:
            ball.CorX = random.choice(ball_speedX)
        ball.CorY = random.choice(ball_speedY)
        if ball.CorY == 0:
            ball.CorY = random.choice(ball_speedY)

    if (
            ball.ycor() >= Lrocket.ycor() - 50 and ball.ycor() <= Lrocket.ycor() + 50) and ball.xcor() >= Lrocket.xcor() - 25 and ball.xcor() <= Lrocket.xcor() + 25:
        Lrocket.color(random.sample(ball_color, 1))  # Aufprall gegen Schläger Links
        ball.color(random.sample(ball_color, 1))
        ball.CorX = -ball.CorX

    if (
            ball.ycor() >= Rrocket.ycor() - 50 and ball.ycor() <= Rrocket.ycor() + 50) and ball.xcor() >= Rrocket.xcor() - 25 and ball.xcor() <= Rrocket.xcor() + 25:
        Rrocket.color(random.sample(ball_color, 1))  # Aufprall gegen Schläger Rechts
        ball.color(random.sample(ball_color, 1))
        ball.CorX = -ball.CorX

    if score_a == finish or score_b == finish:
        ball.setposition(0, 0)
        ball.setx(0)
        ball.sety(0)
        ball.write("Game Over", align="center", font=("calibri", 44))
        time.sleep(True)

window.mainloop()
