def getDifference(vals):
    diff_vals = []
    for i in range(len(vals)-1):
        currVal = vals[i]
        nextVal = vals[i+1]
        diff_vals.append(nextVal-currVal)
    distinct_diffs = set(diff_vals)
    if len(distinct_diffs)>1 or diff_vals[0] != 0:
        res = getDifference(diff_vals)
    else:
        return 0
    next_num =  diff_vals[0] - res
    return next_num
def getDifference1(vals):
    diff_vals = []
    for i in range(len(vals)-1):
        currVal = vals[i]
        nextVal = vals[i+1]
        diff_vals.append(nextVal-currVal)
    distinct_diffs = set(diff_vals)
    if len(distinct_diffs)>1 or diff_vals[0] != 0:
        res = getDifference(diff_vals)
    else:
        return 0
    next_num =  diff_vals[len(diff_vals)-1] + res
    return next_num
def day9(f):
    sum = 0
    for line in f:
        vals = [int(numeric_string) for numeric_string in line.strip().split(" ")]
        diff = getDifference(vals)
        next_num = vals[0]-diff
        sum = sum+next_num
        
        
    
    print(sum)