## Importing necessary classes from other modules
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

## 1. Creating our question bank
question_bank = []
for each_q in question_data:
    question_text = each_q["question"]
    question_answer = each_q["correct_answer"]
    each_question = Question(question_text, question_answer)
    question_bank.append(each_question)

## 1. Creating our quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

## 2. Calling quiz summary
quiz.game_summary()

