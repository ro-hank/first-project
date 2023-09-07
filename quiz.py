import requests
'''
quiz project
using apis
scoreboard using database ?
'''

def main():
    print('''
          quiz game
          ''')
    

def allAPI():
    main_api = 'https://opentdb.com/api.php?amount=10'
    json_data = requests.get(main_api).json()
    print(json_data)


allAPI()
