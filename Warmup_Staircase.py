#The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of 6 (size/ eg 6 ).

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    j=0
    for i in range(1,n+1): 
        word = ""
        for j in range(1,n-i+1):  # space need is (n-i) / eg: n = 6 then, space = 6 -1 =>5 (so 5 space is added first )
            word += " "
        word += "#" * i  # after adding space we need to print i times the symbol (because we subtracted i from n) 
        print(word)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
