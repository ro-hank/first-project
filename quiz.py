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
    allAPI(difficulty)

    
    

def allAPI(difficulty):
    main_api = 'https://opentdb.com/api.php?amount=1'
    json_data = requests.get(main_api).json()
    print(json_data)
    response_code = json_data['response_code']
    question = json_data['results'][0]['question']
    correct_answer = json_data['results'][0]['correct_answer']
    incorrect_answers_str = json_data['results'][0]['incorrect_answers']
    

    
    print(f'\nresponse code: {response_code} \nquestion: {question}\ncorrect_answer: {correct_answer} \nincorrect_answers {incorrect_answers_str}\n')
    print(f'diff: {difficulty}')


def game(num_questions):
    exit() 




main()

