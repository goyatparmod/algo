#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribe = 0 
    for p,v in enumerate(q):
        print(p,v)
    print('-------------')
    for p,v in enumerate(q):

        if (v-p-1) > 2:
            
            return 'Too chaotic'
        for j in range(max(0,v-2), p):
            print(q[j],v)
            if q[j] > v:
                bribe+=1
    return bribe
        
    


if __name__ == '__main__':
    q=[2,1,5, 3 ,4]
    q=[2, 1, 5, 3, 4]


    print(minimumBribes(q))