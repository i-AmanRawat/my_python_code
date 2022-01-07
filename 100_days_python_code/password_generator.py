#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

conbined_list = letters+numbers+symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter = ""
for i in range (nr_letters):
  lett = random.choice(letters)
  letter = letter + lett

# print(letter)

symbol = ""
for j in range (nr_symbols):
  sym = random.choice(symbols)
  symbol = symbol + sym

# print(symbol)

number = ""
for k in range (nr_numbers):
  num = random.choice(numbers)
  number = number + num 

# print(number)
print('\n')
print("Your Password is :\t",letter + symbol + number)
password01 = letter + symbol + number
# print(password01)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
lst = ""
space = " "
for l in range (len(password01)):
  lst = lst + password01[l] + space


# password03 = lst.split()
# print(password03)
print(lst)
print(lst.split( ))
random.shuffle(lst)
print(lst)
