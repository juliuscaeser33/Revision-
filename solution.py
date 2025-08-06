# solutions for tasks 4.1 functions


# 1. Write a function that prints formatted text given below:
# "Don't let the noise of others' opinions 
# drown out your own inner voice."
#                               Steve Jobs
# solution

def quote():
    print("""Don't let the noise of others' opinions 
drown out your own inner voice."
                               Steve Jobs""")    
quote()

# 2. Write a function that takes two numbers as a parameter and displays all odd numbers in between.
# solution
def odd_number(num1, num2):
    for i in range(num1, num2 +1):
        if i % 2 != 0:
            print(i)
odd_number(2, 20)

# 3.Write a function that prints a horizontal or vertical line made out of some symbol. The function takes the following as a parameter: the line's length, direction, symbol
def line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    else:
        for i in range(length):
            print(symbol)

line(10, "horizontal", "@")

# 4. Write a function that returns the greatest of four numbers. Numbers are passed as parameters.
# method 1
def greateest_num(a,b,c,d):
    return max(a,b,c,d)
x = greateest_num(2,34,23,12)
print(x)

# method 2
def great_num(a,b,c,d):
    great = a
    if b > great:
        great = b
    if c > great:
        great = c
    if d > great:
        great = d
    return great

x = great_num(1,40, 12, 38)
print(x)

# 5. Write a function that returns the sum of numbers in a specified range. The start and end points of the range are passed as parameters.
# solution

def sum_of_num(x,y):
    total = 0
    for i in range(x, y+1):
        total += i
    return total
z =sum_of_num(2, 10)
print(z)

# 6. Write a function that checks if a number is prime. The number is passed as a parameter. If the number is prime, return true, otherwise false.
# solution

def is_prime(n):
# assuming user provides positive integer
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

x = is_prime(15)
print(x)

# 7. Write a function that checks if a six-digit number is lucky. The number is passed as a parameter. If the number is lucky, return true, otherwise false.
# solution

user_input = input("please provide si digit number : ")
def lucky_num(user_input):
    if len(user_input) < 6:
        return "please provide 6 digit number"
    first_section = int(user_input[0]) + int(user_input[1]) + int(user_input[2])
    second_section = int(user_input[-1]) + int(user_input[-2]) + int(user_input[-3])
    return first_section == second_section

x = lucky_num(user_input)
print(x)