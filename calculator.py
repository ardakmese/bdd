def add(a, b):
    """This function adds two numbers"""
    return int(a) + int(b)

def subtract(x, y):
   """This function subtracts two numbers"""
   return int(x) - int(y)

def multiply(x, y):
   """This function multiplies two numbers"""
   return int(x) * int(y)

def divide(x, y):
   """This function divides two numbers"""
   try:
       return int(x) / int(y)
   except ZeroDivisionError:
       return 0