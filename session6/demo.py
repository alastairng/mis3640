# age = 21

# if int(age) >= 18:
#     print('adult')
# elif int(age) >=6:
#     print('teenager')
# else:
#     print('kid')

# if x == y:
#     print('x and y are equal')



# def calculate_bmi(weight,height):
#     bmi = weigh / (height * height)
#     if bmi <= 18.5:
#         print("your bmi is {:.1f}. You are underweighted." .format(bmi)
#     elif 18.5 < bmi <= 25:
#         print("your bmi is {:.1f}. You are normal-weighted." .format(bmi)
#     elif 25 < bmi < 30:
#         print("your bmi is {:.1f}. You are overweighted." .format(bmi)
#     else 
#     print("your bmi is {:.1f}. You are obese." .format(bmi)

# weight = input('70')
# height = input('1.8')
# weight = float()
# height = float()

def compare(varA, varB):
    if isinstance(varA,str) or isinstance(varB,str):
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA==varB:
            print('equal')
        else: 
            print('smaller')

a = 'hello'
b = 3
c = 5 

compare(a,b)
compare(b,c)


return is_weekend and cigars >= 40 or 40 <= cigars <= 60

print( 30, False)