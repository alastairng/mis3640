42 * 60 + 42
10 / 1.61
6.21 / (2562 / 60)
6.21 / 2562
6.21 / (2562 / 60 / 60)

import math
math.pi
radius= 5
sphere_volume= (4/3) * math.pi * radius ** 3

print('Volume of a sphere with radius 5: {:.2f}' .format(sphere_volume))

book_price= 24.95
book_cost= 24.95*0.6 * 60
shipping_cost= 3 + 0.75*59
total_cost= book_cost + shipping_cost

print('The wholesale cost for 60 copies is: ${:.2f}' .format(total_cost))

print('I get home for breakfast at: {:d}:{:d}' .format(7, 30))

percentage_change= ((89/82)-1)*100

print('My average grade increased by: {:.1f}%' .format(percentage_change))



# The time module provides a function, also named time, 
# that returns the current Greenwich Mean Time in “the epoch”, 
# which is an arbitrary time used as a reference point. 
# On UNIX systems, the epoch is 1 January 1970.

import time
time.time()
1437746094.5735958

# Write a script that reads the current time and converts it to a 
# time of day in hours, minutes, and seconds, plus the number of days since the epoch.

epoch = time.time()
seconds_day = 24 * 60 * 60
seconds_hours = 60 * 60
seconds_minutes = 60

days = epoch // seconds_day
hours = (epoch % seconds_day) // seconds_hours 
minutes = (epoch % seconds_day) % seconds_hours // seconds_minutes
seconds = (epoch % seconds_day) % seconds_hours % seconds_minutes
print("{:.f} : {:.f} :{:.f} :{:.f}" .format (days, hours, minutes, seconds))

