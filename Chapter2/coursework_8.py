schools = ["lindenwood", "fontbonne", "maryville"]  # List with 3 items
my_list = []  # An empty list
a = "nice"

print("\n SCHOOLS LIST THAT WE INITIALLY HAVE")
print(schools)

print("\n MY LIST THAT WE INITIALLY HAVE (Empty List) ")
print(my_list)

# print(schools[3])   # Trying to print the fourth item from schools, hence IndexError
# print(my_list[-1])  # Trying to print the last item from my_list, hence IndexError

print("\n Length of both lists are: ")
print(len(schools))
print(len(my_list))

print("\n The last item of schools list is: ")
print(schools[-1])  # Printing last item of the schools list

my_list = ["my", a, "10", "3.14", [7, 8, 9]]  # Redefining my_list with 5 values
print("\n UPDATED MY LIST ")
print(my_list)  # Printing my_list after redefining

print("\n Length of my_list is: ")
print(len(my_list))  # Printing length of my_list

print("\n The last item of my_list is another list: ")
print(my_list[-1])  # Printing last item from my_list
