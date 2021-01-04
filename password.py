#!/usr/bin/env python

"""
Een python script dat random wachtwoorden genereert
 """

# import
import random
import string

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def symbols_p():
    global symbols
    question = int(input("How many symbols do you want to add? "))
    symb = string.punctuation
    symbols = str().join(random.choice(symb) for i in range(question))                 # To know how many symbols to add

def letters():
    global let
    question2 = int(input("How many upper cases and lower cases do you want? "))
    letter = string.ascii_uppercase + string.ascii_lowercase
    let = str().join(random.choice(letter) for i in range(question2))     #To know how many uper and lower cases to add

def digits():
    global digit
    question3 = int(input("How many digits do you want? "))
    dig = string.digits
    digit = str().join(random.choice(dig) for i in range(question3))                     #To know how many digits to add

def random_p():
    global password
    password = str().join(random.sample(symbols + let + digit, len(symbols + let + digit)))   #To randomise the password


def main():
    symbols_p()
    letters()
    digits()
    random_p()
    print("\n")
    print(password)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
