from random import randint

# Import random and set a variable with randint from 1-100
the_number = randint(1, 100)

# Print for showing the number > debugging
print(f'The number is: {the_number}')

# Print introduction
intro_string = '''
=====
Hello! 
This is a guessing game. 
The computer will select a number in a range from 1-100. 
Your task is to guess it. 

Good luck! 
=====
'''

print(intro_string)


def get_user_guess():
    try:
        usr_input = int(input('Your guess: '))
    except ValueError:
        print('Only numbers allowed')
        usr_input = int(input('Your guess: '))
    return usr_input


user_guess = get_user_guess()

while True:
    if the_number > user_guess:  # Check if number is small and print "To small!" and return to first step
        print('To small!')
        user_guess = get_user_guess()
    elif the_number < user_guess:  # Check if number is high and print "To big!" and return to first step
        print('To big!')
        user_guess = get_user_guess()
    else:  # If number given by user is equal to computer's number print 'You win!' and end the game.
        print('You win!')
        break
