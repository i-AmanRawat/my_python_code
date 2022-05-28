class QuizBrain :
        def __init__ (self , q_list):
            self.question_number = 0
            self.questions_list = q_list
            self.point=0

        def next_question(self):
                self.current_question = self.questions_list[self.question_number]
                self.question_number+=1
                return input(f"Q.{self.question_number}: {self.current_question.text} (True/False)?: ")

        def still_has_question (self):
            return self.question_number < len(self.questions_list)

        def check_answer(self):
            return self.next_question() == self.current_question.answer


        def score (self):
            if self.check_answer() == True :
                self.point+=1
                print("You got it right!")
                print(f"The correct answer was: {self.current_question.answer}.")
                print("Your current score is: ", self.point, "/", self.question_number)
            else:
                print("You got it wrong!")
                print(f"The correct answer was: {self.current_question.answer}.")
                print("Your current score is: ", self.point, "/", self.question_number)



"""

this code was causing ERROR
        TypeError: 'int' object is not callable
bcz the name of method/function had name ' score ' and i was using ' score ' name as an attribute bcz of the similarity in variable it was throwing name


class QuizBrain :
        def __init__ (self , q_list):
            self.question_number = 0
            self.questions_list = q_list
            self.score=0

        def next_question(self):
                self.current_question = self.questions_list[self.question_number]
                self.question_number+=1
                return input(f"Q.{self.question_number}: {self.current_question.text} (True/False)?: ")

        def still_has_question (self):
            return self.question_number < len(self.questions_list)

        def check_answer(self):
            return self.next_question() == self.current_question.answer


        def score (self):
            if self.check_answer() == "True" :
                self.score+=1
                print("You got it right!")
                print("The correct answer was: True.")
                print("Your current score is: ", self.score, "/", self.question_number)
            else:
                print("You got it wrong!")
                print("The correct answer was: ", self.current_question.answer)
                print("Your current score is: ", self.score, "/", self.question_number)

"""


# TODO : asking the questions
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz
