def lookAndSay(max):
    x=1
    print(x)
    for i in range(max):
        x=nextVal(x)
        print(x)

def nextVal(h):
    c = str(h)
    p=c[0]
    pp=1
    j = 0
    k = ''
    if len(c) > 1:
        for j in range(1,len(c)):
            if c[j] != p:
                k += str(pp) + p
                pp = 1
                
            else:
                p = c[j]
                pp += 1
            p=c[j]
    k += str(pp) + p
    return int(k)


lookAndSay(5)
