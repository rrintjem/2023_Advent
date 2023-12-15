import sys
import re
PRINTLINE = None

def getIndices(line):
    return [i for i, c in enumerate(line) if c == "*"]

def getPart(x,y,grid):
    line = grid[y]
    parts = re.findall(r'\d+',line)

    x_max = 0
    
    for num in parts:
        index = line.find(num,x_max)
        x_min = index if index == 0 else index-1
        x_max = index+(len(num))

        if(x >= x_min and x <= x_max-1):
            return int(num)
        
    print('Error, number not found for index ('+str(x)+','+str(y)+')')
    return 0

    
def parseLine2(grid,y,line):
    gears = getIndices(line)
    if(len(gears)==0):
        return 0
    sum = 0
    y_min = y if y==0 else y-1
    y_max = y if y == len(grid)-1 else y+1
    x_max = 0
    for x in gears:
        count_adj = 0
        valid = False
        ratio = 0
        coords = []
        x_min = x if x == 0 else x-1
        x_max = x if x == len(line)-1 else x+1

        for row in range(y_min,y_max+1):
            for col in range(x_min,x_max+1):
                data = grid[row][col]
                if(data.isnumeric()):
                    if (col > x_min):
                        if (not grid[row][col-1].isnumeric()):
                            count_adj = count_adj + 1
                            coords.append({'x':col,'y':row})
                    else:
                        count_adj = count_adj + 1
                        coords.append({'x':col,'y':row})
        if(count_adj == 2):
            valid = True
            parts = []
            for i in coords:
                parts.append(getPart(i['x'],i['y'],grid))
            ratio = parts[0]*parts[1]
        sum = sum + ratio


    return sum

def parseLine1(grid,y,line):
    parts = re.findall(r'\d+',line)
    if(len(parts)==0):
        return 0
    

    sum = 0
    y_min = y if y==0 else y-1
    y_max = y if y == len(grid)-1 else y+1

    x_max = 0
    
    for num in parts:
        valid = False
        index = line.find(num,x_max)
        x_min = index if index == 0 else index-1
        x_max = index+(len(num))
        if x_max == len(line):
           x_max = x_max-1
        
        
        if(y==PRINTLINE):print (num + ": y="+ str(y_min) +","+str(y_max))
        if(y==PRINTLINE):print ("x="+ str(x_min) +","+str(x_max))
        for row in range(y_min,y_max+1):
            for col in range(x_min,x_max+1):
                data = grid[row][col]
                if(y==PRINTLINE):print(data,end="")
                if(data == "." or data.isnumeric()):
                    continue
                else:
                    valid = True
                    break
            if(y==PRINTLINE):print("")
            
            if(valid):
              if(y==PRINTLINE):print(str(valid))
              break
        if(y==PRINTLINE):print(" ")
        if(valid):
            sum = sum + int(num)

    return sum    
        

def day3(f):
    f = f.readlines()
    sum = 0
    for i in range(0,len(f)):
        line = f[i].strip()
        res = parseLine2(f,i,line)
        sum = sum+res 
    
    print(sum)

            

