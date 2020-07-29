#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_s=0
    b_s=0
    for i in range(3):
        if a[i]>b[i]:
            a_s+=1
        elif b[i]>a[i]:
            b_s+=1
        else:
            a_s+=0
            b_s+=0
    return a_s,b_s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
