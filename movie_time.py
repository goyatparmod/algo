def clac_time(t):
    t.sort(key=lambda x:x[0])
    merged = []
    mv_time = 0

    for higher in t:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
                mv_time = upper_bound - lower[0]
            else:
                merged.append(higher)
                mv_time += higer[1] - higher[0]
    return merged,mv_time

            
if __name__ == "__main__":
    print(clac_time([(0,3),(4,5),(3,10),(9,16),(15,25),(5,8)]))