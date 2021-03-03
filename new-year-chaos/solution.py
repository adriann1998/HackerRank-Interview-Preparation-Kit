#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    # number of swaps/moves
    moves = 0
    
    # count the number of bribes
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        # count how many times did q[i] received bribes
        # one can only receive bribes from the one behind 
        for j in range(i):
            if q[j] > q[i]:
                moves += 1
    
    # print the final result
    print(moves)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
