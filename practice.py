import turtle
import math


# def flower(t,r):
#     t.circle(r)
#     t.up()
#     t.setpos(0,r)
#     t.down()
#     for i in range(6):
#         t.seth(i*60)
#         t.circle(r,360/6)
#         # t.lt(120)  
#         t.seth(180+i*60)
#         t.circle(r,360/6)

def yingyang(t,r):
    t.circle(r)
    t.up()
    t.setpos(0,r*2)
    t.down()
    t.seth(240)
    t.circle(r,360/6)
    t.up()
    t.setpos(0,0)
    t.down()
    t.seth(60)
    t.circle(r,360/6)
    t.up()
    t.setpos(-r/4,2*r/3)
    t.down()
    t.circle(r/5)
    t.up()
    t.setpos(r/2,r+2*r/3)
    t.down()
    t.circle(r/5)


drawer=turtle.Turtle()
drawer.speed(20)

yingyang(drawer,100)
# flower(drawer,100)

turtle.mainloop()