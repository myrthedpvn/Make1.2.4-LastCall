#!/usr/bin/env python

"""
 Een poortscanner.
 """

# import
from socket import *
import time

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def scan():
    startTime = time.time()                                                          #To set the start time
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
    print('Time taken:', time.time() - startTime)                                     #To know how long it took to find


if __name__ == '__main__':  # code to execute if called from command-line
    scan()
