banned_fruits = [
    "kiwi",
    "strawberry",
    "watermelon",
]  # list containing three banned fruits
print("if Statements for testing multiple conditions: ")
if "kiwi" in banned_fruits:  # check whether the person requested kiwi
    print("\nRemoving kiwi ...")
    print("Kiwi is banned in the our canteen.")

if "banana" in banned_fruits:  # check whether the person requested banana
    print("\nRemoving banana ...")
    print("Banana is banned in the our canteen.")

if "watermelon" in banned_fruits:  # check whether the person requested watermelon
    print("\nRemoving watermelon ...")
    print("Watermelon is banned in the our canteen.")

print("\nFinished removing all banned fruits !")
