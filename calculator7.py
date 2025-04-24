 # Create the function to obtain x and y
def ask():
  while True:
    try:
      x = float(input("What is the first number? "))
      y = float(input("What is the second number? "))
    except ValueError:
      print("Please type in a number.")
    else:
      return x, y
   
 # Create the function to divide
def divide():
  x, y = ask()
  if y == 0:
    print("You can't divide by zero.")
  else:
    z = round(x/y, 4)
    print("The quotient is ", z)
 
 # Create the function to use powers
def powers():
  while True:
    try:
      x = float(input("What number would you like to raise? "))
      y = float(input("What would you like to raise it to the power of? "))
    except ValueError:
      print("Please type in a number.")
    else:
      z = round(x ** y, 4)
      print("The answer is ", z)
      break
 
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
  while True:
    try:
      x = float(input("What would you like to take the square root of? "))
    except ValueError:
      print("Please put in a number.")
    else:
      break
  if x < 0:
    print("You can't take the square root of a negative number.")
  else:
      print(round(x ** .5, 4))

# Create the function to use factorials
def factorials():
  x = int(input("What would you like to take the factorial of? "))
  fact = 1
  for i in range(1, x + 1):
    fact *= i
  print(fact)


while True:
  while True:
    # Determine which function the user would like to use
    try:
      k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is raise to the power of _, 6 is square root, 7 is factorial, and 8 is quit "))
    except ValueError:
      print("Please choose a given number.")
    else:
      break

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

  # Factorial if the user chooses
  elif k==7:
    print("You are about to use factorials.")
    factorials()

  # Create a way for the user to end the program.
  elif k==8:
    print("Thank you for using my calculator.")
    break

  # Determine what to do if the user is annoying and doesn't choose a given function
  else:
    print("Please choose a given number.")
