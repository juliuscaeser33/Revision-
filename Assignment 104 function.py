# task1
# create a function that will find min number from list
# 1. use recursion 
# def minimum_number(x):
#     if len(x) == 1:
#         return x[0]
#         if x[0] < x[1]:
#             return x[0]
        
#     else:
#         return min(x[0], minimum_number(x[1:]))
# x=[-1,3,7,0,8]
# minimum_number(x)
# print("The minimum number is:", minimum_number(x))   



# task 2.
# create a pizza order app using function
# 1. put parameters such as small large extra-large pizza for 10, 15 and 20$
# 2. ask user for extra pepproni 2$ 
# 3. ask user for extra cheese 1$
# 4. add 10% tip as well in the end

def pizza_order():
    pizza_size = input("Enter the size of pizza:")

    if pizza_size == "small":
        pizza_price=10
    elif pizza_size == "large":
        pizza_price=15
    elif pizza_size == "extra_large":
        pizza_price=20
    else:
        return 0
    pepproni=input("do you want extra pepproni:")
    price=2 #local variable price for peperoni 
    if pepproni =="yes":
       price+=2
    cheese=input("do you want extra cheese:")
    price=1 #local variable price for cheese
    if cheese == "yes":
        price+=1
   
    tip=0.1*(pizza_price+price)
    global total_price #global variable
    total_price=pizza_price +tip+price
pizza_order()
print("the total price is",{total_price})
      