# https://leetcode.com/problems/minimum-window-substring/solution/
# https://www.youtube.com/watch?v=5xuvqBjRkok
import math
import os
import random
import re
import sys

# find the min common ancestor.
#        1
#     2      3
#   4   5  6   7
#   (3,4) = 1

class Node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        

    def print(self):
        print(self.key)
        if self.right != None:
            self.right.print()
        if self.left != None:
            self.left.print()
        
    
    
    def findPath(self,root, path, k): 
  
        # Baes Case 
        if root is None: 
            return False
    
        # Store this node is path vector. The node will be 
        # removed if not in path from root to k 
        path.append(root.key) 
    
        # See if the k is same as root's key 
        if root.key == k : 
            return True
    
        # Check if k is found in left or right sub-tree 
        if ((root.left != None and self.findPath(root.left, path, k)) or
                (root.right!= None and self.findPath(root.right, path, k))): 
            return True 
    
        # If not present in subtree rooted with root, remove 
        # root from path and return False 
        
        path.pop() 
        return False

    def findLCA(self,root, n1, n2): 
        path1=[]
        path2=[]
        if (not self.findPath(root,path1,n1) or not self.findPath(root,path2,n2)):
            return -1
        i= 0 
        
        while (i < len(path1) and i <len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]

        

        

        


def findCommonAncestor():
    
    
    # Driver program to test above function 
    # Let's create the Binary Tree shown in above diagram 
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.print()
    p=[]

    root.findPath(root,p, 6)
    print(p)


    print( root.findLCA(root, 4, 5,)) 
    print( root.findLCA(root, 4, 6,)) 

    
    # print('LCA(4, 6) = ', findLCA(root, 4, 6)) 
    # print('LCA(3, 4) = ', (findLCA(root,3,4)) 
    # print('LCA(2, 4) = ', (findLCA(root,2, 4))    
    



    





if __name__ == '__main__':

    findCommonAncestor()


#         1
#     2          3
# 4      5     6     7