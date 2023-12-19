import math

def getIndices(arr,key,idx):
    matched_indexes = []

    for i in range(idx+1,len(arr)):
        if key == arr[i]:
            matched_indexes.append(i)
    matched_indexes.sort(reverse=True)
    return matched_indexes

def checkHorizontal(lines,reverse):
    res = 0
    if reverse:
        lines = lines[::-1] 
    res = getSymmetry(lines,reverse)    

    return res

def getSymmetry(lines,reverse):
    num = len(lines)
    start = lines[0]
    remaining = lines[1:num]
    if(start not in remaining):
        return 0
    indexes = getIndices(lines,start,0)
    
    symmetry = False
    for end in indexes:
        mirror = lines[0:end+1]
        l = math.ceil(len(mirror)/2)
        for r1 in range(l):
            
            r2 = end - r1
            if(r1 == r2):
                symmetry = False
                break
            if mirror[r1] != mirror[r2]:
                symmetry = False
                break
            else:
                symmetry = True
        if(symmetry):
            if reverse:
                res = num - 1 - r1
            else:
                res = r1+1
            return res
    return 0

def checkVertical(lines,reverse):
    #pivot array
    lines = [''.join(list(a)) for a in zip(*lines)]
    res = checkHorizontal(lines,reverse)
    return res


def day13(f):
    f = f.read()
    sum = 0
    patterns = f.split('\n\n')
    for p in patterns:
        add = 0
        lines = p.split('\n')
        rows = 100*checkHorizontal(lines,True)
        cols = checkVertical(lines,True)
        
        r_rows = 100*checkHorizontal(lines,False)
        r_cols = checkVertical(lines,False)

        add = max(rows,cols,r_rows,r_cols)
        #print(f"rows:{rows},{r_rows} cols:{cols},{r_cols} =  {add}")
        sum = sum+add   

    print(sum)