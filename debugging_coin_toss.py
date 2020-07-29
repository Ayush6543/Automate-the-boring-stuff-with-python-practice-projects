import random
guess = ''
options = ['heads', 'tails']
while guess not in ('heads', 'tails'):
    print('Guess the coin toss!Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)
if options[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == options[toss]:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
