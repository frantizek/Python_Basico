import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

number_guess = 0 if guess == "tails" else 1
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == number_guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    number_guess = 0 if guess == "tails" else 1
    if toss == number_guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')