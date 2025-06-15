instructor_2 = {
    "name": "miller",
    "course": "csc45400",
}  # dictionary defined with 2 pairs

print(instructor_2)
# print (instructor_2['age'])    # error we get here is KeyError

# get() method requires two arguments (key, optional_argument)
# optional_argument to pass the value if key doesn't exist
# if key doesn't exist and NO second argument in get(), it will return None!
age_value = instructor_2.get(
    "age", "No age value assigned"
)  # message instead of an KeyError
print(age_value)  # if key exits, we will get the corresponding value

age_value = instructor_2.get("age")  # return None
print(age_value)  # if key exits, we will get the corresponding value
