

def pkgDependecy(d):

    result=[]
    visiting=set([])
    visited=set([])
    def dfs(n):
        if n in visited:
            return
        for ineighbor in d[n]:
            


    for n in d.keys():
        dfs(n)
    return result












mapping = {
    3:[],
    4:[]
}

print(pkgDependecy(mapping))