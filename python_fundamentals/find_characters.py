''' Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
Here's an example:
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']'''

def findCharacters(arr, ch):
    print "search list:", str(arr), "for character:", ch
    new_arr = []
    for i in range (len(arr)):
        # print "i=", i, "arr[i].find(ch)=", arr[i].find(ch)
        if( arr[i].find(ch) > -1):
            new_arr.append(arr[i])
    return new_arr

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
print findCharacters(word_list, char)

print findCharacters(word_list, "n")

print findCharacters(word_list, "i")