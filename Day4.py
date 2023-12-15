import sys
import re

card_copies = {
    '1': 1
}

def parseLine2(card,line,copies):
    #print("Copies: "+str(copies),end=" ")
    line = line.strip().split("|")

    win_Nums = [int(numeric_string) for numeric_string in line[0].strip().split(" ")]
    card_nums = [int(numeric_string) for numeric_string in line[1].strip().split(" ")]

    matches = 0

    for num in card_nums:
        if(num in win_Nums):
            matches = matches + 1
    #print("Matches: "+str(matches))
    for i in range(card+1,card+matches+1):
        cardNum=str(i)
        if(not cardNum in card_copies):
            card_copies[cardNum] = 1
        card_copies[cardNum] = card_copies[cardNum] + copies

def parseLine1(line):
    line = line.strip().split("|")

    win_Nums = [int(numeric_string) for numeric_string in line[0].strip().split(" ")]
    card_nums = [int(numeric_string) for numeric_string in line[1].strip().split(" ")]

    matches = 0
    points = 0

    for num in card_nums:
        if(num in win_Nums):
            matches = matches + 1
    if(matches > 0):
        points = pow(2,matches-1)
    return points
        

def day4(f):
    sum = 0
    for line in f:
        line = line.strip().split(":")
        cardNum = re.findall(r'\d+',line[0])
        cardNum=cardNum[0]

        if(not cardNum in card_copies):
            card_copies[cardNum] = 1

        sum = sum + card_copies[cardNum]
        #print(line[0],end=" ")
        parseLine2(int(cardNum),line[1].replace("  "," "),card_copies[cardNum])
    
        
    print(str(sum))

            
