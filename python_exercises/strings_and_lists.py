# Find and Replace: In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
words = "It's thanksgiving day. It's my birthday,too!"
print words
dayPosition = words.find("day")
print dayPosition
newWords = words.replace("day", "month")
print newWords

# Min and Max: Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print x
min = x[0]
max = x[0]
for i in range( 1, len(x)):
    if ( x[i] < min ):
        min = x[i]
    if ( x[i] > max ):
        max = x[i]
print "min of x=", min
print "max of x=", max

# First and Last: Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
print x
print "first value =", x[0]
print "last value =", x[len(x)-1]
newList = [ x[0], x[len(x)-1] ]
print "new list = ", newList

# New List: Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
n = len(x)
x.sort()
print x
firstHalf = x[:n/2]
print firstHalf
newList = [firstHalf]
newList[1:n/2] = x[n/2:n]
print newList
