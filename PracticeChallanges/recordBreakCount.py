'''
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points
and least points in a game. Points scored in the first game establish 
her record for the season, and she begins counting from there.

Input Format

The first line contains an integer n, the number of games. 
The second line contains n space-separated integers describing the respective 
values of score_0, score_1,..., score_n-1
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minCount = 0
    maxCount = 0
    minScore = scores[0]
    maxScore = scores[0]
    for index, i in  enumerate(scores):
        if (index!=0 and i<minScore):
            minScore=i
            minCount+=1
        #if -ends
        if (index!=0 and i>maxScore):
            maxScore=i
            maxCount+=1
        #if -ends
    #for -ends
    return maxCount, minCount
#def breakingRecords -ends
        
if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().strip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
