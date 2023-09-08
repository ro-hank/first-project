import requests
import random
'''
quiz project
using apis
scoreboard using database ?
'''
    #user chooses settings
def main():
    print('''
          
          quiz game

          Please choose your settings :

          ''')
          
    
    num_questions = int(input("enter number of questions 1 - 10"))
    difficulty = int(input("1 - easy, 2 - medium, 3 - difficult"))
    allAPI(difficulty, num_questions)

    
    
    #calls api

def allAPI(difficulty, num_questions):
    main_api = 'https://opentdb.com/api.php?amount=1'
    json_data = requests.get(main_api).json()
    print(f'diff: {difficulty}')
    game(json_data, num_questions)


def game(json_data, num_questions):
    score = 0
    count = 0
    answers = []

    response_code = json_data['response_code']
    question = json_data['results'][0]['question']
    correct_answer = json_data['results'][0]['correct_answer']
    incorrect_answers_ls = json_data['results'][0]['incorrect_answers']
    
    print(f'\nresponse code: {response_code} \nquestion: {question}\ncorrect_answer: {correct_answer} \nincorrect_answers {incorrect_answers_ls}\n')
    answers.append(correct_answer)
    for i in range(len(incorrect_answers_ls)):
        answers.append(incorrect_answers_ls[i])

    random.shuffle(answers)
    print(answers)


    print("\nEnter number\n")
    j = 1
    for j, choice in enumerate(answers, 1):
        print(j, choice)
    user_choice = int(input())


    if user_choice == (answers.index(correct_answer) + 1):
        score = score + 1    
    print(score)




main()

