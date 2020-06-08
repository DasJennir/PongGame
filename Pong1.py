import turtle
import os
import time
from datetime import datetime
from threading import Timer

wn =  turtle.Screen()
wn.title("Pong by @EchoFoxtrot")
wn.bgcolor("#edb879")
wn.setup(width=1000, height=1000)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#1979a9")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-480, 0)

#Score

score_a = 0
score_b = 0 


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#1979a9")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(480, 0)


# Ball
ball = turtle.Turtle()
ball.speed(10000000000)
ball.shape("square")
ball.color("#80391e")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.2

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 450)
pen.write('Player A:  Player B: ', align='center', font=("Courier",24,'bold'))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def exitfunc():
    datetime.now()
    os._exit(0)
    
    
#Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Gamme Loop

while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 490:
        ball.sety(490)
        ball.dy *= -1

    if ball.ycor() < -490:
        ball.sety(-490)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=("Courier",24,'bold'))


    if ball.xcor() < -490:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=("Courier",24,'bold'))

    if score_a > 4:
        pen.clear()
        pen.write('Player A is the Winner', align='center', font=("Courier",24,'bold'))
        Timer(3, exitfunc).start()

    if score_b > 4:
        pen.clear()
        pen.write('Player B is the Winner', align='center', font=("Courier",24,'bold'))
        Timer(3, exitfunc).start()


    #Paddle and Ball colision    
    if (ball.xcor() > 455 and ball.xcor() < 460) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -450 and ball.xcor() > -455) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    
    
    

