import re
from word2num import Word2Num
w2n = Word2Num(fuzzy_threshold=100)


def parseLine1(line):
    nums = re.findall(r'\d{1}', line)
    count = len(nums)

    digit_1 = 0
    digit_2 = 0
    if count>0:
        digit_1 = nums[0]
    
    if count==1:
        digit_2 = nums[0]
    else:
        digit_2 = nums [count-1]
    
    num = int(str(digit_1)+str(digit_2))
    return num

def findFirstNumStr(line):
    word = ""

    for idx,start in enumerate(line[:-2]):
        word = ""
        word = start
    
        for x in line[idx+1:]:
            word=word+x
            if(len(word)<3 or  word =='teen'):
                continue
            else:
                val = None
                val = w2n.parse(word)
            if (val != None and val != 0.5 and val != 0.125):
                
                print("first word: "+word + " value: "+str(val))
                val = str(int(val))
                if len(val) > 1:
                    val = val[-1:]
                return val
    return None
def findLastNumStr(line):
    line = line[::-1]
    word = ""
    for idx,end in enumerate(line[:-2]):
        word = ""
        word = end
    
        for x in line[idx+1:]:
            word=x+word
            if(len(word)<3 or word == 'teen'):
                continue
            else:
                val = None
                val = w2n.parse(word)
            if (val != None and val != 0.5 and val != 0.125):
                print("Last word: "+word + " value: "+str(val))
                val = str(int(val))
                if len(val) > 1:
                    val = val[-1:]
                return val
    return None
def parseLine(line):
    nums = re.findall(r'\d{1}', line)
    count = len(nums)
    line_len = len(line)
    num_1 = None
    num_2 = None
    
    digit_1 = 0
    index_1 = None
    digit_2 = 0
    index_2 = None
    if count>0:
        digit_1 = nums[0]
        index_1 = line.find(digit_1)
        if count==1:
            digit_2 = nums[0]
        else:
            digit_2 = nums[count-1]
        index_2 = line.rfind(digit_2)
        if(index_1 < 3):
            num_1 = digit_1
        if(line_len - index_2 < 3):
            num_2 = digit_2
        if(num_1 == None):
            preStr = line[0:index_1]
            res1 = findFirstNumStr(preStr)
            if(res1!=None):
                num_1 = res1
            else:
                num_1=digit_1
        if(num_2 == None):
            postStr = line[index_2+1:]
            res = findLastNumStr(postStr)
            if(res!=None):
                num_2 = res
            else:
                num_2=digit_2
    else:
        num_1 = findFirstNumStr(line)
        num_2 = findLastNumStr(line)

    num = int(str(num_1)+str(num_2))
    return num
        
def day1(f):
    sum = 0
    for line in f:
        line = line.strip()
        num = parseLine(line)
        sum = sum+num
      
    
    print(sum)

            

