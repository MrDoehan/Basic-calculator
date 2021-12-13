def calculator():
  num1 = int(input("Variable: "))
  while num1:
    operation = input("Operator? +, -, *, /, **, % ")
  
    num2 = int(input("Variable: "))
    display = input("Do you want to display the result? y/n: ")
    
    if display == "n":
      if operation == "+":
        num1 = num1 + num2
      elif operation == "-":
        num1 = num1 - num2
      elif operation == "/":
        num1 = num1 / num2
      elif operation == "*":
        num1 = num1 * num2
      elif operation == "%":
        num1 = num1 % num2
      elif operation == "**":
        num1 =num1 ** num2
      else:
        print("What do phoque?")

    
    elif display == "y":
      if operation == "+":
        print(num1 + num2)
      elif operation == "-":
        print(num1 - num2)
      elif operation == "/":
        print(num1 / num2)
      elif operation == "*":
        print(num1 * num2)
      elif operation == "%":
        print(num1 % num2)
      elif operation == "**":
        print(num1 ** num2)
      else:
        print("What do phoque?")
    else:
      print("No.")    
