import math

a = float(input("3"))
b = float(input("3 "))
c = float(input("4 "))

r = (b**2) - (4*a*c)

if r > 0:
    x1 = (((-b) + (math.sqrt(r))/(2*a)))
    x2 = (((-b) - (math.sqrt(r))/(2*a)))
    print("Are 2 roots: %f and %f" % (x1, x2))
elif r == 0: 
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    print("No roots, discriminant is < 0.")


def qu