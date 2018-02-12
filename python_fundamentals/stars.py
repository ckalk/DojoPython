''' Assignment: Stars --Write the following functions.
Part I; Create a function called draw_stars() that takes a list of numbers and prints out *.
For example:
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following when invoked:
****
******
*
***
*****
*******
*************************

Part II; Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
For example:
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x) should print the following in the terminal:
****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj '''

# Part I; Create a function called draw_stars() that takes a list of numbers and prints out *.
print "--------  Stars: Part I --------"
def draw_stars(arr):
    print "input list: ", arr, "\n"
    prntStr = ''
    for i in arr:
        prntStr = "*" * i
        print prntStr
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

#Part II; Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
print "\n","--------  Stars: Part II --------"
def draw_stars2(arr):
    print "input list: ", arr, "\n"
    prntStr = ''
    prntChr =''
    num = 0
    for i in range( len (arr) ):
        # print "i=", i, " arr[i]=", arr[i], "type =", type(arr[i])
        if(type(arr[i]) is str):
            # print arr[i].lower(), arr[i].lower()[0]
            num = len(arr[i])
            prntChr = arr[i].lower()[0]
        else:
            num = arr[i]
            prntChr = "*"
        prntStr = prntChr * num
        print prntStr

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
