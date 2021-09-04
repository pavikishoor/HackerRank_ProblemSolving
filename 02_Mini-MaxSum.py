#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    #arr.sort()
    #print(f'{sum(arr[:4])} {sum(arr[len(arr) - 4:])}')
    arr_sort = sorted(arr)
    print(sum(arr_sort[0:4]),end=' ')
    print(sum(arr_sort[-4:]),end=' ')

if __name__ == '__main__':

    arr = list(map(int,input().rstrip().split()))
    
    miniMaxSum(arr)
