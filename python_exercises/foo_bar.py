''' Optional Assignment: Foo and Bar -- Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".'''

# define function to check if a number is a prime number
def checkIfPrime(num):
    loopUntil = num/2
    isPrime = True
    for i in range(2, loopUntil+1):
        if( num % i  == 0):
            isPrime = False
    return isPrime

# define function to check if a number is a perfect square
def checkIfPerfectSqaure(num):
    isPerfectSq = False
    i = 1
    while i*i <= num:
        if( (num - i*i)  == 0):
            isPerfectSq = True
        i+=1
    return isPerfectSq

# check that functions are doing the right thing
''' for i in range (1, 100):
    if (checkIfPrime(i)):
        print "i = ", i, "is a prime number"
    else:
        print "i = ", i, "is NOT a prime number"

for i in range (1, 100):
    if (checkIfPerfectSqaure(i)):
        print "i = ", i, "is a perfect square"
    else:
        print "i = ", i, "is NOT a perfect square" '''

# do what assignment asks (For all numbers between 100 and 100000: If prime number, print "Foo"; If perfect square, print "Bar"; if neither, print "FooBar".)
for i in range (100, 100000):
    print "\n ***Number being evaluated =", i
    if (checkIfPrime(i)):
        print "Foo"
        #don't need to check if (checkIfPerfectSqaure(i)) here, since only prime number that is also perfect square is number 1
    else: #now is not prime, check if perfect square
        if (checkIfPerfectSqaure(i)):
            print "Bar"
        else:
            print "Foobar"

    
        

