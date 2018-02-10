''' Assignment: Scores and Grades -- Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
    Score: 60 - 69; Grade - D
    Score: 70 - 79; Grade - C
    Score: 80 - 89; Grade - B
    Score: 90 - 100; Grade - A
The result should be like this:
Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
...
Score: 72; Your grade is C
End of the program. Bye!
Hint: Use the python random module to generate a random number
import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint() '''

# for loop to generate 10 scores and get grade by calling function grade(score)

def grade(score):
    letter = "F"
    if (score >= 90):
        letter = "A"
    elif (score >= 80):
        letter = "B"
    elif (score >= 70):
        letter = "C"
    elif (score >= 60):
        letter = "D"
    return letter

import random
for i in range(10):
    random_num = random.randrange(100)
    gr = grade(random_num )
    print "Score: ", random_num, " ; Your grade is", gr
print "End of the program. Bye!"


