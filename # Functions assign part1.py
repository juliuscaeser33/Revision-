# Functions
# Part 1  

# Task 1
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
#  if you do so, you are insulting yourself."
#                                           Bill Gates
def my_function():  
  print("""Don't compare yourself with anyone in this world...\n if you do so, you are insulting yourself.\n" 
By Bill Gates""")
my_function()


# Task 2
# Write a function that takes two numbers as a parameter and displays all even numbers in between.
import random
def display_even_numbers():
    for num in range(2,10,):
        if num%2==0:
          print(num)
display_even_numbers()
  
# Task 3
# Write a function that prints an empty or solid square made out of some symbol. 
# The function takes the following as parameters: 
# the length of the side of the square, a symbol, and a boolean variable:

# def print_square(length, symbol, solid):
#     for row in range(length):
#         if solid or row == 0 or row == length - 1:
#             print(symbol * length)
#     print_square()




# if it is True, the square is solid;
# if False, the square is empty.

# Task 4
# Write a function that returns the smallest of five numbers. Numbers are passed as parameters.
def smallest_number(a,b,c,d,e):
    return min(a,b,c,d,e)
smallest_number(20,15, 30, 5, 10)
print(smallest_number(20,15, 30, 5, 10))

   

# Task 5
# Write a function that returns the product of numbers in a specified range. 
# The start and end points of the range are passed as parameters. 
# If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them.
def product_range(start,end):
    if start>end:
        start,end=end,start
    product=1
    for num in range(start,end+1):
        product*=num
    return product
result = product_range(2,5)
print(result)


# Task 6
# Write a function that counts how many digits a number has. 
# The number is passed as a parameter. 
# Return the received number of digits from the function. 
# For example, if the passed number is 3456, it has 4 digits.
# def count_digits(n):
#    if n==0:
#       return 1
#    count=0
#    while n>0:
#       n//=5
#       count+=1
#    



# Task 7
# Write a function that checks if a number is a palindrome. 
# The number is passed as a parameter. 
# If the number is a palindrome, return true, otherwise false.

def check_palindrome(number):
   if str(number) == str(number)[::-1]:
      return True
   else:
      return False
print(check_palindrome(121))
print(check_palindrome("level"))
print(check_palindrome(123))
print(check_palindrome(12321))
print(check_palindrome("madam"))


# A palindrome is a number which reads the same backward as forward. For instance, 123321 is a palindrome, 546645 is a palindrome, but 421987 is not.