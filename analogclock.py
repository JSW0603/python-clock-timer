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
c_circle.shapesize(1.3, 1.3)
c_circle.color("#c8c8c8")

#marking numbers
mark = turtle.Turtle()
mark.speed(0)
mark.color("#FFD700")

def mark_nums(hand_num, position1, position2):
    mark.penup()
    mark.hideturtle()
    mark.goto(position1, position2)
    mark.write(f"{hand_num}", align="center", font=("Time", 30, "bold"))

#mark 1
mark_nums("I", 140, 215)

#mark 2
mark_nums("II", 235, 120)

#mark 3
mark_nums("III", 270, -25)

#mark 4
mark_nums("IV", 235, -150)

#mark 5
mark_nums("V", 135, -245)

#mark 6
mark_nums("VI", 0, -280)

#mark 7
mark_nums("VII", -135, -245)

#mark 8
mark_nums("VIII", -225, -150)

#mark 9
mark_nums("IX", -265, -25)

#mark 10
mark_nums("X", -235, 110)

#mark 11
mark_nums("XI", -135, 215)

#mark 12
mark_nums("XII", 0, 250)

#draw a circle for calender
t.penup()
t.speed(0)
t.pensize(2)
t.hideturtle()
t.goto(0, -230)
t.pendown()
t.pencolor("#FFAF0A")
t.begin_fill()
t.circle(100, 360)
t.end_fill()


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

