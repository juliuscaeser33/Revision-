eng_to_pol = {
    "hello": "cześć",
    "goodbye": "do widzenia",
    "please": "proszę",
    "thank you": "dziękuję",
    "yes": "tak",
    "no": "nie",
    "sorry": "przepraszam",
    "water": "woda",
    "food": "jedzenie",
    "friend": "przyjaciel"
}

user_input = "water"

def create_dict(key, value):
    eng_to_pol[key] = value
    return f"{key}, {value} has been added to dictionary"

def delete_dict(key, value):
    del eng_to_pol[key] 
    return f"{key}, {value} has been deleted to dictionary"


def search_dict(key):
    if key in eng_to_pol:
        return eng_to_pol[key]
    else:
        return f"{key } not found"


# x = create_dict("wife", "zona")
# print(x)
# y = delete_dict("hello", "cześć")
# print(y)
z = search_dict("yes")
print(z)

# print(eng_to_pol)
# for i in eng_to_pol:
#     if eng_to_pol[i] == user_input:
#         print(i)

# for j in eng_to_pol:
#     if j == user_input:
#         print(eng_to_pol[j])
