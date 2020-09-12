import random
def prt(n):
    
    matrix = [[random.randint(0,9) for x in range(n)] for y in range(n)] 
    matrix =[[10,11,12,13],[14,15,16,17],[18,19,20,21],[22,23,24,25]]

    prt_matrix(matrix)
    rotate(matrix)  
   
    prt_matrix(matrix)
    
     

def prt_matrix(mx):
    for mxx in mx:
        print(mxx)
           
def rotate(mat):
    N= len(mat) -1
    for x in range(0,int(len(mat)/2)):
        for y in range(x,N-x):
            # store current cell in temp variable 
            # x=0,y=1
            print('x=',x,'y=',y)
            temp = mat[x][y]

            mat[x][y] = mat[N-y][x]
            
            mat[N-y][x] = mat[N-x][N-y]
                    
            mat[N-x][N-y] =mat[y][N-x]
                                
            mat[y][N-x] = temp




            # temp = mat[x][y] 
  
            # # move values from right to top 
            # mat[x][y] = mat[y][N-1-x] 
  
            # # move values from bottom to right 
            # mat[y][N-1-x] = mat[N-1-x][N-1-y] 
  
            # # move values from left to bottom 
            # mat[N-1-x][N-1-y] = mat[N-1-y][x] 
  
            # # assign temp to left 
            # mat[N-1-y][x] = temp 
        

def isInvalid(m,r,c):
    return r<0 or c<0 or r>=len(m) or c>= len(m) or m[r][c] != 0



mm= prt(4)

# prt_matrix(mm)
        