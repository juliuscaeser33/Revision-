# def greating_user():
#     "display a simple greating"
#     print("hello")
# greating_user()

# def my_pet(animal_type,pet_name):
#     print(f"\n I have an {animal_type.title()}.")
#     print(f"\n my {animal_type.title()}'s name is {pet_name.title()}.")
# my_pet("dog", "jerry")

# def make_shirt(size, message):
#     print(f"\n I have a {size} size shirt")
#     print(f"\n It is {message.title()} in color")
# make_shirt(46, 'blue')

def get_fomatted_name(first_name, last_name):
    full_name = (f"{first_name} {last_name}")
    return full_name.title()
developer = get_fomatted_name('julius', 'mwangi')
print(developer)