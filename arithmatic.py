def ask():
  while True:
    try:
      x = float(input("What is the first number? "))
      y = float(input("What is the second number? "))
    except ValueError:
      print("Please type in a number.")
    else:
      return x, y
    
def divide():
  x, y = ask()
  if y == 0:
    print("You can't divide by zero.")
  else:
    z = round(x/y, 4)
    print("The quotient is ", z)
 
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
 
def add():
  x, y = ask()
  z = round(x + y, 4)
  print("The sum is ", z)
 
def subtract():
  x, y = ask()
  z = round(x - y, 4)
  print("The difference is ", z)
 
def multiply():
  x, y = ask()
  z = round(x * y, 4)
  print("The product is ", z)

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

def factorials():
  while True:
    try:
      x = int(input("What would you like to take the factorial of? "))
    except ValueError:
      print("You can only take the factorial of positive whole numbers.")
    else:
      if x < 0:
        print("You can only take the factorial of positive whole numbers.")
      elif x > 0 and x < 100:
        fact = 1
        for i in range(1, x + 1):
          fact *= i
        print(fact)
        break
      elif x > 100:
        print("I'm sorry, the number is too large.")
