#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    
    total = 0
    
    for i in range(1, len(s)+1):
        dicty = {}
        for j in range(len(s)-i+1):
            substr1 = s[j:j+i]
            for k in range(j+1, len(s)-i+1):
                substr2 = s[k:k+i]
                if sorted(list(substr1)) == sorted(list(substr2)):
                    total += 1
    
    return total
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
