#!/usr/bin/env python

"""
Een python script dat random wachtwoorden genereert
 """

# import
import random, string

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"

def main():
    y = int(input("How long do you want your password to be without symbols?\n"))
    length = y                                                               #To know how long the passwords needs to be

    question = int(input("How many symbols do you want to add?\n"))
    symb = string.punctuation
    symbols = str().join(random.choice(symb) for _ in range(question))        #To know how many symbols to add

    a = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits
    password = str().join(a.choice(alphabet) for _ in range(length)) + symbols    #To generate the password

    print("This is your password :", password)


if __name__ == '__main__':  # code to execute if called from command-line
    main()

