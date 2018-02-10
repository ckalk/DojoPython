''' Assignment: Making Dictionaries -- Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.
Your first function will take in two lists containing some strings. Here are two example lists:
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
Here's some help starting your function.
def make_dict(list1, list2):
  new_dict = {}
  # your code here
  return new_dict
'''

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    n = len(list1) # and can assume n = len(list2) also
    for i in range( n ):
        new_dict[list1[i]] = list2[i]
    return new_dict

print make_dict(name, favorite_animal)

#Hacker Challenge: If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values. 
print "\n", "------- Hacker Challenge --------"
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Charlie", "Theodore"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas","elephant","zebra","whale"]

def make_dict2(list1, list2):
    new_dict = {}
    n2 = max(len(list1), len(list2))
    n1 = min(len(list1), len(list2))
    # print " min & max list length:", n1, n2
    for i in range( n1 ):
        if(len(list1)>=len(list2)):
            new_dict[list1[i]] = list2[i]
            for j in range(n1, n2):
                new_dict[list1[j]] = ''
        else:
            new_dict[list2[i]] = list1[i] 
            for j in range(n1, n2):
                new_dict[list2[j]] = ''           
    return new_dict

print "\n Case with name list longer"
print make_dict2(name2, favorite_animal)
print "\n Case with favorite_animal list longer"
print make_dict2(name, favorite_animal2)