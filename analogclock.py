import datetime
import turtle

#configure window for Analog clock
window = turtle.Screen()
window.setup(1000, 800)
window.bgcolor("black")
window.title("Analog Clock")

'''
If the argument of tracer() is 0. It has to be put update().
update() is used when tracer is turned off. 
'''

#Make turtle object
t = turtle.Turtle()

#set a turtle object color
t.color("#FFD700")

#draw a circle
t.penup()
t.speed(0)
t.pensize(20)
t.hideturtle()
t.goto(0, -290)
t.pendown()
t.fillcolor("#1E3269")
t.begin_fill()
t.circle(300, 360)
t.end_fill()

#create hour hand
h_hand = turtle.Turtle()
h_hand.shape("arrow")
h_hand.shapesize(0.5, 20)
h_hand.color("#FFD700")

#create minute hand
m_hand = turtle.Turtle()
m_hand.shape("arrow")
m_hand.shapesize(0.4, 28)
m_hand.color("#FFD700")

#create second hand
s_hand = turtle.Turtle()
s_hand.shape("arrow")
s_hand.shapesize(0.1, 30)
s_hand.color("#c8c8c8")

#create center circle
c_circle = turtle.Turtle()
c_circle.shape("circle")
c_circle.color("#c8c8c8")
c_circle.shapesize(1.3, 1.3)

#marking numbers
mark = turtle.Turtle()
mark.speed(0)
mark.color("#FFD700")

#mark 1
mark.penup()
mark.hideturtle()
mark.goto(140, 215)
mark.write("I", align="center", font=("Time", 30, "bold"))

#mark 2
mark.penup()
mark.hideturtle()
mark.goto(235, 120)
mark.write("II", align="center", font=("Time", 30, "bold"))

#mark 3
mark.penup()
mark.hideturtle()
mark.goto(270, -25)
mark.write("III", align="center", font=("Time", 30, "bold"))

#mark 4
mark.penup()
mark.hideturtle()
mark.goto(235, -150)
mark.write("IV", align="center", font=("Time", 30, "bold"))

#mark 5
mark.penup()
mark.hideturtle()
mark.goto(135, -245)
mark.write("V", align="center", font=("Time", 30, "bold"))

#mark 6
mark.penup()
mark.hideturtle()
mark.goto(0, -280)
mark.write("VI", align="center", font=("Time", 30, "bold"))

#mark 7
mark.penup()
mark.hideturtle()
mark.goto(-135, -245)
mark.write("VII", align="center", font=("Time", 30, "bold"))

#mark 8
mark.penup()
mark.hideturtle()
mark.goto(-225, -150)
mark.write("VIII", align="center", font=("Time", 30, "bold"))

#mark 9
mark.penup()
mark.hideturtle()
mark.goto(-265, -25)
mark.write("IX", align="center", font=("Time", 30, "bold"))

#mark 10
mark.penup()
mark.hideturtle()
mark.goto(-235, 110)
mark.write("X", align="center", font=("Time", 30, "bold"))

#mark 11
mark.penup()
mark.hideturtle()
mark.goto(-135, 215)
mark.write("XI", align="center", font=("Time", 30, "bold"))

#mark 12
mark.penup()
mark.hideturtle()
mark.goto(0, 250)
mark.write("XII", align="center", font=("Time", 30, "bold"))

#functions to move hands
def hourhand():
    currenthour = datetime.datetime.now().hour
    degree = (currenthour - 15) * -30
    currentminute = datetime.datetime.now().minute
    degree = degree + -0.5 * currentminute
    h_hand.setheading(degree)
    window.ontimer(hourhand, 60000)

def minutehand():
    currentminute = datetime.datetime.now().minute
    degree = (currentminute - 15) * -6
    currentsecond = datetime.datetime.now().second
    degree = degree + (-currentsecond * 0.1)
    m_hand.setheading(degree)
    window.ontimer(minutehand, 1000)

def secondhand():
    currentsecond = datetime.datetime.now().second
    degree = (currentsecond - 15) * -6
    s_hand.setheading(degree)
    window.ontimer(secondhand, 1000)

window.ontimer(hourhand, 1)
window.ontimer(minutehand, 1)
window.ontimer(secondhand, 1)
window.exitonclick()

