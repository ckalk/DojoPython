# In the code below, you have created your own custom Python module/library that others can use! How can others use the methods in your library? By calling the properties stored in the class you defined (e.g. _.map(), _. reduce(), _.find(), etc).
# * Your assignment is to implement the 5 methods below using delegating callbacks. You will have to modify the 5 methods to take in an array and a callback. Use what you learned in the previous chapter about callbacks to complete the assignment.
# One important concept that we want you to learn through this assignment is how to pass data to and from callbacks. You pass data to a callback with a parameter and you pass data from the callback back to the parent function with a return. While you are going through this assignment pay close attention to this relationship.
# * To understand what each method does, please refer to the underscore library. Note that your method does not have to be as robust as underscore's; you just need to get the base functionality working. Therefore for most methods you will only have the list and a lambda as parameters, and for the lambda you will pass in each element and potentially a "memo" also known as a "collector".
# * Note that some of these functions already exist in Python. We want you to explore how you might implement these yourself. Be aware that these tools exist to help work in a design idiom known as "functional programming". It's not something that we cover here, but is a topic you may want to explore on your own. It is mainly used in data science in recent years.

class Underscore(object):

    def map(self, arr, cb):
        # map: Produces a new array of values by mapping each value in list through a transformation function (iteratee). The iteratee is passed three arguments: the value, then the index (or key) of the iteration, and finally a reference to the entire list.
        print "arr=", arr
        newarr = []
        for i in range(len(arr)):
            # print "i", i, " arr[i]", arr[i]
            # print "cb(arr[i])", cb(arr[i])
            newarr.append(cb(arr[i]))
        return newarr


    def reduce(self, arr, cb, memo):
    # _.reduce(list, iteratee, [memo])
    # reduce boils down a list of values into a single value. Memo is the initial state of the reduction, and each successive step of it should be returned by iteratee. 
    # When _.reduce([1, 2, 3, 4, 5], function(memo, num) { return memo + num; }, 5); is called, the following happens:
    #     memo starts at 5
    #     memo + list[0] = memo = 6
    #     ...
    #     memo + list[4] = memo = 20
    # or
    # _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0)
    # => 6
        print "arr=", arr
        print "memo=", memo
        for i in range(len(arr)):
            # print "i", i, " arr[i]", arr[i]
            # print cb(memo, arr[i])
            memo = cb(memo, arr[i])
        return memo


    def find(self, arr, cb):
        # _.find(list, predicate) 
        # Looks through each value in the list, returning the first one that passes a truth test (predicate), or undefined if no value passes the test. The function returns as soon as it finds an acceptable element, and doesn't traverse the entire list.
        print "arr=", arr
        for i in range(len(arr)):
            if cb(arr[i]):
                found = arr[i]
                return found
        return 'undefined'


    def reject(self,arr, cb):
    # _.reject(list, predicate)
    # Returns the values in list without the elements that the truth test (predicate) passes. The opposite of filter.
        print "arr=", arr
        newarr = []
        for i in range(len(arr)):
            # print "i", i, " arr[i]", arr[i]
            # print "cb(arr[i])=", cb(arr[i])
            if not cb(arr[i]):
                newarr.append(arr[i])
        return newarr


    def filter(self,arr, cb):
        print "arr=", arr
        newarr = []
        for i in range(len(arr)):
            # print "i", i, " arr[i]", arr[i]
            # print "cb(arr[i])=", cb(arr[i])
            if cb(arr[i]):
                newarr.append(arr[i])
        return newarr


# you just created a library with 5 methods!
# let's create an instance of our class

_ = Underscore() # yes we are setting our instance to a variable that is an underscore

print '*'*10, "testing map", '*'*10
mapped = _.map([1, 2, 3], lambda num: num * 3)
print "mapped=", mapped
# _.map([1, 2, 3], function(num){ return num * 3; });
# => [3, 6, 9]

print '*'*10, "testing reduce", '*'*10
def reduce_function(memo, num):
     return memo + num
reduced = _.reduce([1, 2, 3, 4, 5], reduce_function, 5)
print "reduced=", reduced
#_.reduce([1, 2, 3, 4, 5], function(memo, num) { return memo + num; }, 5)
#=> 20
reduced = _.reduce([1, 2, 3], reduce_function, 0)
print "reduced=", reduced
# _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0)
# => 6

print '*'*10, "testing find", '*'*10
found = _.find([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)
print "found=", found
# _.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; })
# => 2
found = _.find([1, 3, 5], lambda num: num % 2 == 0)
print "found=", found
# _.find([1, 3, 5], function(num){ return num % 2 == 0; })
# => undefined

print '*'*10, "testing filter", '*'*10
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "evens=", evens
# should return [2, 4, 6] after you finish implementing the code above

print '*'*10, "testing reject", '*'*10
#  _.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
# => [1, 3, 5]
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "odds=", odds
