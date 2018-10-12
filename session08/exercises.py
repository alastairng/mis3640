Excercise 3:

# Split program
x = 'Print this list one character at a time, including commas.'
y= x.split(",")
print(y)

# Strip program
x = 'Remove spaces from this sentence.'
y = x.strip()
print(y)

# Replace program
x = 'Capitalize alastair.'
y = x.replace('a', 'A')
print(y)


Excercise 4:

items = [
    'bananas',
    'rice',
    'paprika',
    'potato chips'
]

def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    print(n,'$'+str(p))
price('bananas')
price（'rice')
price('paprika')
price('potato chips')
print("------------------------")
print('Total','$237')

