USER_DICT = {}

def create_dict(key, value):
    data = USER_DICT[key] = value
    return data

def search_data(key):
    if key in USER_DICT:
        return USER_DICT[key]
    else:
        return f"key : {key} not found"

def replacing_value(key, replacing_value):
    if key in USER_DICT:
        data =USER_DICT[key] = replacing_value
        return data
    else:
        return f"key : {key} not found"
    
def deleting_value(key):
    if key in USER_DICT:
        del USER_DICT[key]
        return f" key : {key} has been deleted"
    else:
        return f"{key} not found"
    

create_dict("pushkar", 35)
print(USER_DICT)

print(deleting_value("pushkar"))

# print(search_data("xyz"))
# print(replacing_value("abc", 40))
# print(USER_DICT)


