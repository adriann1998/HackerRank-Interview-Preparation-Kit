#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    # sort the price
    prices.sort()
    # pick the top cheapest toys, 
    # and then buy them until k is not sufficient to buy the next toy
    total = 0
    for price in prices:
        if price <= k:
            k -= price
            total += 1
    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
