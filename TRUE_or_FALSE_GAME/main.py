import data
import question_model
ques_bank = []
for i in range(len(data.question_data)):
    ques_bank.append(question_model.Question(data.question_data[i]["text"], data.question_data[i]["answer"]))

print(ques_bank[5].text)
print(ques_bank[5].answer)

