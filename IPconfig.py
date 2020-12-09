#!/usr/bin/env python

"""
 IP weergave
 """

# import
import os

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def ip():
    os.system("ipconfig")                                                            #To show information about ur IP

if __name__ == '__main__':
    ip()