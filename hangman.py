from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])
    username: str = input('What is your name? ')
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
        
        if blanks == 0:
            print('You got it')
            break
        
        guess: str =input('Enter a letter:')
        if guess in guessed:
            print(f'You already used "{guess}". Please try another letter!')
            continue
        
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f'Sorry that was a bad guess. {tries} tries left')
            
            if tries == 0:
                print('Game over, no more tries left')
                break
                
            
            
if __name__ == '__main__':
    run_game()