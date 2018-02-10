''' Assignment: Making and Reading from Dictionaries -- Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.
Write a function that will print something like the following as it executes:
My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values. '''
#create an empty dictionary then add values
myself = {} 
#populate dictionary
myself["name"] = "Cindy"
myself["age"] = "101"
myself["country of birth"] = "USA"
myself["favorite language"] = "French"
myself["favorite activity"] = "cycling"
def printDict(obj):
    # print all keys and values in dictionary
    for key,value in obj.iteritems():
        print "My", key,"is", value

    #look at other ways to print dictionary
    print "\n", "---- other ways to print dictionary ----"

    #print all keys
    print "\n", "Print all keys:"
    for data in obj:
        print data

    #another way to print all keys
    print "\n", "Print all keys another way:"
    for obj_key in obj.iterkeys():
        print obj_key

    #to print the values
    print "\n", "Print all values:"
    for val in obj.itervalues():
        print val

printDict(myself)
