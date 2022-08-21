
class NameError (BaseException):
    pass


def guess_name(name):
    '''
    Guess the secret name! This function
    will raise a NameError when you guess
    the wrong name and return a special
    greeting when you guess the right one.

    It will also raise a ValueError if the
    given name is not a string.
    '''
    if not isinstance(name, str):
        raise ValueError("Hey, Only strings allowed here!")
    elif name == "John":
        return "You guessed right!"
    else:
        raise NameError("That's not my name")


name = "Robbert"  # Try changing this to a number and see that happens

try:
    print(guess_name(name))
except NameError as error:
    print("You guessed wrong: {}".format(error))
except ValueError as error:
    print(error)
