import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
list = [rock,paper,scissors]
m = int (input ("Make a choice :"))
n = random.randrange(3)
print('You choose \n')
print(list[m])
print('Your opponent choose\n')
print(list[n])

if(m==n):
  print('Draw')
# elif(m==0 && n==0)
elif(m==0 & n==1):
  print('loose')
elif(m==0 & n==2):
  print('win')
elif(m==1 & n==0):
  print('win')
# elif(m==1 && n==1)
elif(m==1 & n==2):
  print('loose')
elif(m==2 & n==0):
  print('loose')
elif(m==2 & n==1):
  print('win')
# elif(m==2 && n==2)
