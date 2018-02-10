dog = ("Canis Familiaris", "dog", "carnivore", 12)
print dog[2]
for data in dog:
     print data

# dog[0] = "X"

dog = dog + ("domestic",)
print dog

dog = dog[:3] + ("man's best friend",) + dog[4:]
print dog

capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data