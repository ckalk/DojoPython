# Assignment: Product: The owner of a store wants a program to track products. 
# Create a Product class to fill the following requirements.
# Attributes
# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
class Product(object):
    def __init__(self, price, itemname, weight, brand):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    # Methods:
    # Every method that doesn't have to return something should return self so methods can be chained.
    
    # Sell: changes status to "sold"
    def sell(self):
        self.status = "sold"
        return self
    
    # Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def addTax(self, tax):
        priceWithTax = self.price * (1+tax)
        return priceWithTax

    # Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
    def returned(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "box opened":
            self.status = "used"
            self.price = self.price * 0.8
        else:
            print "Unknown reason code"
        return self

    # Display Info: show all product details.
    def displayInfo(self):
        print "Item Name: " + self.itemname
        print "Brand: " + self.brand
        print "Price: $" + str(self.price)
        print "Weight: " + str(self.weight) + "lbs"
        print "Status: " + self.status
        return self

print "\n------ product1-------"
product1 = Product(1000, "Vase", 3.5, "Vivaldi")
product1.displayInfo()
tax = .1
print "Price with Tax(" + str(tax) + "): $" + str(product1.addTax(tax))

reason = "box opened"
print "------ product1 is returned bc " + reason + "-------"
product1 = Product(700, "Vase", 3.5, "Vivaldi")
product1.returned(reason).displayInfo()
print "Price with Tax(" + str(tax) + "): $" + str(product1.addTax(tax))

print "\n------ product2-------"
product2 = Product(3200, "Bike", 5.2, "Trek")
product2.displayInfo()
tax = .15
print "Price with Tax(" + str(tax) + "): $" + str(product2.addTax(tax))

reason = "defective"
print "------ product2 is returned bc " + reason + "-------"
product2.returned(reason).displayInfo()
print "Price with Tax(" + str(tax) + "): $" + str(product2.addTax(tax))

print "\n------ product3-------"
product3 = Product(1500, "ArtFrame", 1.8, "Samsung")
product3.displayInfo()
tax = .12
print "Price with Tax(" + str(tax) + "): $" + str(product3.addTax(tax))
reason = "in box"
print "------ product3 is returned bc " + reason + "-------"
product3.returned(reason).displayInfo()
print "Price with Tax(" + str(tax) + "): $" + str(product3.addTax(tax))