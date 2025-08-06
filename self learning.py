
# #show the higher order function example
# studBirthYear = [2000, 1997, 2002, 1999, 2007]
# studAges = list(map(lambda x:2022-x, studBirthYear))
# print(studAges) # [22, 25, 20, 23, 15]

# #without hof
# studBirthYear = [2000, 1997, 2002, 1999, 2007]
# studAges = []
# for year in studBirthYear:
#     studAges.append(2025-year)
# print(studAges) #[22, 25, 20, 23, 15]

#example where abs function return input with positive number
userNumber=int(input("Enter a number: "))
print(abs(userNumber))

myNumbers = [1.3, -2.3, -12, 11, 0.45]
print(myNumbers)
print(sorted(myNumbers, key = abs))