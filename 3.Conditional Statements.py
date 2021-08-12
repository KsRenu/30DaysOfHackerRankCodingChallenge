# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# Explanation

# Sample Case 0: n=3
#  n is odd and odd numbers are weird, so we print Weird.

# Sample Case 1: n=24
#  n>20 and n is even, so it is not weird. Thus, we print Not Weird.


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

if N%2==1:
    print('Weird')
elif N%2==0:
    if N>=2 and N<=5:
        print('Not Weird')
    elif N>=6 and N<=20:
        print('Weird')
    else:
        print('Not Weird')
