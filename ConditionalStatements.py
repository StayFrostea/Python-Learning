y = 20
x = 10

# This should end up being the second digit
if y == x:
    print("Y is equal to x")
elif y != x:
    print("Y does not equal x")

# Try block
rawstr = input('Enter a number')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival >= 0:
    print('Succesful')
elif ival < 0:
    print("Didn't work")