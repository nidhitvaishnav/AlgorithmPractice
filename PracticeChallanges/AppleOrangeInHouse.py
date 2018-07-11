'''
 s Starting point of Sam's house location. 
 t Ending location of Sam's house location. 
 a Location of the Apple tree. 
 b Location of the Orange tree. 
 m Number of apples that fell from the tree. 
 apples Distance at which each apple falls from the tree. 
 n Number of oranges that fell from the tree. 
 oranges Distance at which each orange falls from the tree
 
 Input Format

The first line contains two space-separated integers denoting the respective values of s and t. 
The second line contains two space-separated integers denoting the respective values of a and b. 
The third line contains two space-separated integers denoting the respective values of m and n. 
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a. 
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Find how many apples and oranges will fall in sam's house. 
 '''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesInHouse = 0
    orangesInHouse = 0
    for i in apples:
        if ((a+i)>=s and (a+i)<=t):
            applesInHouse+=1
        #if -ends
    #for i -ends
    for j in oranges:
        if ((b+j)>=s and (b+j)<=t):
            orangesInHouse+=1
        #if -ends
    #for j -ends
    return applesInHouse, orangesInHouse
    
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    applesInHouse, orangesInHouse =countApplesAndOranges(s, t, a, b, apples, oranges)
    print(applesInHouse)
    print(orangesInHouse)