'''
The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location as part of the show.

Complete the function kangaroo which takes starting location and speed of 
both kangaroos as input, and return YES or NO appropriately. 
Can you determine if the kangaroos will ever land at the same location at 
the same time? The two kangaroos must land at the same location after making the same number of jumps.

INPUT: A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.
'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if ((x1>x2 and v1>=v2) or (x1<x2 and v1<=v2)):
        return "NO"
    else:
        if((x1-x2)%(v2-v1)==0):
            return "YES"
        else:
            return "NO"
        #if -ends
    #if -ends
#def kangaroo -ends

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
