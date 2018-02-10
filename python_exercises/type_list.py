''' Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
*** test case 1: #input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
*** test case 2: # input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
*** test case 3: # input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns" '''

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']
l4 = [2, [55,77,33], 2.1, "end of list"]

def typeList(arr):
    sum = 0
    newStr = ""
    typesArr = [0, 0, 0]
    print "-----------------------------"
    print arr

    for i in range(len(arr)):
        # print "i:", i, "arr[i]: ", arr[i], " type: ", type(arr[i])

        # Integer: If it is a number, add it to a running sum
        if(type(arr[i]) is int or type(arr[i]) is float):
            sum = sum + arr[i]
            typesArr[0] = typesArr[0]+1

        # String:  concatenate it onto a new string
        if(type(arr[i]) is str):
            newStr = newStr + " " + arr[i]
            typesArr[1] = typesArr[1]+1

        # List: Instructions don't specify, so just print the list
        if(type(arr[i]) is list):
            print str(arr[i]) + " is a list"
            typesArr[2] = typesArr[2]+1
    # At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
    # To do this, check to see if there is more than one element=0 in typesArr[]
    print "newStr:", newStr
    print "sum:", str(sum)
    # print typesArr
   
    if (typesArr[0] == len(arr)):
        print "Input array is all type integer or float"
    elif (typesArr[1] == len(arr)):
        print "Input array is all type string"
    elif (typesArr[1] == len(arr)):
        print "Input array is all type list"
    else:
        print "Input array is mixed"

typeList(l1)
typeList(l2)
typeList(l3)
typeList(l4)
