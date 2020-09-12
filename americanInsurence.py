def occur(S):

    o = ''
    c=0
    for i in S:
        if i not in o:
            c = S.count(i)
            o = o + i + str(c)
            
    return o

print(occur('occurrences'))