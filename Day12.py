import re
from math import comb
from itertools import combinations 


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch], s.count(ch)

def getArrangements(row,groups,pattern):
    res = 0
    indexes,n = find(row,'?')
    #row =list(filter(None, row.split('.')))
    r = sum(groups) - row.count('#')

    #opts = comb(n,r)
    combos = list(combinations(indexes,r))

    for c in combos:
        temp = [char for char in row]
        for i in c:
            temp[i] = '#'
        reg = re.search(pattern,''.join(temp))
  
        if(reg):
            res = res+1
    return res


def splitRow(line):
    row = line.strip().split(" ")[0]
    groups =  [int(numeric_string) for numeric_string in (line.strip().split(" ")[1].split(','))]


    for i in range(0,4):
        row=row+row
        groups = groups+groups

    pattern = r"[\.?]*"

    for idx,g in enumerate(groups):
        if idx > 0:
            pattern = pattern +r"+"
        p = r"#{"+str(g)+r"}[\.?]"
        pattern = pattern+p
    pattern = pattern +r"*"
    return row,groups,pattern

def day12(f):
    sum = 0
    for line in f:
        row,groups,pattern = splitRow(line)
        arr = getArrangements(row,groups,pattern)
        sum = sum+arr
    print(sum)