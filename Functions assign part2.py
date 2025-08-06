# Functions
# Part 2
# Task 1
# Write a function that calculates the product of the elements from a list of integers. 
# The list is passed as a parameter. The result is returned from the function.
# Function to double a number
def double_number(x):
    return x * 2

a = [1, 2, 3, 4]

b = []
for num in a:
    b.append(double_number(num))

print(b)

# Task 2
# Write a function to find the minimum in a list of integers. The list is passed as a parameter. 
# The result is returned from the function.
a = [5,8,25,10,3,15]
smallest = min(a)
print(smallest)

# Task 3
# Write a function that determines how many prime numbers there are in the list of integers. 
# The list is passed as a parameter. The result is returned from the function.
import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)
# Task 4
# Write a function that removes a given number from the list of integers. 
# Return the number of removed elements from the function.

#def remove_number(input_list, no_delete):

 


# Task 5
# Write a function that takes two lists as a parameter and returns a list containing the elements of both lists.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

union_list = list(set(a).union(b))

print("Union lists:", union_list)

# Task 6
# Write a function that calculates the power of each element from the list of integers.
#  A value for the power is passed as a parameter, the list is also passed as a parameter.
#  The function returns a new list containing the results.
# Python3 code to recursively find
# the power of a number



    # If power is 0 then return 1
    # if condition is true
    # only then it will enter it,
    # otherwise not
# Recursive function to find N^P.
def power(N, P):

    if P == 0:
        return 1

    return (N*power(N, P-1))

if __name__ == '__main__':
    N = 5
    P = 2

    print(power(N, P))