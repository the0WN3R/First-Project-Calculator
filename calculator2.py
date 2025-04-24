def ask():
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    return x, y

# Create the function to divide
def divide():
    x, y = ask()
    print("The quotient is ", x/y)

# Create the function to square
def square():
    a = float(input("What's the first number? "))
    print("The squared answer is ", a * a)

# Create the function to add
def add():
    x, y = ask()
    print("The sum is ", x + y)

# Create the function to subtract
def subtract():
    x, y = ask()
    print("The difference is ", x - y)

# Create the function to multiply
def multiply():
    x, y = ask()
    print("The product is ", x * y)

# Determine which function the user would like to use
k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, and 5 is square. "))

# Add if the user chooses
if k==1:
    print("You are about to add.")
    add()

# Subtract if the user chooses
elif k==2:
    print("You are about to subtract.")
    subtract()

# Multiply if the user chooses
elif k==3:
    print("You are about to multiply.")
    multiply()

# Divide if the user chooses
elif k==4:
    print("You are about to divide.")
    divide()

# Square if the user chooses
elif k==5:
    print("You are about to square.")
    square()
