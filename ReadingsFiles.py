# open() function is the function which allows you to open a
# a file in python

stuff = 'Hello\nWorld'
print(stuff)
print(len(stuff))

# This is not a "file" but it represents a handle to a sequence
# Using a "handle"
filehandle1 = open('example.txt')
count = 0
for line in filehandle1:
    count +=1
print('Line Count: ', count)
# This would count the number of lines in the example.txt filehandle

# Using the __contains__ function
try:
    filehandle2 = open('example.txt')
except:
    print("There was an error in loading the file!: ")
    quit()

for line in filehandle2:
    line = line.rstrip()
    if line.__contains__("you"):
        print(line)

# Using the input for this function
filename = input("Which file are you inquiring about?: ")

try:
    newFHandle = open('example.txt')
except:
    print("There was an error in loading the file!: ")
    quit()

wordQuery = input("And which word are you looking for?: ")
for line in newFHandle :
    if line.__contains__(wordQuery):
        print("We have found the word in: ")
        print(line)

