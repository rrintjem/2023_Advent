import re
import math

def getRaceTable(timeLim,record):
    winCount = 0
    for duration in range(timeLim):
        moveTime = timeLim - duration
        distance = duration*moveTime
        
        if distance > record:
            winCount = winCount + 1
    return winCount

def part1(f):
    f = f.readlines()
    race_times = [int(numeric_string) for numeric_string in re.findall(r'\d+',f[0])]
    record_distance = [int(numeric_string) for numeric_string in re.findall(r'\d+',f[1])]

    result = None

    for i in range(len(race_times)):
        wins = getRaceTable(race_times[i],record_distance[i])
        if result == None:
            result = wins
        else: 
            result = result * wins
    print(str(result))

def getZeros(a,b,c):
    #y = ax^2 + bx + c
    d = (b**2) - (4*a*c)

    # find two solutions
    z1 = (-b+math.sqrt(d))/(2*a)
    z2 = (-b-math.sqrt(d))/(2*a)

    return int(z1),int(z2)

def day6(f):
    f = f.readlines()
    move_time = int(f[0].strip().split(':')[1].replace(" ",""))
    record_distance = int(f[1].strip().split(':')[1].replace(" ",""))

    #y = ax^2 + bx + c
    a = -1
    b = move_time
    c = 0
  

    #get zeroes of the record time 
    z1,z2 = getZeros(1,(-1)*b,record_distance)
   
    
    result = (z2-z1) if (z2>z1) else (z1-z2)

    
    print(str(result))
    
    

