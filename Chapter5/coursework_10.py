favorite_cars = {  # press enter after {
    "mackenzie": "toyota",  # indent next line one level (4 spaces)
    "danian": "tesla",  # write K-V pair followed by comma
    "taya": "hyundai",  # your text editor should automatically indent
    "gabriel": "audi",  # good to include comma after last KV pair
}  # closing braces on a new line

print(favorite_cars)  # print the dictionary
print("\n")

# keys() method when we DON'T need to work with all values
# looping via key is the default behavior in Python Dictionary

for name in favorite_cars:  # same as for name in favorite_cars.keys()
    # for name in favorite_cars.keys():     # loop the favorite_cars dictionary
    print(name.title())  # print the name of everyone in titlecase
