from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data :
  q = Question(i['text'],i['answer'])
  question_bank.append(q)

quiz = QuizBrain(question_bank)

while(quiz.question_number < len(question_bank)) :
  quiz.next_question()

print(f"Your final score is : {quiz.score}")

