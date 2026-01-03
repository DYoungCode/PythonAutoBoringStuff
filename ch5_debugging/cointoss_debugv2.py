# version 2 of cointoss_debug.py.  Use dictionary to map
# tails to 0 and heads to 1

import random
import logging
logging.basicConfig(filename="cointoss_logging.log", level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

logging.debug("\nStart of Program")

def get_user_guess():
    
    while True:
        guess = input("Please guess 'heads' or 'tails': ").strip().lower()
        logging.debug("User input is: " + guess)
        if guess == "heads" or guess == "tails":
            return guess
        else:
            print("Error: you didn't enter 'heads' or 'tails'.")


toss_map = {0: 'tails', 1: 'heads'}
random_int = random.randint(0, 1)
toss_result = toss_map[random_int]
logging.debug("The random coin toss result is: " + toss_result)

guess = get_user_guess()

if guess == toss_result:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = get_user_guess()
    if guess == toss_result:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

# ****** Original Code ******

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')