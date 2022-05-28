from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
length = len(question_data)
for i in range(length):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.score()
