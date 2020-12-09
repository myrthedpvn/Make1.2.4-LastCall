#!/usr/bin/env python

"""
 Software installatie (linux): Apache
 """

# import
import os

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def install():
    os.system("sudo apt-get -y install apache2")                                             #To install apache

if __name__ == '__main__':                                                # code to execute if called from command-line
    install()
