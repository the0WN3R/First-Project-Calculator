# Create the function to divide
def divide():
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    z = round(x / y, 2)
    print("The quotient is ", z)

# Create the function to square
def square():
    a = int(input("What's the first number? "))
    print("The squared answer is ", a * a)

# Create the function to add
def add():
    b = float(input("What is the first number? "))
    c = float(input("What is the second number? "))
    d = round(b + c, 2)
    print("The sum is ", d)

# Create the function to subtract
def subtract():
    e = float(input("What is the first number? "))
    f = float(input("What is the second number? "))
    g = round(e - f, 2)
    print("The difference is ", g)

# Create the function to multiply
def multiply():
    h = float(input("What is the first number? "))
    i = float(input("What is the second number? "))
    j = round(h * i, 2)
    print("The product is ", j)

# Determine which function the user would like to use
k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, and 5 is square. "))

# Add if the user chooses
if k==1:
    print("You are about to add.")
    add()

# Subtract if the user chooses
if k==2:
    print("You are about to subtract.")
    subtract()

# Multiply if the user chooses
if k==3:
    print("You are about to multiply.")
    multiply()

# Divide if the user chooses
if k==4:
    print("You are about to divide.")
    divide()

# Square if the user chooses
if k==5:
    print("You are about to square.")
    square()