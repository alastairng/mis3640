import turtle
import math
# # def square(t, length):
# #         for i in range(4):
# #             t.fd(length)
# #             t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


# # square(jack, 200)

# polygon(jack, 80, 10)



def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    print(n, type(n))
    length = circumference / n
    polygon(t, length, n)

jack = turtle.Turtle()
circle(jack, 30)

turtle.mainloop()