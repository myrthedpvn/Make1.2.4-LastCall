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
    print('What do you like to install?\n 1.Apache\n 2.MariaDB\n 3.PHP')
    choice = input('Give me your choice pleas:')

    if choice == "1":
      os.system("sudo apt-get -y install apache2")                                             #To install Apache
    elif choice == "2":
        os.system("sudo apt install mariadb-server")                                           #To install MariaDB
    elif choice == "3":
        os.system("sudo apt install php libapache2-mod-php")                                   #To install PHP

if __name__ == '__main__':                                                # code to execute if called from command-line
    install()
