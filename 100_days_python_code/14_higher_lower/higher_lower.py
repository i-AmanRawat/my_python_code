import random 
import art 
import game_data
from replit import clear

def higher_lower ():
  print(art.logo)
  end = False
  score = 0
  while(not end):
    a=random.choice(game_data.data)
    b=random.choice(game_data.data)
    print(f"Compare A : {a['name']}, {a['description']}, {a['country']}")
    print(art.vs)
    print(f"Compare B : {b['name']}, {b['description']}, {b['country']}")
    opt = input("who has more following? Type 'A' or 'B' : ")
    if (opt == 'A' and a['follower_count']>b['follower_count']):
      score +=1
      clear()
      print(art.logo)
      print(f"You are right current score {score}")
    elif (opt == 'B' and a['follower_count']<b['follower_count']):
      score +=1
      clear()
      print(art.logo)
      print(f"You are right current score {score}")
    else:
      print("sorry")
      end = True
      
higher_lower()
