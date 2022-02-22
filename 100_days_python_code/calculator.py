#calculator

def add(a,b):
  return (a+b)

def substract(a,b):
  return (a-b)
  
def multiply(a,b):
  return (a*b)

def divide(a,b):
  return (a/b)

def calculator() :
    f_number = float (input ("What's the first number? :"))
    print("+\n-\n*\n/\n")
    operation =input ("Pick an operation:")
    choice = 'y'
    while choice == 'y':
        n_number = float (input ("What's the next number? :"))
        if operation=='+':
          answer = add(f_number,n_number)
          print(f"{f_number} + {n_number} = ",answer)
        
        elif operation=='-':
          answer = substract(f_number,n_number)
          print(f"{f_number} - {n_number} = ",answer)
        
        elif operation=='*':
          answer = multiply(f_number,n_number)
          print(f"{f_number} * {n_number} = ",answer)
        
        elif operation=='/':
          answer = divide(f_number,n_number)
          print(f"{f_number} / {n_number} = ",answer)
        
        else :
          print("Enter a valid choice ...")
        
        choice = input (f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation:")
        if (choice == 'y'):
          f_number = answer
          
        else:
          calculator()

calculator()
