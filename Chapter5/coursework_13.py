instructor_1 = {
    "name": "david",
    "course": "csc24400",
}  # dictionary 1 with 2 KV pairs
instructor_2 = {
    "name": "smith",
    "course": "csc45400",
}  # dictionary 2 with 2 KV pairs
instructor_3 = {
    "name": "mark",
    "course": "csc46400",
}  # dictionary 3 with 2 KV pairs

print(instructor_1)  # print first dictionary
print(instructor_2)  # print second dictionary
print(instructor_3)  # print third dictionary

print("\n")  # print new line after printing three dictionary
instructors = [instructor_1, instructor_2, instructor_3]  # three dictionaries in a list

for instructor in instructors:  # loop through the instructors list
    print(instructor)  # print each item via instructor variable
