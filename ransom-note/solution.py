#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    # create a dict that counts the number of occurance of each word in the magazine
    dictionary = {}
    for w in magazine:
        try:
            dictionary[w] += 1
        except KeyError:
            dictionary[w] = 1
            
    # see if we can create the ransom note
    flag = True
    for w in note:
        try: 
            if dictionary[w] == 0:
                # running out of word
                print("No")
                flag = False
                break
            else:
                dictionary[w] -= 1
        except KeyError:
            print("No")
            flag = False
            break
    
    # if the note is possible
    if flag == True:
        print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
