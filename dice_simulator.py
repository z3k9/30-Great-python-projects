from random import randint
import random

def roll_dice(amount: int =2):
    if amount <= 0:
        raise ValueError('Number of dice must be greater than 0')
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll =  random.randint(1,6)
        rolls.append(random_roll)
        
    return rolls

def main():
    while True:
        try:
            user_input: str = input('How many dice do you want to roll?')
            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break
            print(*roll_dice(int(user_input)), sep=', ')
        
        except ValueError:
            print('Please enter a valid number')

if __name__ == "__main__":
    main()
