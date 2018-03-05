# Assignment: Bike: 
# 6) Questions: What would you do to prevent the instance from having negative miles? Add a check to reverse() after computing self.miles: if self.miles < 0 then self.miles=0
# Which methods can return self in order to allow chaining methods? Answer: displayInfo(), ride(), and reverse()

# 1)Create a new class called Bike with the following properties/attributes:
#     price
#     max_speed
#     miles
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    # 4)Add the following functions to this class:
    # displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "bike's price is: $"+str(self.price), "bike's max speed is: "+str(self.max_speed)+"mph", "bike's total miles is:"+str(self.miles)      
        return self
    # ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10    
        return self
    # reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5
    def reverse(self):
        print "Reversing"
        self.miles = self.miles -5    
        return self

# 2)Create 3 instances of the Bike class.
# 3)Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
bike1 = Bike(100, 15)
bike2 = Bike(500, 15)
bike3 = Bike(2500, 45)

# 5)Have the first instance ride three times, reverse once and have it displayInfo(). 
print "------ bike1-------"
bike1.ride().ride().ride().reverse().displayInfo()
#Have the second instance ride twice, reverse twice and have it displayInfo(). 
print "------ bike2-------"
bike2.ride().ride().reverse().reverse().displayInfo()
#Have the third instance reverse three times and displayInfo().
print "------ bike3-------"
bike3.reverse().reverse().reverse().displayInfo()
# Test code



