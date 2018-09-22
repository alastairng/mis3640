# # result = 0 

# # # for i in range(1,10):
# # #     print('current number to be added', i+1)
# # #     result = result + i
# # #     print('new result after this iteration', result)
# # #     print('The final result:', result)

# # for i in range (1,1001):
# #     if i % 2 == 1:
# #         result = result + i
# # print('The sum of odd numebrs is', result)

# # for i in range(1, 1001, 2):
# #     result = result + i

# # print('The sum of the odd numbers is', result)

# # result = 1

# # for i in range(1,11):
# #     result = result * i 

# # print('The factorial of 10 is', result)

# # def countdown(n):
# #     while n > 0:
# #         print(n)
# #     n = n-1
# #     print('Blastoff!')

# # counter = 0 
# # while counter < 10:
# #     print(r"Here's Johnny!")
# #     counter = 

# while True:
#     line = input ('>')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + ")
    
