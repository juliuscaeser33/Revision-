#  #Task 1
# # Create an app that stores information about great basketball players.
# #  Store the player's full name and height. 
# # Provide the possibility to add, delete, search, and replace data.
# #  Use a dictionary to store information.

playerS={}
playerS={
    "kim kim":{
    "Height":170,
    "country": "kenya",
    "DOB":1980,
    "score":100,
},
    "liz liz":{
    "Height":178,
    "country":"kenya",
    "DOB":1990,
    "score":105,
},

    "jordan spark":{
    "Height":179,
    "country":"USA",
    "DOB":1985,
    "score":110
    }
}
"""Storing players information """   
for key, value in playerS.items():
 print(f"{key} : {value}")
 
"""adding new player to the dictionary updated list of players"""
for new_player in key,value:
  playerS["sam cook"]={
    "Height":190,
    "country":"poland",
    "DOB":1986,
    "score":96
  }

print(f"{playerS}updated list of players")

"""deleting player from the dictionary updated list of players"""
def deleting_player(key):
    if key in playerS:
        del playerS[key]
        return f" key : {key} has been deleted"
    
del playerS["kim kim"]
print(f"{playerS}updated list1 of players kim kim deleted")

# # """"help on this part of search"""
# # # search_player= input("Enter the player name:")

# # # for key,value in playerS[search_player]:
# # #      if search_player in playerS:
# # #       print(key,value)
     
# # # else:
# # #         f"{search_player} not found"



# # #Task 3
# # # Create an app Company. 
# # # Store the following information about a person: 
# # # full name, phone number, corporate email, job title, room number, skype. 
# # # Provide the possibility to add, delete, search, and replace data.
# # #  Use a dictionary to store information.

my_app={}

my_app={"name":"julius chomba",
             "Tel":487890000,
             "email":"juliusmwangi44@gmail.com",
             "desgination": "developer",
             "office number": 306,
             "skype": "juliusmwangi44"}
for key, value in my_app.items():
    print(f"{key},{value}")

""""adding information"""

def add_info(key,value):
    my_app[key]=value
add_info("rank","junior developer")
for key, value in my_app.items():
    print(f"{key},{value}")

"""deleting some information"""
def deleting_info(key):
 if key in my_app:
  del my_app[key]
  print(f"{key} has been deleted")
 else:
        print(f" {key} not found")
deleting_info("skype")
for key, value in my_app.items():
 print(f"{key},{value}")

""""searching infor"""
def search_infor(key):
   if key in my_app:
      print(f"{key}:{my_app[key]}")
   else:
      print(f"{key} not found")

search_infor("facebook")
"""replacing infor"""
def replace_infor(key, new_infor):
   if key in my_app:
      old_infor=my_app[key]
      my_app[key]=new_infor
      print("{key}updated")
   else:
      print("cannot be updated")

replace_infor("email", "juliuscaeser33@gmail.com")
for key, value in my_app.items():
    print(f"{key},{value}")

# # Task 4
# Create an app Book Collection. 
# Store the following information about books: 
# author, title, genre, year of release, publisher. 
# Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.

ebook_app={}
ebook_app=[
    {
   "Title":"A profound Mind",
    "Author":"The Dalai Lama",
    "genre": "spiritual/motivational",
    "year":2011,
    "publisher":"Harmony Books"
},
{
    "Title":"The Hunger Games",
    "Author":"Suzanne Collins",
    "genre":"fixion",
    "year":2008,
    "publisher":"Scholastic"
}
]
for books in ebook_app:
    for key, value in books.items():
     print(f"{key} : {value}")
  
"""ADD NEW BOOK"""
def adding_book(key, value):
   ebook_app.append(new_book) 
print(f"new book has been added")
new_book={"title":"Diary by St faustina",
            "Author":"Faustina Kowalska",
            "genre": "inspirational",
            "year":1979,
            "publisher":"Nihil Obstat"}

for key, value in new_book.items():
    print(f"{key} : {value}")

""""deleting book"""
def deleting_book(key):
    if key in ebook_app:
        del ebook_app[key]
        print(f"{key} has been deleted")
    else:
        print(f"{key} not found")
deleting_book("title")
for key, value in books.items():
    print(f"{key} : {value}")
