favorite_cars = {  # press enter after {
    "mackenzie": "toyota",  # indent next line one level (4 spaces)
    "danian": "tesla",  # write K-V pair followed by comma
    "taya": "hyundai",  # your text editor should automatically indent
    "gabriel": "audi",  # good to include comma after last KV pair
}  # closing braces on a new line

print(favorite_cars)  # print the dictionary
print("\n")

# values ( ) method to return list of values (without any keys)
for car in favorite_cars.values():  # loop the favorite_cars dictionary
    print(car.title())  # print the values in titlecase
