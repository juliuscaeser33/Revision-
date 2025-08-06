# Task 1
# Create an app that stores information about great basketball players.
#  Store the player's full name and height. 
# Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.
 
basketball_players={
    "kim":{
    "full_name":"kim kim",
    "country":"kenya",
    "height":"190cm",    
},
"liz":{
    "full_name":"liz kyla",
    "height":"175cm",
    "country":"poland"
},
"mic":{
    "full_name":"mic jords",
    "height":"181cm",
    "country":"USA"
}
}
for name, data in basketball_players.items():
    print(f"{name}: {data}")
basketball_players["kay byran"] = {
    "full_name": "kay byran",
    "country": "USA",
    "height": "200cm"
}
print(basketball_players["kay byran"])

name_search=basketball_players.__class_getitem__("full_name ")
if name_search in basketball_players:
        print("basketball_players"[name])




# Task 2
# Create an app English-French Dictionary. 
# Store a word in English and its French translation.
#  Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.



# Task 3
# Create an app Company. Store the following information about a person: full name, phone number, corporate email, job title, room number, skype. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

# Task 4
# Create an app Book Collection. Store the following information about books: author, title, genre, year of release, publisher. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

