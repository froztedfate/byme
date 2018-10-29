import turtle
import os


wn=turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350,0)


paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=2)
paddle_b.penup()
paddle_b.goto(350,0)


ball=turtle.Turtle()
ball.speed(-2)
ball.shape("square")
ball.color("white")
ball.penup()
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


while True:
	wn.update()
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	if (ball.ycor()>290):
		ball.sety(290)
		ball.dy*=-1
	elif ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	if (ball.xcor() > 350):
		ball.goto(0, 0)
		ball.dx *= -1
	elif ball.xcor() < -350:
		ball.goto(0, 0)
		ball.dx *= -1
	if (ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
		ball.dx *= -1
	elif (ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
		ball.dx *= -1




