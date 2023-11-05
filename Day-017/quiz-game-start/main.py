from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

# for i in range(len(question_data)):
#     question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

for i in range(len(question_data["results"])):
    question_bank.append(Question(question_data["results"][i]["question"], question_data["results"][i]["correct_answer"]))

print(len(question_bank))

quiz_brain=QuizBrain(question_bank)

# print(question_bank[1].text, question_bank[1].answer )
while quiz_brain.still_has_questions():
    print(quiz_brain.next_question())

print(f"You've completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")