#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = (random.choice(word_list))
print((chosen_word))
count = len(chosen_word)+1
dash =  ("__  "*(count))
print(dash)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Make a guess ! \n ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in range (1,count):
    if (guess==chosen_word[i]):
        print( f"{'__ '*(i-1) + chosen_word[i] + ' __ '*(count-i-1)}" )
