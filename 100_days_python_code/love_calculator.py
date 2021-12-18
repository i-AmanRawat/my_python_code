print("Welcome to the Love Calculator!")
print("Enter your full name.\nFor Example : Aman Rawat")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
concate_name = name1.lower() +name2.lower()
spell = 'true'
count=0
x = len(spell)
y = len(concate_name)
for i in range (0,x):
  for j in range (0,y):
    if (spell[i] == concate_name[j]) :
      count+=1
    tenth=str(count)
count=0
spells = 'love'
m = len(spells)
for i in range (0,m):
  for j in range (0,y):
    if (spells[i] == concate_name[j]) :
      count+=1
    once=str(count)
love_score = int(tenth + once)
if (love_score>=90 or love_score<=10):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>=40 and love_score<=50):
  print(f"Your score is {love_score}, you are alright together.")
else :
  print(f"Your score is {love_score}.")
