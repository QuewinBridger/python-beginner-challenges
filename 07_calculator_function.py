def calculate(number1, number2, math_operator):

  if math_operator == '*':
    return number1*number2

  elif math_operator == "/":
    return number1/number2

  elif math_operator == '-':
    return number1-number2

  elif math_operator == '+':
    return number1+number2
  
  else: 
    return number1%number2

number1 = int(input("Enter first number"))
math_operator = str(input("Enter the maths operator, i.e. * for multiplication or / for division"))
number2 = int(input("Enter second number"))

print(calculate(number1,number2,math_operator))
