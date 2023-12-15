import sys
import re

CUBE_COLS = {
    'red':12,
    'green':13,
    'blue':14
}

def parseLine2(line):
    hands = line.strip().split(";")

    min_cubes = {
        'red':0,
        'green':0,
        'blue':0
    }

    for hand in hands:
        cubes = hand.strip().split(",")
        for x in cubes:
            x = x.strip().split(" ")
            count = int(x[0])
            colour = x[1]
        
            if min_cubes[colour] < count:
                min_cubes[colour] = count
    return (min_cubes['red']*min_cubes['green']*min_cubes['blue'])

def parseLine1(line):
    hands = line.strip().split(";")

    for hand in hands:
        cubes = hand.strip().split(",")
        for x in cubes:
            x = x.strip().split(" ")
            count = int(x[0])
            colour = x[1]
        
            if CUBE_COLS[colour] < count:
                return False
    return True

def day2(f):

    sum = 0
    for line in f:
        line = line.strip().split(":")
        res = parseLine2(line[1])
        sum = sum+res 
    
    print(sum)

            