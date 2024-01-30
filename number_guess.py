from random import randint

lower_num, higher_num =1,10
random_num: int =randint(lower_num, higher_num)

print(f'Guess the number in the range from {lower_num} to {higher_num}')

while True:
    try:
        user_guess: int = int(input('Guess: ')) 
    except ValueError as e:
        print('Please enter a valid number')
        continue

    if user_guess > random_num:
        print('The number is lower')
    elif user_guess < random_num:
        print('The number is greater')
    else: 
        print('You guessed it!')
        break

    