for number in range(1, 10):
    print(number)  # printing numbers from 1 to 9

for number in range(1, 11):
    print(number)  # printing numbers from 1 to 10

numbers = list(range(1, 11))
print(numbers)  # convert range() directly into a list

even_numbers = list(range(2, 11, 2))
print(even_numbers)  # print even numbers between 1 to 10

# print a list of first 10 square numbers
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)  # squares.append(value**2)
print(squares)

# Statistics with a list of numbers, minimum, maximum, and sum of a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# list comprehension to generate same list
squares = [value**2 for value in range(1, 11)]
print(squares)
