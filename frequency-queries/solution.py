#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    
    # create an occ map
    db = {}
    ans = []
    
    # start executing every queries in the queries array
    for query in queries:
        # extract the instruciton and element
        ins = query[0]
        elem = query[1]
        # execute the instruction
        if ins == 1:
            db[elem] = db.get(elem, 0) + 1
        elif ins == 2:
            if db.get(elem, 0) != 0:
                db[elem] = db.get(elem, 0) - 1
        elif ins == 3:
            if elem in db.values(): 
                ans.append(1)
            else: ans.append(0)
        else:
            raise Exception('Instruction not recognized')
    
    # return the answer
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
