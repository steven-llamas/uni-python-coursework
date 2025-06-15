instructor_1 = {
    "name": "blythe",
    "course": "csc24400",
    "age": 41,
}  # dictionary defined 3 pairs

print(instructor_1)  # print the dictionary, instructor_1
inst_age = instructor_1["age"]  # pull the value of age & assign to variable 'inst_age'
print(f"The instructor is {inst_age} years old. \n")
# prefix f or F inside print ( ) is a formatted string literal
# newly introduced concept from Python 3.6
# f-string is a string literal that may contain replacement fields
# replacement fields are expression delimited by curly braces { }
# other string literals have a constant value
# formatted strings (f-strings) are expressions evaluated at run-time by Python interpreter

instructor_1["age"] = 42  # updating instructor's age to 42

print(instructor_1)  # print the dictionary to see modified value
inst_age = instructor_1["age"]  # pull the value of age & assign to variable 'inst_age'
print(f"The instructor is now {inst_age} years old.")
