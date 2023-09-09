import requests
import random
import os
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
          
    
    num_questions = int(input("enter number of questions 1 - 10\n"))
    difficulty = int(input("1 - easy, 2 - medium, 3 - difficult\n"))
    game(num_questions, difficulty)

    
    




def game(num_questions, difficulty):
    score = 0
    count = 0
    answers = []

    while count < num_questions:
        os.system("cls || clear")
        main_api = 'https://opentdb.com/api.php?amount=1'
        json_data = requests.get(main_api).json()
        response_code = json_data['response_code']
        question = json_data['results'][0]['question']
        correct_answer = json_data['results'][0]['correct_answer']
        incorrect_answers_ls = json_data['results'][0]['incorrect_answers']
        
        #print(f'\nresponse code: {response_code} \nquestion: {question}\ncorrect_answer: {correct_answer} \nincorrect_answers {incorrect_answers_ls}\n')
        print(f'\nquestion: {question}')
        answers.append(correct_answer)
        for i in range(len(incorrect_answers_ls)):
            answers.append(incorrect_answers_ls[i])

        random.shuffle(answers)


        print("\nEnter number\n")
        j = 1
        for j, choice in enumerate(answers, 1):
            print(j, choice)
        user_choice = int(input())


        if user_choice == (answers.index(correct_answer) + 1):
            score = score + 1    
            print("correct")
        else: 
            print("incorrect")
        answers.clear()
        count = count + 1

        print(f'\nFinal score: {score}\n')
        play_again = input("Play again -Y/N\n")

        if play_again.lower == "y":
            main()
        else:
            print("Thank you for playing")
            exit()




main()

