entry = int(input("Enter the limit :"))
for i in range ( 1 , entry + 1 ):
  if (i%3==0):
    print("FIZZ \n")
  
  elif (i%5==0):
    print("BUZZ \n")

  elif (i%3==0 & i%5==0):
    print("FIZZBUZZ \n")

  else:
    print(i ,"\n")
