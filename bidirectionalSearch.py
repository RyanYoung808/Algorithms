#Author: Ryan Young
#Date: 8/15/19
#Location: MIT Open Course Ware, Introduction to Computer Science and Programming in Python (MIT 6.0001)
#Description: A basic bidirectional search algorithm. Does searches faster than a linear search.
#               Requires the array to be ordered smallest to largest
#Editing History
#8/15/19    Version 1.00     Created the program

import array as arr

#The target number you want to find. A hardcoded value, change in order to test.
targetNum = 11.31

#Start by creating an array of floats 0.0 - 100.0 representing percentages.
count = 0
addItem = 0
percentages = arr.array('d', [])
while (count != 10001):
    addItem = count / 100
    percentages.append(addItem)
    print ("The number", percentages[count], "has been placed into the array at location", count)
    count = count + 1

#search for a target number in the array with bisection search
highIndex = len(percentages)        #The highest index in the array you will search. Starts at 10,000
lowIndex = 0                        #The lowest index in the array you will search. Starts at 0
searchAt = 0                        #The box you want to search
discoveredValue = 0                 #The value that the box you searched contains
steps = 0                           #How many steps the bidirectional search algorythm has done. Tracks efficeiency.

while(discoveredValue != targetNum):
    searchAt = int((highIndex + lowIndex) / 2)      #search in the middle of the highest and lowest index
    discoveredValue = percentages[searchAt]         #grab the value at that middle index
    print("The loop looks at the value in box [", searchAt, "] and finds the value", discoveredValue)
    if(discoveredValue < targetNum):                #if the discovered value is smaller than the target
        lowIndex = searchAt                         #remove this entry and all lower entries from the search area
        print("Target not found, the loop will now search in boxes between,", highIndex, "and", lowIndex)
    elif(discoveredValue > targetNum):              #if the discovered value is larger than the target
        highIndex = searchAt                        #remove this entry and all higher entries from the search area
        print("Target not found, the loop will now search in boxes between,", highIndex, "and", lowIndex)
    else:
        print("The target has been found! Location ", searchAt, "contains value ", discoveredValue)
    steps = steps + 1
print("The search took", steps, "steps to complete")

