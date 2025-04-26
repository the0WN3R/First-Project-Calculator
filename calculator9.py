import arithmatic

while True:
  while True:
    try:
      k = int(input("What would you like to do? 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is raise to the power of _, 6 is square root, 7 is factorial, and 8 is quit "))
    except ValueError:
      print("Please choose a given number.")
    else:
      break

  if k==1:
    print("You are about to add.")
    arithmatic.add()

  elif k==2:
    print("You are about to subtract.")
    arithmatic.subtract()

  elif k==3:
    print("You are about to multiply.")
    arithmatic.multiply()

  elif k==4:
    print("You are about to divide.")
    arithmatic.divide()

  elif k==5:
    print("You are about to use powers.")
    arithmatic.powers()

  elif k==6:
    print("You are about to square root.")
    arithmatic.square_root()

  elif k==7:
    print("You are about to use factorials.")
    arithmatic.factorials()

  elif k==8:
    print("Thank you for using my calculator.")
    break

  else:
    print("Please choose a given number.")
