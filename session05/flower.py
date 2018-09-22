# flower
import turtle
import math

def flower(t,r):
    t.circle(r)
    t.up()
    t.pos(0,r)
    t.down 
    for i in range(6):
        t.seth(360/6*i)
        t.circle(r,360/6)
        t.lt()

drawer=turtle.Turtle()
flower(drawer,100)
turtle.mainloop()
    



