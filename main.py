#!/usr/bin/env python

"""
 Je maakt of hebt een ander scriptje dat je hier importeert. Hier kan je dan een optie kiezen welke code je wilt runnen.
 """

# import
import password
import IPconfig
import linux
import software_install
import system_info
import port_scan
import gpio_pin
import guess

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def restart():
    options()


def options():
    print(f'Hi, what do you want to do? \n 1.IPConfig\n 2.Passwordgenerator\n 3.Update & Upgrade in Linux\n '
          f'4.Software installation\n 5.System info\n 6.Port scan\n 7.Gpio pin\n 8.Guess game')
    choice = input('Give me your choice:')

#To see what the choice is and what the code needs to do then
    if choice == "1":
        IPconfig.ip()
        print("\n")
        restart()
    elif choice == "2":
        password.main()
        print("\n")
        restart()
    elif choice == "3":
        linux.update_upgrade()
        print("\n")
        restart()
    elif choice == "4":
        software_install.install()
        print("\n")
        restart()
    elif choice == "5":
        system_info.main()
        print("\n")
        restart()
    elif choice == "6":
        port_scan.scan()
        print("\n")
        restart()
    elif choice == "7":
        gpio_pin.pin()
        print("\n")
        restart()
    elif choice == "8":
        guess.guess()
        print("\n")
        restart()
    else:
        exit()

if __name__ == '__main__':  # code to execute if called from command-line
    options()