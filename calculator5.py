 # Create the function to obtain x and y
def ask():
  try:
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    return x, y
  except ValueError:
    print("Error")
   
 # Create the function to divide
def divide():
  try:
    x, y = ask()
    z = round(x/y, 4)
    print("The quotient is ", z)
  except ValueError:
    print("Error")
 
 # Create the function to use powers
def powers():
  try:
    x = float(input("What number would you like to raise? "))
    y = float(input("What would you like to raise it to the power of? "))
    z = round(x ** y, 4)
    print("The answer is ", z)
  except ValueError:
    print("Error")
 
 # Create the function to add
def add():
  x, y = ask()
  z = round(x + y, 4)
  print("The sum is ", z)
 
 # Create the function to subtract
def subtract():
  x, y = ask()
  z = round(x - y, 4)
  print("The difference is ", z)
 
 # Create the function to multiply
def multiply():
  x, y = ask()
  z = round(x * y, 4)
  print("The product is ", z)

# Create the function to root
def square_root():
  try:
    x = float(input("What would you like to take the square root of? "))
    if x < 0:
        print("Error")
    else:
        print(round(x ** .5, 4))
  except ValueError:
    print("Error")

 # Determine which function the user would like to use
try:
  k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is raise to the power of _, and 6 is square root."))
except ValueError:
  print("Please choose a given number.")

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

 # Root if the user chooses
elif k==6:
  print("You are about to square root.")
  square_root()

 # Determine what to do if the user is annoying and doesn't choose a given function
else:
  print("Please choose a given number.")
