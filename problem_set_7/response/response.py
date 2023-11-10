'''
In a file called response.py, using either validator-collection or validators from PyPI, 
implement a program that prompts the user for an email address via input and then prints 
Valid or Invalid, respectively, if the input is a syntatically valid email address. 
You may not use re. And do not validate whether the email address’s domain name actually exists.
'''
from validator_collection import validators

def main():
    print(email(input("What's your email adress? ")))


def email(s):
    try:
        if validators.email(s):
            return "Valid"
        else:
            return "Invalid"
    except ValueError:
        return "Invalid"



if __name__ == "__main__":
    main()
