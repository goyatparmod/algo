# Python3
# Given a pattern as below and an integer n your task is to decode it and print nth row of it. The pattern follows as :
# 1
# 11
# 21
# 1211
# 111221
# ............

# Input:
# The first line of input is the number of test cases .  Then T test cases follow . The first line of each test case is an integer N.

# Output:
# For each test case print the required nth row of the pattern.

# Expected Time Complexity : O(N2)
# Expected Auxilliary Space : O(1)

# Constraints:
# 1<=T<=20
# 1<=N<=20

# Example:
# Input:
# 2
# 2
# 3
# Output:
# 11
# 21



if __name__ == '__main__':
    ans_l = [None]*5
    ans_l[0] = '1'
    
    for i in range(1, 5):
        w = ans_l[i-1]
        k = 0
        tmp = ''
        last_char=''
        count=0
        for j in range(len(w)):
           
            if w[j] == last_char:
                count +=1
            elif last_char == '':
                count +=1  
            else:
                tmp = tmp + str(count) + last_char
                count = 1
                 
            last_char = w[j]
        tmp = tmp + str(count) + w[j] 
            

        ans_l[i] = tmp

        print(tmp)

    # cases = int(input())
    # for _ in range(cases):
    #     n = int(input())
        
    #     print(ans_l[n-1])