#!/usr/bin/env python

"""
 System update en upgrade (linux)
 """

# import
import os

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def update_upgrade():
    os.system("sudo apt-get update -y")                                                  #To update your system
    os.system("sudo apt-get upgrade -y")                                                 #To upgrade your system

