# https://leetcode.com/problems/minimum-window-substring/solution/
# https://www.youtube.com/watch?v=5xuvqBjRkok
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minSubstring():
    a='xyyzyzyx'
    b='xyz'
    c=set(b)
    d = {x:0 for x in b}
    x= [(p,v) for p,v in enumerate(a)]
    print(x)
    for i in range(len(b)-1,len(a)):
        
        r=a[i]
        m=a[i-1]
        l=a[i-2]
        if r==m or m ==l or r==l:
            continue
        elif r in d or l in d or m in d:
            print(l+m+r)


        
        



        
        
    


if __name__ == '__main__':

    minimumBribes()