#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

# Complete the activityNotifications function below.
def mid_elem(arr):
    lngth = len(arr)
    if lngth % 2 == 0:
        i = int(math.floor(lngth/2))
        j = int(math.ceil(lngth/2))
        return (arr[i] + arr[j]) / 2
    return arr[(lngth//2)]
    
def activityNotifications(expenditure, d):
    # total notifs
    notifs = 0
    # initialize the window arr
    arr = [None] + sorted(expenditure[0:d-1])
    # start checking fraudent activities
    for i in range(d-1,len(expenditure)-1):
        arr = arr[1:]
        # insert the next element into arr and maintain the sorted structure
        nxt = expenditure[i]
        j = 0
        while j < len(arr):
            if arr[j] < nxt:
                j += 1
            else:
                break
        # insert the new element inside arr
        arr.insert(j, nxt)
        print(arr)
        print(mid_elem(arr))
        # check fraudent activity
        if expenditure[i+1] >= 2 * mid_elem(arr):
            notifs += 1
    # return the result
    return notifs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
