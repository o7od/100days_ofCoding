## asking the questions
## checking if the answer was correct
## checking if we are at the end of the quiz

class QuizBrain:

    ## Constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ").capitalize()
        self.question_number += 1
        self.check_answer(answer, current_question.answer)
        

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            print("You got it right! ")
            self.score += 1
        else:
            print("That's wrong.")
        
        print(f"The correct answer was: {actual_answer}\nYour current score is: {self.score}/{self.question_number}\n")


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def game_summary(self):
        print(f"You've completed the quiz\nYour final score was: {self.score}/{self.question_number}")