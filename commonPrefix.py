def commonPrefixUtil(s1,s2):
    result=''
    l1,l2 = len(s1),len(s2)
    i,j=0,0
    while i <= l1-1 and j <= l2-1:
        if s1[i] != s2[j]:
            break

        result += s1[i]
        i,j= i+1,j+1
    return result 

if __name__ == '__main__':
    
    print(commonPrefixUtil('parmod','pardom'))