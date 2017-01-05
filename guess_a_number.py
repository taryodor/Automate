#Program that asks you what your name is
#Then it thinks a number and gives you up to six chances
#To guess it
import random

your_name = input("What is your name? ")
print('Hello ' + your_name + ', can you guess a number between 1 and 42?')
secret_number = random.randint(1, 42)
guess = 0
guess_count = 0
while guess != secret_number:
    guess_count += 1
    print('Take a guess')
    guess = int(input())
    if guess == secret_number:
        print('Goodjob ' + your_name + ', You have made it!')
        print('You have made it in {} guesses'.format(guess_count))
        break
    elif guess > secret_number:
        print('Your guess is too high, or are you?')
    elif guess < secret_number:
        print('Your guess is too low.')
    if guess_count > 6:
        print('It must be hard to be retarded.')
        print(secret_number, 'was the number.')
        break
    
    
