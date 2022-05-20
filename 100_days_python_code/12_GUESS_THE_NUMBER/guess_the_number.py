import random
def number_generator():
  list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
  return random.choice(list_of_numbers)
  
def update_life(life):
  return life-1

logo = """  ___ _  _ ____ ____      ____ _  _ ____      __ _  _  _ _  _ ____ ____ ____ 
 / __) )( (  __) ___)    (_  _) )( (  __)    (  ( \/ )( ( \/ |  _ (  __|  _ \
( (_ ) \/ () _)\___ \      )( ) __ () _)     /    /) \/ ( \/ \) _ () _) )   /
 \___|____(____|____/     (__)\_)(_(____)    \_)__)\____|_)(_(____(____|__\_)"""

print(logo)                                                                        
print("Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = number_generator()
if(input("Choose a difficulty. Type 'easy' or 'hard' : ") == 'easy'):
  life = 10
else :
  life = 5
while (life >0):
  print(f"You have {life} attempts remaining to guess the number.")
  guess = int (input ("Make a guess : "))
  if (number ==guess):
    print("right guess you won")
    break
  elif (guess > number ):
    print("Too high\nGuess again")
    life = update_life(life)
  elif (guess < number ):
    print("Too low\nGuess again")
    life = update_life(life)
