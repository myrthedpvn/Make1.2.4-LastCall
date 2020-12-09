#!/usr/bin/env python

"""
 Info about our project comes here.
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def guess():
    list = ["flamingo", "hond", "stokstaartje", "beer", "leeuw"]
    a = 0
    while a < 3:                                                             #To know how many times u can try
        guess = input(f"Guess the word.\n")
        for x in list:
            if guess == x:                                                   #To see if they guessed a word from list
                print("Jej, you won.")
                return                                                       #To quit the loop after they guessed right
        else:
            a+=1



if __name__ == '__main__':  # code to execute if called from command-line
    guess()
