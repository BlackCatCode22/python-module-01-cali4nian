# Boolean Expressions
print(5 == 5) # true
print(5 == 6) # false

print(type(True))
print(type(False))

# Logical operators
x = 1
y = 2
print(x > y)
print(not (x > y))
print(17 and True)

# Conditional execution
if x > 0 :
    print('x is positive')

if x > y:
    print(x)
    print(y)

if x < 0 :
    pass   # need to handle negative values, do nothing for now.

x = 3
if x < 10:
    print('Small')

# Alternative execution
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

# Chained conditionals
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

choice = 'a'

if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

# Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < x < 10:
    print('x is a positive single-digit number.')

# Catching exceptions using try and except
prompt = "What is the air velocity of an unladen swallow?\n"
speed = input(prompt)
int(speed)

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

# Short-circuit evaluation of logical expressions
x = 6
y = 2
print(x >= 2 and (x/y) > 2)

x = 1
y = 0
print(x >= 2 and (x/y) > 2)

x = 6
y = 0
print(x >= 2 and (x/y) > 2)

x = 1
y = 0
print(x >= 2 and y != 0 and (x/y) > 2)

x = 6
y = 0
print(x >= 2 and y != 0 and (x/y) > 2)

print( x >= 2 and (x/y) > 2 and y != 0)

# Debugging
x = 5
    # y = 6