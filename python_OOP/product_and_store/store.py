# Optional Assignment: Store: Build a store to contain our products by making a store class and putting our products into an array.
# Store class:
# Attributes:
# * products: an array of products objects
# * location: store address
# * owner: store owner's name

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def displayInfo(self):
        print "Location:", self.location
        print "Owner:", self.owner
        self.inventory()
        return self

# Methods:
# add_product: add a product to the store's product list
    def addProduct(self, price, itemname, weight, brand):
        self.products.append(Product(price, itemname, weight, brand))
        return self

# remove_product: should remove a product according to the product name
    def removeProduct(self, obs_product_name):
        #find array element containing object to be removed

        len_prod = len(self.products)
        for i in range( len_prod ):
            indx = -1
            if self.products[i].itemname == obs_product_name:
                indx = i
                break
        # if indx >= 0, then object to be removed was found in self.products
        if indx >= 0:
            # object to be removed exists at self.products[indx], so move everything forward by one position, starting at indx
            for i in range(indx, len_prod-1):
                self.products[i] = self.products[i+1]    
            #now remove last position in products list
            self.products.pop()
        else:
            print "Cannot remove product. It does not exist in store"
        return self


# * inventory: print relevant information about each product in the store
    def inventory(self):
        print "Product Iventory:"
        for i in range( len(self.products) ):
            print " ---- Product " + str(i) + " ----"
            self.products[i].displayInfo()
        return self

class Product(object):
    def __init__(self, price, itemname, weight, brand):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    # Methods:
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        priceWithTax = self.price * (1+tax)
        return priceWithTax
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
    def displayInfo(self):
        print "Item Name: " + self.itemname
        print "Brand: " + self.brand
        print "Price: $" + str(self.price)
        print "Weight: " + str(self.weight) + "lbs"
        print "Status: " + self.status
        return self


# You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.

store1 = Store([], { "street":"100 Main St", "city":"Anycity", "state":"VA", "zipcode":54234 }, { "fname":"Charlie", "lname":"Parker"} )
store1.displayInfo()

# product1 = Product(1000, "Vase", 3.5, "Vivaldi")
# product2 = Product(3200, "Bike", 5.2, "Trek")
# product3 = Product(1500, "ArtFrame", 1.8, "Samsung")

# add product
print " ----- added a product ------"
store1.addProduct(1000, "Vase", 3.5, "Vivaldi")
store1.displayInfo()

# add product
print " ----- added a product ------"
store1.addProduct(3200, "Bike", 5.2, "Trek")
store1.displayInfo()

# add product
print " ----- added a product ------"
store1.addProduct(1500, "ArtFrame", 1.8, "Samsung")
store1.displayInfo()

# remove product
print " ----- removed a product ------"
store1.removeProduct("Vase")
store1.displayInfo()

store1.inventory()