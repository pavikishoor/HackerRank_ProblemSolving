#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    c1=0
    c2=0
    c3=0
    for i in range(0,len(arr)):
        if(arr[i])>0:
            c1+=1
        if(arr[i]<0):
            c2+=1
        if(arr[i]==0):
            c3+=1
    r1 = c1/len(arr)
    r2 = c2/len(arr)
    r3 = c3/len(arr)
    print("{:.6f}".format(r1))
    print("{:.6f}".format(r2)) 
    print("{:.6f}".format(r3))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
