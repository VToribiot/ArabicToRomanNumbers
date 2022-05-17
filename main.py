# 1. Accepts an integer from 1 to 3999 and converts it to roman numbers
# 2. Allows number conversion as many times the user wants
# 3. Checks the entered input

def validation(s):

    if not s.isalnum():
        return False
    if not s.numeric():
        return False
    if 1 > int(s) > 3999:
        return False
    return True

def main():
    print("Welcome to the Arabic Number to Roman Number Converter Program\n")

    number = input("Enter the Arabic number: ")

    # input validation function

    # number conversion function
