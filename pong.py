
import turtle
import time
import winsound
#import simpleaudio as sa

window =  turtle.Screen()
window.title("Pong in python")
window.bgcolor("black")
window.setup(width=806,height=600)
window.tracer(0)
#main game loop

# Paddle A
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)
# Paddle B

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dy = 150
ball.dx = 150
# Function
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)
def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)
def paddle_right_up():
    y= paddle_right.ycor()
    y += 20
    paddle_right.sety(y)
def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,230)
pen.color("white")

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()
pen2.goto(-378,0)
pen2.color("white")
pen2.write("A.I.", align="center", font=("Courier",12,"bold") )
pen2.goto(378,0)
pen2.write("P1", align="center", font=("Courier",12,"bold") )
#keybord binding
window.listen()
#window.onkeypress(paddle_left_up, "w") 
#window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

start_time = time.time()

def check_paddle_upper_limit(obj):
    if(obj.ycor() >250):
        obj.sety(250)
def check_paddle_lower_limit(obj):
    if(obj.ycor()<-250):
        obj.sety(-250)
def check_paddle_limits(obj):
    check_paddle_lower_limit(obj)
    check_paddle_upper_limit(obj)

points_left  = 0
points_right = 0

start_time = time.time()
    
while True:
    window.update()
    current_time = time.time()
    
    delta_time = current_time - start_time
    #move ball
    ball.setx(ball.xcor() + ball.dx*delta_time )
    ball.sety(ball.ycor() + ball.dy*delta_time )

    if( (ball.ycor() < paddle_right.ycor()+50 ) & (ball.ycor()> paddle_right.ycor()-50) ):
        if(ball.xcor() > 335):
            winsound.PlaySound("Peep2.wav",winsound.SND_ASYNC)
            ball.dx *=-1
            ball.setx(335)
    if((ball.ycor() < paddle_left.ycor()+50)&(ball.ycor()>paddle_left.ycor()-50)):
        if(ball.xcor()< -335):
            winsound.PlaySound("Peep2.wav",winsound.SND_ASYNC)
            ball.dx *= -1
            ball.setx(-335)
            
    if(ball.xcor() < 0 and ball.dx < 0):
        if(ball.ycor() > paddle_left.ycor()+10):
            paddle_left_up()
        elif(ball.ycor() < paddle_left.ycor()-10):
            paddle_left_down()

    check_paddle_limits(paddle_left)
    check_paddle_limits(paddle_right)
    #check border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if(ball.xcor() > 340):
        winsound.PlaySound("Peep.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        points_left +=1
    if( ball.xcor() < -340):
        winsound.PlaySound("Peep.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *=-1
        points_right +=1

    pen.clear()
    pen.write("{} : {}".format(points_left,points_right), align="center", font=("Courier",50,"normal") )
    start_time = time.time()
 
    
