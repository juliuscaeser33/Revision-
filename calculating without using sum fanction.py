#write a function that calculates the sum of the elements from a list of integers. 
# The list is passed as a parameter. 
# The result is returned from the function. 
# data=[1,2,3,4,5,6,7]
# def sum(x):
#     total=0
#     for i in x:
#         total+=i
#     return total
# print(sum(data))

#write a function that calculates the max of the elements from a list of integers. 
# The list is passed as a parameter. 
# The result is returned from the function. 
data=[1,2,3,4,5,6,7]
def a (x):
    a=x[0]
    for i in x:
        if i>a:
            a=i
    return a
print(a(data))





 