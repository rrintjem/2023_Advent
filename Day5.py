import sys
import re

SEEDS = []
MAPPINGS = {}
class Seed:
    '''
    start_id
    end_id
    length
    '''
    def __init__(self, start_id,length):
        self.start_id = start_id
        self.end_id = start_id + length - 1
        self.length = length
    
    def getLocation(self):
        srcTitle = "seed"
        index = self.id
        while (srcTitle!="location"):
            resTitle = getNextMapping(srcTitle)
            index = getMapping(index,srcTitle,resTitle)
            srcTitle = resTitle
        return index
    
    def inSeedRange(self,index):
        res = False
        if(index >= self.start_id and index <= self.end_id):
            res = True
        return res

    pass

class Mappings:
    '''
    title
    source
    destination
    ranges {Map_Ranges}
    '''
    def __init__(self, title):
        self.title = title
        temp = title.replace(" map","").replace("to","").split("--")
        self.source = temp[0]
        self.destination = temp[1]
        self.ranges = []

    def setRanges(self,data):
        for line in data:
            line = [int(numeric_string) for numeric_string in line.strip().split(" ")]
            self.ranges.append(Map_Range(line[1],line[0],line[2]))
    
    def findDest(self, index):
        res = index
        for r in self.ranges:
            if(index >= r.src_start and index <= r.src_end):
                res = r.getDest(index)
                break
        return res 
    
    def findSrc(self,index):
        res = index
        for r in self.ranges:
            if(index >= r.dest_start and index <= r.dest_end):
                res = r.getSrc(index)
                break
        return res 

    pass

class Map_Range:
    '''
    src_start
    src_end
    dest_start
    dest_end
    length
    '''
    def __init__(self, src_start, dest_start, length):
        self.src_start = src_start
        self.dest_start = dest_start
        
        self.src_end = src_start+length-1
        self.dest_end = dest_start+length-1
        
        self.length = length
    
    def getDest(self,index):
        diff = index - self.src_start
        return self.dest_start + diff
    def getSrc(self,index):
        diff = index - self.dest_start
        return self.src_start + diff

    pass

def getMapping(index,src,dest):
    key = src+"-to-"+dest+" map"
    m = MAPPINGS[key]
    return m.findDest(index)

def getPrevMapping(dest):
    for key in MAPPINGS.keys():
        m = MAPPINGS[key]
        if m.destination == dest :
            return m.source
    return None

def getNextMapping(src):
    for key in MAPPINGS.keys():
        m = MAPPINGS[key]
        if m.source == src :
            return m.destination
    return None

def getSeedNums(line):
    data = [int(numeric_string) for numeric_string in line.strip().split(" ")]
    start = None

    for i in range(len(data)):
        val = data[i]
        if i%2 == 0:
            start = val
        else:
            SEEDS.append(Seed(start,val))

def backMap(index,src,dest):
    key = src+"-to-"+dest+" map"
    m = MAPPINGS[key]
    return m.findSrc(index)

def getLowestLocation(index):
    resTitle = "location"
    while (resTitle!="seed"):
        srcTitle = getPrevMapping(resTitle)
        index = backMap(index,srcTitle,resTitle)
        resTitle = srcTitle
    return index

def day5(f):
    sections = f.read().split("\n\n")
    lowest = None

    for sect in sections:
        sect = sect.strip().split(":")
        heading = sect[0].strip()
        lines=sect[1].strip().split("\n")
        
        if(heading == 'seeds'):
            getSeedNums(lines[0])
        else:
            MAPPINGS[heading] = Mappings(heading)
            MAPPINGS[heading].setRanges(lines)
    index = 0
    while(lowest == None):
        seed = getLowestLocation(index)
        for s in SEEDS:
            if s.inSeedRange(seed):
                lowest = index
                break
        index = index+1


    print(str(lowest))
            

