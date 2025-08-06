# Task 1
# Create a function that returns all prime numbers in a range.
#  The function takes the beginning and end of the range as parameters.
#  Use the generator mechanism inside the function.
def primeNumber(start, end, checkFunction):
    current=start
    while current<=end:
        if checkFunction(current):
            print(current)
        current=current+1
def checkPrime(num):
    if num<2:
        return False
    i=2
    while i+i<=num:
     if num%i==0:
         return False
     i=i+1
     return True
primeNumber(2,20, checkPrime)


# Task 2
# Create a function that returns all Armstrong numbers in a range.
#  The function takes the beginning and the end of the range as parameters.
#  Use the generator mechanism inside the function.


# Armstrong numbers (or self-referential numbers) are natural numbers that are equal to the sum of their digits,
#  raised to a power equal to the number of digits of a number. 
# For example, the number 153 is Armstrong's number because

# 1^3 + 5^3 + 3^3 = 153.



# Another example: the number 370 is an Armstrong number because the sum of the cubes of its digits is equal to the number:

# 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370

# You can read more about Armstrong numbers here.

def armstrongNumber(start, end):
    for num in range(start, end + 1):
        numbers = str(num)
        power=len(numbers)
        total=sum(int(numbers)**power for numbers in numbers)
        if num==total:
            print(num)
armstrongNumber(1,1000)



# Task 3
# To solve this task, be sure to use the mechanism of higher order functions. 
# Create a function that finds the minimum or maximum in the list. 
# A user defines what to check for (minimum or maximum).

# The function's signature:

# def find_min_or_max(list_to_check, function_to_call) 

# list_to_check — a list to check.
# function_to_call — a function to check (function to check for minimum or function to check for maximum).
def find_max(lst):
    num = 0
    for i in lst:
        if i > num:
            num = i
    return num 

def find_min(lst):
    num = lst[0]   
    for i in lst:
        if i < num:
            num = i
    return num

def find_userchoice(lst):
    user_choice = input("which number you would like to find max or min :").lower()
    if user_choice == "max":
        return find_max(lst)
    elif user_choice == "min":
        return find_min(lst)
    else:
        return "please provide a valid input"

data = [2,4,3,5,88,6,0,1]
x = find_userchoice(data)
print(x)

# Task 4
# Create a pizza baking application.
# Each pizza has different components.
# Using the decorator mechanism, create different pizzas:

# Margarita;
# Four cheeses;
# Capricosa;
# Hawaiian.




    
    


