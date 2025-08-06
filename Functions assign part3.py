# Functions
# Part 3


# Task 1
# Write a recursive function for finding the greatest common divisor of two integers.
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("the gcd of",a,"and",b,"is",gcd(a,b)) 
gcd(a,b)




# Task 2
# Develop a game of Bulls and Cows. 
# The program chooses a four-digit number, and the player has to guess it.
#  After the user enters a number, the program reports how many digits of the number are guessed (bulls),
#  and how many digits are guessed and stand in the right place (cows).
#  After guessing the number, print the number of user's attempts.
#  Use recursion in your game.
# import random
# def numbers():





# Task 3
# There are an 8×8 chessboard and a knight. 
# The program should request the coordinates of the square from the user and put the knight there. 
# The program's objective is to find the knight's path that allows it to go through the entire chessboard while stepping on each square only once. 
# (Since the process of finding a path for initial squares can take a long time,
#  we recommend you to begin with a 6×6 chessboard). Use recursion in your game.

# Task 4
# Develop a game of 15 Puzzle.