#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    lngth = len(s)
    # count number of 'a's in s
    occ_single = 0
    for char in s:
        if char == 'a':
            occ_single += 1
    
    # count total 'a's
    total = n // lngth * occ_single
    for i in range(n%lngth):
        if s[i] == 'a':
            total += 1
    
    # return the result
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
