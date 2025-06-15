instructor_2 = {
    "name": "miller",
    "course": "csc45400",
    "office": "young317",
}  # dictionary defined with 2 pairs

print(instructor_2)

for key, value in instructor_2.items():  # items() return a list of KV pairs
    print(f"\nKey: {key}")  # for loop assigns each of these pairs to two variables
    print(f"Value: {value}")  # variables to print each key & associated value
