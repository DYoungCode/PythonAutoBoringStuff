import random
import logging
logging.basicConfig(filename="cointoss_logging.log", level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

logging.debug("\nStart of Program")
guess = ''

def user_guess():
    while True: 
        guess = input('Guess the coin toss! Enter heads or tails: ').strip().lower()
        logging.debug("User entered: " + str(guess))

        if guess == "heads":
            return 1

        elif guess == "tails":
            return 0
        else:
            print("Error: please enter 'heads' or 'tails'")

guess = user_guess()          
logging.debug("Guess: " + str(guess))

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug("Toss: " + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = user_guess()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')







****** Original Code ******

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')