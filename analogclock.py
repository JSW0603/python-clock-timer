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
mark.goto()
mark.write("I", align="center", font=("Time", 30, "bold"))


turtle.done()
