def max_semi_consecutive_days(days) -> int:
    
    c=[0]*2
    x=0
    
    
    for i in range(len(days)):
        if days[i]==True:
            x += 1 
        else:
            
            if i == len(days)-1:
                x=0
                break

            if days[i+1] == 0:
                c[0]=c[1]=0
                x=0
            if (x + c[1]) > (c[0]+c[1]):
                c[0] = c[1]
                c[1] = x
                
            x = 0
    
    c[0]= c[1]
    c[1]= x
    print(c) 
    return (c[0]+c[1])
    

print(max_semi_consecutive_days([1,0,0,1])) 