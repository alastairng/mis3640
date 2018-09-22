import math
import turtle
import turtle

Jack = turtle.Turtle()


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)


def Yang(t, r):
    t.penup()
    t.goto(0, r * 2)
    t.pendown()
    t.circle(r/2, 180)

def Yin(t, r):
    t.circle(r/2, 180)

def Upper(t, r):
    t.penup()
    t.goto(0, r + r/3)
    t.pendown()
    t.circle(r/6, 360)


def Lower(t, r):
    t.penup()
    t.goto(0, r/3)
    t.pendown()
    t.circle(r/6, 360)

circle(Jack, 50)

Yin(Jack, 50)
Yang(Jack, 50)
Upper(Jack, 50)
Lower(Jack, 50)

turtle.mainloop()
