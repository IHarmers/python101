
def guess_name(name):
    '''
    Guess the secret name! This function
    return False when you guess
    the wrong name and return True
    when you guess the right one.

    It will also raise a ValueError if the
    given name is not a string.
    '''
    if not isinstance(name, str):
        raise ValueError(
            "Name must be a string type. Got {}".format(type(name)))
    elif name == "John":
        return True
    else:
        return False


names = [
    "Robbert",
    "Sam",
    15,
    "John",
    "Jane",
    "Daniel",
    "Jack",
    True,
    "James"
]

for name in names:
    try:
        if guess_name(name):
            print("You guessed right! My name is {}".format(name))
        else:
            print("You guessed wrong! {} is not my name".format(name))
    except ValueError as error:
        index = names.index(name)
        print("There is something wrong with the name on index {}: {}".format(
            index, error))
