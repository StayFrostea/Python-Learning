# Lists can be of different types.
weirdList = ['red', 24, 'george']
print(weirdList[1])
print(weirdList[0])

# Lists are Mutable

weirdList[2] = 'purple'
print(weirdList[2])

# Using the range iterator
for item in range(len(weirdList)):
    print(weirdList[item])

# List functions
weirdList.append(32)
weirdList.insert(0, 'Banana')
print(weirdList)

# Sorting
nameList = ['Joseph', 'Sarah', 'Garry']
print(nameList)
nameList.sort()
print(nameList)

# Using split()
# This works with whitespaces
sentence = 'There is so many words in this sentence, it is unbelievable!'
words = sentence.split()
print(words)

# Useful alternation is for CSV file which uses ",' a comma to seperate
csvFake = "this,is,some,sort,of,csv,file"
csvItems = csvFake.split(',')
print(csvItems)
