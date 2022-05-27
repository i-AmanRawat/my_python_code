from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
length = len(question_data)
for i in range(length):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
endgame = False
correct=0
quiz = QuizBrain(question_bank)
while not endgame:
    if quiz.question_number == length:
        print("The quiz has been ended.\nYou have score: ", correct,"/",quiz.question_number)
        endgame=True
    elif quiz.next_question() == quiz.current_question.answer :
        correct += 1
        print("You got it right!")
        print("The correct answer was: True.")
        print("Your current score is: ", correct,"/",quiz.question_number)

    else :
        print("You got it wrong!")
        print("The correct answer was: ", quiz.current_question.answer)
        print("Your current score is: ", correct,"/",quiz.question_number)


