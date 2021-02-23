#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0 
    while i < len(c)-1:
        if i+2 < len(c):    # if there exist a cloud in two steps ahead
            if c[i+2] == 0:
                i += 2
                jumps += 1
            else:
                # there will always be a solution,
                # therfore, if we can't jump 2 steps,
                # we must have been able to jumped 1 step
                i += 1
                jumps += 1
        else:
            i += 1
            jumps += 1
    
    return jumps
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
