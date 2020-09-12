def prt(n):
    
    matrix = [[0 for x in range(n)] for y in range(n)] 
    # c=[0]*n 
    # r=[c]*n

    r=0
    c=0
    x=n
    dc=[1,0,-1,0]
    dr=[0,1,0,-1]
    x = 0 
    limit = n*n
    i=1

    while i < limit:
        matrix[r][c] = i
        r += dr[x];
        c += dc[x];
        if (isInvalid(matrix,r, c)):
            print('invalid',matrix)
            r-= dr[x]
            c-=dc[x]
            x = (x+1)%4
            r+= dr[x]
            c+= dc[x]
        i += 1
    return matrix
           
def isInvalid(m,r,c):
    return r<0 or c<0 or r>=len(m) or c>= len(m) or m[r][c] != 0



mm= prt(5)

for mmm in mm:
    print(mmm)
        
        
        


