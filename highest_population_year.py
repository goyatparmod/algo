def higest_population_year(a):
    h = {}
    for i in range(len(a[0])):
        if a[0][i] in h:
            h[a[0][i]]+=1
        else:
            h[a[0][i]]=1

        if a[1][i] in h:
            h[a[1][i]]-=1
        else:
            h[a[1][i]]=-1

    alive = 0
    maxAlive = 0
    theYear = ''
    for year in sorted(h):
        alive += h[year]
        if alive > maxAlive:
            maxAlive = alive
            theYear = year
    # return max(h.items(), key=operator.itemgetter(1))[0]
    return theYear,maxAlive





bb=['1945','1950','1950','1943','1937']
aa=['1999','1999','1980','2001','1987']
a=[bb,aa]
print(higest_population_year(a))
