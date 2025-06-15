favorite_cars = {  # press enter after {
    "mackenzie": "toyota",  # indent next line one level (4 spaces)
    "danian": "tesla",  # write K-V pair followed by comma
    "taya": "hyundai",  # your text editor should automatically indent
    "gabriel": "audi",  # good to include comma after last KV pair
}  # closing braces on a new line

print(favorite_cars)  # print the dictionary

danian_car = favorite_cars[
    "danian"
].title()  # fetch the value of danian & assign to variable 'danian_car'
print(
    f"\nDanian's favorite car is {danian_car}."
)  # print the dictionary to see removed pair

# prefix f or F inside print ( ) is a formatted string literal
# newly introduced concept from Python 3.6
# f-string is a string literal that may contain replacement fields
# replacement fields are expression delimited by curly braces { }
# other string literals have a constant value
# formatted strings (f-strings) are expressions evaluated at run-time by Python interpreter
