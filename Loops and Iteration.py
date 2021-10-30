counter = 0
sumOfFunc = 0

# Showing a normal while loop
while counter < 15:
    sumOfFunc += counter
    print(sumOfFunc)
    counter += 1

# Showing the loop breaking statement
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# This is a for each statement
friends = {'Mary', 'Jerry', 'George', 'Katy'}
for name in friends:
    print(name)

# This is a loop idiomatic loop
nums = {1, 12, 45, 31, 2, 51}
for num in nums:
    num = num + 1
    print(num)

# Bit more complex of a loop
def findAThree(array):
    found = False
    numbers = array
    for inQuestion in numbers:
        if inQuestion == 3:
            found = True
            print("We found a 3!")
            break
    print(found)


intarray = {12, 41, 82, 15, 3, 92}
findAThree(intarray)
