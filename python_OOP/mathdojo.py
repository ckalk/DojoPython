# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# PART I: 1) Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            self.result = self.result + num
        return self
    def subtract(self, *nums):
        for num in nums:
            self.result = self.result - num
        return self

# 2) Then create a new instance called md. It should be able to do the following task:
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.
md = MathDojo()
print "----- Part I -----"
print md.add(2).add(2,5).subtract(3,2).result

# PART II: Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. 
class MathDojo2(object):
    def __init__(self):
        self.result = 0
    def add(self, *items):
        for item in items:
            if type(item) == int:
                self.result+=item
            elif type(item) == list:
                for i in range(len(item)):
                    self.result+=item[i]
            else:
                print "item is wrong type"
        return self
    def subtract(self, *items):
        for item in items:
            if type(item) == int:
                self.result-=item
            elif type(item) == list:
                for i in range(len(item)):
                    self.result-=item[i]
            else:
                print "item is wrong type"
        return self

# It should now be able to perform the following tasks:
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
print "----- Part II -----"
md2 = MathDojo2()
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
print "check",0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3)


# PART III: Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons. 
class MathDojo3(object):
    def __init__(self):
        self.result = 0
    def add(self, *items):
        for item in items:
            if type(item) == int:
                self.result+=item
            elif type(item) == list:
                for i in range(len(item)):
                    self.result+=item[i]
            elif type(item) == tuple:
                for i in item:
                    self.result+=i
            else:
                print "item is wrong type"
        return self
    def subtract(self, *items):
        for item in items:
            if type(item) == int:
                self.result-=item
            elif type(item) == list:
                for i in range(len(item)):
                    self.result-=item[i]
            elif type(item) == tuple:
                for i in item:
                    self.result-=i
            else:
                print "item is wrong type"
        return self

# It should now be able to perform the following tasks:
# md.add((1,2,3), 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
print "----- Part III -----"
md3 = MathDojo3()
print md3.add((1,2,3), 3, 4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, (2,3,4), [1.1,2.3]).result
print "check", 1+2+3+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3+4)-(1.1+2.3)