def sum (list):
  sum =0
  for i in list :
    sum = sum + i 
    return sum 
    
import random as rd
ch1 = input ("Do you want to play a game of Blackjack? Type 'y' or 'n':")
play = True
while (play == True):
  if (ch1 == 'y'):
    ur_cards = []
    com_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ur_cards.append(rd.choice(cards))
    ur_cards.append(rd.choice(cards))
    print("Your cards: ",ur_cards)
    com_cards.append(rd.choice(cards))
    print("Computer's first card: ",com_cards)
  
    ch2 = input ("Type 'y' to get another card, type 'n' to pass:")
    if (ch2 == 'n'):
      com_cards.append(rd.choice(cards))
      print("Your final hand: ",ur_cards)
      print("Computer's first hand: ",com_cards)
  
      if (sum(ur_cards) == sum(com_cards)):
        print("Draw")
        print("1")
      elif (sum(ur_cards) == 18):
        print ("You Win ")
        print("2")
      elif (sum(com_cards) == 18):
        print ("computer Win ")
        print("3")
      elif (sum(com_cards) > sum(ur_cards)):
        print("Computer win")
        print("4")
      else :
        print("You win")
  
      ch3 = input ("Do you want to play a game of blackjack? Type 'y' or 'n':")
      if (ch3 == 'n'):
        play = False

  else :
    break

