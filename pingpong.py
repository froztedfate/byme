import turtle
import os
wn=turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer()
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")0
paddle_a.shapesize(strecth_wid=5,stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")0
paddle_b.shapesize(strecth_wid=5,stretch_len=2)
paddle_b.penup()
paddle_b.goto(350,0)
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")0
ballpenup()
ball.goto(0,0)
ball.dx=2
ball.dy=2
def paddleaup():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)
def paddleadown():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)
wn.listen()
wn.onkeypress(paddleaup,"r")
wn.onkeypress(paddleadown,"d")
def paddlebup():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)
def paddlebdown():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddlebup,"p")
wn.onkeypress(paddlebdown,"l")







