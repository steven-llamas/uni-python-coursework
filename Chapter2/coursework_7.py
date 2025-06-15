cars = ["toyota", "tesla", "hyundai", "audi", "porsche"]
print("\n CARS LIST OF 5 CARS WE INITIALLY HAVE")
print(cars)

fruits = ["apple", "mango", "banana", "grapes", "peach"]
print(" FRUITS LIST OF 5 FRUITS WE INITIALLY HAVE")
print(fruits)

squares = ["1", "4", "9", "16", "25"]
print(" SQUARES LIST OF 5 SQUARES WE INITIALLY HAVE")
print(squares)

print("\n REVERSING ALL THREE LISTS, WITH THEIR LENGTH: ")
# reverse() method doesn't sort backward alphabetically
# it only reverses the list order
cars.reverse()
print(cars)
print(len(cars))

fruits.reverse()
print(fruits)
print(len(fruits))

squares.reverse()
print(squares)
print(len(squares))
