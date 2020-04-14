"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import string

a = int(input('Enter minimum string length: '))
b = int(input('Enter maximum string length: '))
len_string = random.choice(range(a,b))
n = int(input('How many random strings to generate? '))

def random_string(n):
    count = 0
    while count != n:
        let_digit = string.ascii_letters + string.digits
        print(''.join(random.choice(let_digit) for i in range(len_string)))
        count += 1

print("Random string:",random_string(c))