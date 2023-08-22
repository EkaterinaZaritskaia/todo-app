# we are going to create json file in same "bonus" directory
# we create a list of dictionary and move it to question.json file

import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content) # we create a "data" variable; "loads" means (load), (s)-string; the string - is content
#"data" - is a whole list
score = 0
for question in data: # we iterate over the data list(перебрать список данных), which is a list of dictionaries
    print(question["question_text"])
# now we need to print out "alternatives"
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: ")) # using "int"-integer, becouse user should enter a number. INT - convert
    question["user_choice"] = user_choice
# "user_choice" - is a key, user_choice - is a value of "user_choice"

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]: # if the users_choice is equal to correct_answer
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))