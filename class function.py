# def my_function():
#     print("function class 101")# to print you must return the data function   
# my_function() # calling or returning the function


# def my_function(University):
#     print(University+"nairobi campus")
# my_function("Kemu ")
# my_function("UON ")
# my_function("MKU ")


# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# def my_function(religion ="christian"):
#     print("i am a "+ religion)
# my_function("christian")
# my_function("muslim")
# my_function("jew")
# my_function()

# def my_function(religion="christian"):  # Fixed the default argument syntax
#      print("I am a " + religion)

# my_function("christian")  # Prints: I am a christian
# my_function("muslim")     # Prints: I am a muslim
# my_function("jew")        # Prints: I am a jew
# my_function()             # Uses default, prints: I am a christian...#function call

#Python Function With Arbitrary Arguments
# program to find sum of multiple numbers 

# def find_sum(*numbers): #find_sum function being define
#     result = 0
    
#     for num in numbers:
#         result = result + num
    
#     print("Sum = ", result)

# #function call with 3 arguments
# find_sum(1, 2, 3)

# # function call with 2 arguments
# find_sum(4, 9)

message ="hello"
def greetings():
    print("local",message)

print("global", message)
greetings()