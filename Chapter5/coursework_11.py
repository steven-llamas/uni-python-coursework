favorite_cars = {  # press enter after {
    "mackenzie": "toyota",  # indent next line one level (4 spaces)
    "danian": "tesla",  # write K-V pair followed by comma
    "taya": "hyundai",  # your text editor should automatically indent
    "gabriel": "audi",  # good to include comma after last KV pair
}  # closing braces on a new line

print(favorite_cars)  # print the dictionary
print("\n")

# sorted ( ) method is one way to sort the keys as they are returned
# wrap sorted ( ) around keys ( ) which sort the list before looping

for name in sorted(favorite_cars.keys()):  # loop the favorite_cars dictionary
    # print the name of everyone in titlecase with thank you message
    print(f"{name.title()}, thank you for listing your favorite car.")
