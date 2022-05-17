def validation(s):

    if not s.isalnum():  # Checks the presence of any special characters
        print("The entered input has special characters, please try again")
        return False
    if not s.isnumeric():  # Checks the presence of any letter
        print("The entered input has letters, please try again")
        return False
    if int(s) > 3999 or int(s) < 1:  # Checks if it's within the range
        print("The entered input it's bigger than 3999 or smaller than 1, please try again")
        return False
    return True


def intToRoman(n):

    rules = (  # Definition of conversions
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
    print("Welcome to the Arabic Number to Roman Number Converter Program")
    control = True
    while control:
        while True:
            number = input("\nEnter the Arabic number: ")
            if validation(number):
                print(f"The Roman equivalent of {number} is {intToRoman(int(number))}")
                break
            else:
                pass

        while True:
            leave = input("\nDo you want to leave the program? (y/n) ")
            if leave.lower() == 'y':
                print("\nThank you for using the program")
                control = False
                break
            elif leave.lower() != 'y' and leave.lower() != 'n':
                print("You entered an invalid option, please try again with y or n")
            else:
                break


main()