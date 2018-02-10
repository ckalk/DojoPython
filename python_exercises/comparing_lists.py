''' Assignment: Compare Lists
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two: '''
list_one_1 = [1,2,5,6,2]
list_two_1 = [1,2,5,6,2]

list_one_2 = [1,2,5,6,5]
list_two_2 = [1,2,5,6,5,3]

list_one_3 = [1,2,5,6,5,16]
list_two_3 = [1,2,5,6,5]

list_one_4 = ['celery','carrots','bread','milk']
list_two_4 = ['celery','carrots','bread','cream']


def compareLists(arr1, arr2):
    print arr1
    print arr2

    isSame = True
    n1 = len(arr1)
    n2 = len(arr2)

    if (n1 != n2):
        print "failed length comparison"
        isSame = False
        return isSame
    for i in range (n1):
        if(arr1[i] != arr2[i]):
            print "failed value comparison"
            isSame = False
            return isSame
    print "passed length & value comparison if you see this"
    return isSame

def printComparison (arr1, arr2):
    if (compareLists(arr1, arr2)):
        print "The two lists are identical"
    else:
        print "The two lists differ"
    print " -------------------------------"

printComparison (list_one_1, list_two_1)
printComparison (list_one_2, list_two_2)
printComparison (list_one_3, list_two_3)
printComparison (list_one_4, list_two_4)