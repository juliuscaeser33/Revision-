import random
family_members={
"john":{
               "age":36,
                "gender":"male",
                  "date_of_birth":"1989",
                    "place_of_birth":"muranga"
                    },

"liz":{

 "age":25,
  "gender":"female",
   "date_of_birth":"1994",
    "place_of_birth":"kisumu"
    },
"kim":{

 "age":23,
  "gender":"male",
   "date_of_birth":"1996",
    "place_of_birth":"nairobi"}
}
for x in family_members.items():
    print(x)

#accessing the age/ place of birth or any other info needed of john in the dictonary
    print(family_members["john"]["place_of_birth"])
