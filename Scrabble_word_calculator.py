# Exercise 1 - Scrabble word calculator

# Write a program that outputs given the below scoring create a Scrabble word calculator that will provide
# the correct scores dependent on the string provided.

# Letter -> Value
# A, E, I, O, U, L, N, R, S, T -> 1
# D, G -> 2
# B, C, M, P -> 3
# F, H, V, W, Y -> 4
# K -> 5
# J, X -> 8
# Q, Z -> 10

class Scrabble_calculator:

    def __init__(self):
        self.letter_value = { # Dictionary that will save the letter and their respective values
            "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N":1, "R":1, "S": 1, "T": 1,
            "D": 2, "G": 2,
            "B": 3, "C": 3, "M": 3, "P": 3,
            "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
            "K": 5,
            "J": 8, "X": 8,
            "Q": 10, "Z": 10
        }

    # Function that will provide the correct score
    # We pass one parameter that is the word provided
    def calculate_score(self, word):
        score = 0 # variable to save the score
        upper = word.upper() # Format the word to process correctly with the dictionary

        for letter in upper: # For loop to iterate the word and add the score for each letter
            score += self.letter_value[letter]

        return score # return the final score

word = input("Please enter the word that you would like to get the score (NOT DIGITS): ")
print("Processing...")

# Let's create an object of the Scrabble_calculator Class
object_scrabble = Scrabble_calculator()

# Call the function that will get the score
result = object_scrabble.calculate_score(word)

print(f"The value of the word {word} is: {result} points!")
