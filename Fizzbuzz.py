# Exercise 1 - Fizzbuzz

# Write a program that outputs sequentially the integers from 1 to 100, but on some conditions prints a string instead:
# when the integer is a multiple of 3 print “Fizz” instead of the number,
# when it is a multiple of 5 print “Buzz” instead of the number,
# when it is a multiple of both 3 and 5 print “FizzBuzz” instead of the number.

# Notes: must be in a class and method format

# Let's create the Fizzbuzz class
class Fizzbuzz:

    def __init__(self):
        self.three = 3 # Integer to check if is a multiple of 3
        self.five = 5 # Integer to check if is a multiple of 5

# Function that will check if the number is multiple of 3 or 5 and print the correct answer
    def fizzbuzz_prints(self):
        i = 1
        while i <= 100: # loop while from 1 to 100
            if i % self.three == 0 and i % self.five == 0: # check if is multiple of both
                print("FizzBuzz")
            elif i % self.three == 0: # check if is multiple of 3
                print("Fizz")
            elif i % self.five == 0: # check if is multiple of 5
                print("Buzz")
            else:
                print(i) # number that is not dividable by 3 or 5

            i += 1

# Let's create an object of the Fizzbuzz Class
object_fizzbuzz = Fizzbuzz()

# Call the function that will print the corrects answers
object_fizzbuzz.fizzbuzz_prints()
