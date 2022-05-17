# 1. Accepts an integer from 1 to 3999 and converts it to roman numbers
# 2. Allows number conversion as many times the user wants
# 3. Checks the entered input

def validation(s):

    if not s.isalnum():
        return False
    if not s.isnumeric():
        return False
    if 1 > int(s) > 3999:
        return False
    return True

def intToRom(n):

    rules = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    )

    num = ""

    for let, val in rules:  # Travels the entire tuple of tuples
        while n >= val:  # Runs while the parameter is bigger that the current checked value
            n -= val  # Subtracts that value to the parameter
            num += let  # Adds the letter equivalent to the subtracted number

    return num


def main():
    print("Welcome to the Arabic Number to Roman Number Converter Program\n")

    number = input("Enter the Arabic number: ")

    if validation(number):
        print(f"The Roman equivalent of {number} is {intToRom(int(number))}")


main()