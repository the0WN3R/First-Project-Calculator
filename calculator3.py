def ask():
  x = float(input("What is the first number? "))
  y = float(input("What is the second number? "))
  return x, y
 
 # Create the function to divide
def divide():
  x, y = ask()
  print("The quotient is ", x/y)
 
 # Create the function to use powers
def powers():
  x = float(input("What number would you like to raise? "))
  y = float(input("What would you like to raise it to the power of? "))
  print("The answer is ", x ** y)
 
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

# Create the function to root
def square_root():
    x = float(input("What would you like to take the square root of? "))
    if x < 0:
        print("Error")
    else:
        print(x ** .5)
 
 # Determine which function the user would like to use
k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is raise to the power of _, and 6 is square root."))
 
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
  print("You are about to use powers.")
  powers()

elif k==6:
  print("You are about to square root.")
  square_root()
