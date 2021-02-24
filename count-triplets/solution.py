#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    total = 0
    
    for i in range(1, len(arr)-1):
        left_count = 0
        right_count = 0
        for j in range(0,i):
            if arr[j] == arr[i]/r:
                left_count += 1
        for j in range(i+1, len(arr)):
            if arr[j] == arr[i]*r:
                right_count += 1
        total += left_count * right_count
    
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
