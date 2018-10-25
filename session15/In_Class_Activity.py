class Circle: 
 """Represents a point in 2-D space.
     attributes: x, y
 """
 
class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
my_point = Point()
my_point.x = 1
my_point.y = 1
 
class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    Corner is a point type 
    """
 
 
def point_in_circle(point,circle):
    if (point.x > (circle.center.x + circle.radius)) or (point.x < (circle.center.x - circle.radius)):
        return False
    elif (point.y > (circle.center.y + circle.radius)) or (point.y < (circle.center.y - circle.radius)):
        return False
    else:
        return True
 
 
def rect_in_circle(rect, circle):
    if (rect.corner.x > (circle.center.x + circle.radius)) or (rect.corner.x < (circle.center.x - circle.radius)):
        return False
    elif (rect.corner.y > (circle.center.y + circle.radius)) or (rect.corner.y > (circle.center.y - circle.radius)):
        return False
    else:
        return True

def rect_circle_overlap(rect, circle):
    if (rect.corner.x == (circle.center.x + circle.radius)) or (rect.corner.x == (circle.center.x - circle.radius)):
        return True
    elif (rect.corner.y ==  (circle.center.y + circle.radius)) or (rect.corner.y == (circle.center.y - circle.radius)):
        return True
    else:
        return False
 
def main():
    my_circle = Circle()
    my_circle.center = my_point
    my_circle.center.x = 150
    my_circle.center.y = 100
    my_circle.radius = 75
 
    print(point_in_circle(my_point, my_circle))
 
    al_rect = Rectangle()
    al_rect.width = 10
    al_rect.height = 10
    al_rect.corner = my_point
 
    print(rect_in_circle(al_rect, my_circle))
 
    print(rect_circle_overlap(al_rect,my_circle))


main()

# ---------------------------------------------------------------

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
time = Time()
time.hour = 11
time.minute = 59
time.second = 30 


# Here is a simple prototype of add_time:
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  0
 
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
print(done)

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return time_to_int(seconds)



def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


# def add_time_2(t1, t2):
#     if not valid_time(t1) or not valid_time(t2):
#         raise ValueError('invalid Time object in add_time')
#     seconds = time_to_int(t1) + time_to_int(t2)
#     return time_to_int(seconds)


# def add_time(t1, t2):
#     assert valid_time(t1) and valid_time(t2)
#     seconds = time_to_int(t1) + time_to_int(t2)
#     return time_to_int(seconds)

