dimensions = (800, 600)  # tuple dimensions, say rectangle of certain size
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 850     #TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:  # looping in a tuple
    print(dimension)

# Writing over a tuple
dimensions = (800, 600)
print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (1920, 1080)  # store a new tuple in the variables dimensions
print("\nNew dimensions: ")  # overwriting a variable is valid in Python
for dimension in dimensions:
    print(dimension)
