''' Assignment: Checkerboard
Write a program that prints a 'checkerboard' pattern to the console. Your program should require no input and produce console output that looks like so:
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping. '''

# approach 1: using a 2d list
print " ----- Approach 1 -------"
numRows = 8
numCols = 8
# Creates a list containing numRows lists, each of numCols items, all set to " "
arr = [[" " for i in range(numRows)] for j in range(numCols)] 
firstStarPos = 0
for i in range(numRows):
    fmt = ''
    for j in range (firstStarPos, numCols,2):
        arr[i][j] = "*"
        fmt += "{}{}"
    # print arr[i]
    # print fmt
    print fmt.format(*arr[i])
    firstStarPos = (firstStarPos + 1) % 2

# approach 2: build print string on the fly
print " ----- Approach 2 -------"
numRows = 8
numCols = 8
firstStarPos = 0
for i in range(numRows):
    printStr = ""
    if((i+1) % 2 == 1):
        printStr+=" "
        firstStarPos = 2
    for j in range (firstStarPos, numCols+1, 2):
        printStr+="* "
    print printStr
    firstStarPos = (firstStarPos + 1) % 2
