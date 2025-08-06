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