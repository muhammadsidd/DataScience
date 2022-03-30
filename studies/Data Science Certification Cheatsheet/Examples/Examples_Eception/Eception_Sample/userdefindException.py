# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class InputTooSmallError(Error):
    """Raised when the entered alpahbet is smaller than the actual one"""
    pass


class InputTooLargeError(Error):
    """Raised when the entered alpahbet is larger than the actual one"""
    pass


# our main program
# user guesses an alphabet until he/she gets it right
# you need to guess this alphabet
alphabet = 'm'

while True:
    try:
        guess = input("Enter an alphabet: ")
        if guess < alphabet:
            raise InputTooSmallError
        elif guess > alphabet:
            raise InputTooLargeError

    except InputTooSmallError:
        print("The entered alphabet is too small, try again!")
        print('')
    except InputTooLargeError:
        print("The entered alphabet is too large, try again!")
        print('')
    else:
        print("you guessed correctly")
        break
        # load other services
        # load the services, depending on the location
    finally:
        print("its a finally block. Thanks for guessing")
