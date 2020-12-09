#!/usr/bin/env python

"""
 gpio pin weergave en hun status
 """

# import
import os

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def pin():
    os.system("pinout")                                                          #To show the pin and his status


if __name__ == '__main__':  # code to execute if called from command-line
    pin()