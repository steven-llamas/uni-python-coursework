

squares = ['1', '4', '9', '16', '25']       # squares list with 5 items
for square in squares:
print(square)           # ERROR 1: Forgetting to indent, IndentationError
    
for square in squares:
    print(square)
print(square + ", is a square value")  # ERROR 2: Forgetting to indent additional lines, Logical error

message = "Hello class CSC-10011 !"
    print(message)      # ERROR 3: Indenting unnecessarily, IndentationError
    
for square in squares:
    print(square)
    print(square + ", is a square value")  
    print("Thank you everyone")    # ERROR 4: Indenting unnecessarily after the loop, Logical error
    
cars = ['toyota', 'tesla', 'hyundai', 'audi', 'porsche']
for car in cars         # ERROR 5: Forgetting the colon, Syntax error
    print(cars)     