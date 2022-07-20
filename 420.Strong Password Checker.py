#It has at least 6 characters and at most 20 characters.
#It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
#It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

from pyparsing import nums


def strongPasswordChecker(password: str) -> int:

    numSteps = 0

    hasUpperCase = False
    hasLowerCase = False
    hasDigit = False
    hasRepetion = False

    if len(password) < 6:
        numSteps = 6 - len(password)

    elif len(password) > 20:
        numSteps = len(password) - 20

    else:
        for i in range(len(password)):
           
            if not hasLowerCase:
                if password[i].islower():
                    numSteps = numSteps - 1
                    hasLowerCase = True

            if not hasUpperCase:
                if password[i].isupper():
                    numSteps = numSteps - 1
                    hasUpperCase = True

            if not hasDigit:
                if password[i].isdigit():
                    numSteps = numSteps - 1
                    hasDigit = True
            
            if i < len(password) - 1:
            
                numRepetion = 0

                while password[i] == password[i+1]:
                    numRepetion = numRepetion + 1
                    i = i + 1

            if numRepetion > 1:
                numSteps = numSteps + 1

    return numSteps if numSteps > 0 else 0


for test in ["a", "aA1", "1337C0d3", "aaa123"]:
    print(f'{test} = {strongPasswordChecker(test)}')