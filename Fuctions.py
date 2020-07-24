import re
import random
secret_number = random.randint(1, 20)
print("I am thinking of a secret number between 1 and 20")
for guess_taken in range(1, 7):
    guess = int(input('Guess'))

    if guess > secret_number:
        print('Your guess is too high')
    elif guess < secret_number:
        print('Your guess is low')
    else:
        break

if guess == secret_number:
    print('Good job! You gueesed my number in ' + str(guess_taken) + ' guesse')
else:
    print('Nope. The number I was thinking was ' + str(secret_number))
