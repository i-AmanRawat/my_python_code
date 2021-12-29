# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length=len(names)
# length=length-1
import random 
index = random.randrange(length)
print(names[index],"is going to pay for us all")

