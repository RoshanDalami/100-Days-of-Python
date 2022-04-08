from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

for item in question_data:
    questions = Question(item["text"],item["answer"])
    question_bank.append(questions)


quiz = QuizBrain(question_bank)
while(quiz.still_has_question()):
    quiz.next_question()

