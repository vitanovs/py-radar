"""
This module defines user input utilities.
"""
from errors import InvalidInputException

_LIMIT_MAX_INPUT_MISTAKES = 3
_INPUT_QUIT_VALUE = 'quit'

def input_message():
    """Takes `Message` variable input."""
    message = input('Enter message: ')
    if message.lower() == _INPUT_QUIT_VALUE:
        raise KeyboardInterrupt()

    return message

def input_spam(cycle=0):
    """Takes `Spam` variable input."""
    if cycle > _LIMIT_MAX_INPUT_MISTAKES:
        raise InvalidInputException('Maximal limit of invalid inputs was reached!')

    spam = input('Is Spam [yes/no]: ')
    result = False
    if spam.lower() == 'yes':
        result = True
    elif spam.lower() == 'no':
        result =  False
    else:
        msg = 'Invalid input. Try Again!'
        if cycle > 0 & cycle <= _LIMIT_MAX_INPUT_MISTAKES:
            msg = 'Invalid input. Attempt {}!'.format(cycle + 1)
        print(msg)
        result = input_spam(cycle + 1)
    return result
