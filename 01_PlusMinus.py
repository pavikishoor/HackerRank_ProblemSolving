#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    i=1
    neg = 0
    pos = 0
    zero = 0
    n=len(arr)
    for i in range(n):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zero+=1
    print(round((pos/n),6))
    print(round((neg/n),6))
    print(round((zero/n),6))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
