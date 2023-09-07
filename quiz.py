import requests
'''
quiz project
using apis
scoreboard using database ?
'''

def main():
    print('''
          
          quiz game

          Please choose your settings :

          ''')
          
    
    num_questions = int(input("enter number of questions 1 - 10"))
    difficulty = int(input("1 - easy, 2 - medium, 3 - difficult"))
    allAPI(difficulty, num_questions)

    
    

def allAPI(difficulty, num_questions):
    main_api = 'https://opentdb.com/api.php?amount=1'
    json_data = requests.get(main_api).json()
    response_code = json_data['response_code']
    question = json_data['results'][0]['question']
    correct_answer = json_data['results'][0]['correct_answer']
    incorrect_answers_str = json_data['results'][0]['incorrect_answers']
    

    
    print(f'\nresponse code: {response_code} \nquestion: {question}\ncorrect_answer: {correct_answer} \nincorrect_answers {incorrect_answers_str}\n')
    print(f'diff: {difficulty}')

    game(json_data, num_questions)

def game(json_data, num_questions):
    print(json_data)
    print(num_questions)




main()

