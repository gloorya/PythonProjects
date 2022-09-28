#simple game to guess right number using random

import random

#let us define our function

def guess(x):
    random_num = random.randint(1,x)
    guess = 0

    while  guess != random_num:
        guess = int(input(f'Guess number between 1 and {x}: '))

        if guess <  random_num :
            print('your guess is too low')

        elif guess > random_num:
            print ('your guess is too high')

    print ('you guess right ')

guess(10)