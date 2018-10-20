# import random

# pool = list(range(1, 71))
# print(random.sample(pool, 5))

import os
print(os.getcwd())

fout = open('session14/output.txt', 'a')

line1 = "How many roads must a man walk down \n"
fout.write(line1)
line2 = "Before you call him a man?\n"
fout.write(line2)

print(os.path.subpath('session14/output.txt'))

