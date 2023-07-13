from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# first we're creating a list of questions so it can be passed to our quiz object
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# creating object quiz and passing question_bank
quiz = QuizBrain(question_bank)
# the quiz runs until we run out of questions
while quiz.still_has_questions():
    quiz.next_question()
# once no more questions:
print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
