
def day14(f):
    sum = 0
    f = f.readlines()
    load = {}
    points = {}
    row_count = len(f)
    total = 0

    for row,line in enumerate(f):
        f[row] = [char for char in line.strip()]
        load[row] = 0
        points[row] = row_count-row

        for col,c in enumerate(line):
            if c=='O':
                load[row] = load[row]+1
                
                if row > 0:
                    prev = row-1
                    curr = row
                    while (f[prev][col]=='.'):
                        f[prev][col]= 'O'
                        load[prev] = load[prev]+1
                        f[curr][col] = '.'
                        load[curr] = load[curr]-1
                        prev = prev - 1
                        curr = curr - 1
                        if prev < 0:
                            break
    
    for key,x in enumerate(f):
        print(''.join(x), end=' ') 
        print(f"{points[key]} x {load[key]}")
        total = load[key] * points[key]
        sum = sum+total
                    
    print(sum)
    #low 108779