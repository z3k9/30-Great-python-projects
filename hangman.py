from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])
    username: str = input('What is your name?')
    print(f'Welcome to hangman, {username}!')
    
    # setup
    guessed: str = ''
    tries: int = 3
    
    while tries > 0:
        blanks: int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks +=1
    
    print() # Adds a new line
    
