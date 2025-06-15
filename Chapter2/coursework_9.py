num = 10  # num variable with value 10
print(num)
num.remove(10)
# AttributeError 1
# Because no such method append () supported for integer data type num

# Avoiding AttributeError 1
num = [10]  # now num as a list with one list item as 10
print("Values of num list are: ")
print(num)

num.remove(10)  # now remove function is supported here, because of list type
print(num)  # prints a emplty list

myFavString = "AJourneyOfThousandMilesBeginsWithASingleStep"
print(myFavString)

print(len(myFavString))

print(myFavString.lower())  # prints our string in lower case
print(myFavString.upper())  # prints our string in UPPER CASE
print(myFavString.title())  # prints our string in Title Case

print(myFavString.lowe())
# AttributeError 2
# Because we mispell lower () function as lowe () function
