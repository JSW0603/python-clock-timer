import turtle

#configure window for Analog clock
window = turtle.Screen()
window.setup(1000, 800)
window.bgcolor("black")
window.title("Analog Clock")
window.tracer(0)

#Make turtle object
t = turtle.Turtle()

#set a turtle object color
t.color("#FFD700")

#draw a circle
t.penup()
t.speed(0)
t.pensize(25)
t.hideturtle()
t.goto(0, -290)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(300, 360)
t.end_fill()


turtle.done()
