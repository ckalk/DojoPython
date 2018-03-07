# Assignment: Animal: Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.
# Objective: understand inheritance--to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.

# Create Animal Class
# Attributes: name, health
# Methods: 1) walk: decreases health by one; 2) run: health decreases by five; 3) display health: print to the terminal the animal's health.
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print self.health
        return self

# * Create Dog Class: inherits everything from Animal
# Attributes: default health of 150
# Methods: 1) pet: increases health by 5
class Dog(Animal):
    def __init__(self, name, health):
        # use super to call the Animal __init__ method
        super(Dog, self).__init__(name, health) 
        #alternative way to initialize it
        # Animal.__init__(self, name, health)
        self.health = 150
    def pet(self):
        self.health+=5
        return self

# Create Dragon Class: inherits everything from Animal
# Attributes: default health of 170
# Methods: 1) fly: decreases health by 10; 2) display health: prints health by calling the parent method and prints "I am a Dragon"
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        print "I am a Dragon"
        super(Dragon, self).displayHealth()
        return self

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().

class Cat(Animal):
    def __init__(self, name, health):
        # use super to call the Animal __init__ method
        super(Cat, self).__init__(name, health) 


# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
tiger = Animal("tiger", 10)
tiger.displayHealth().walk().walk().walk().run().run().displayHealth()

# * Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
golden = Dog("golden", 99)
golden.displayHealth().walk().walk().walk().run().run().pet().displayHealth()

scary = Dragon("scary", 50)
scary.displayHealth().fly().fly().walk().run().run().displayHealth()

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. 
calico = Cat("calico",300)
# calico.fly()
# calico.pet()
# calico.displayHealth()
calico.displayHealth().walk().walk().walk().run().run().displayHealth()

# Also confirm that your Dog class can not fly().
# golden.displayHealth().fly().displayHealth()