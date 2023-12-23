
def hash(str):
    val = 0
    for ch in str:
        val = val + ord(ch)
        val = (val*17)%256

    return val

def splitStep(step):
    if ('-' in step):
        step = step.split('-')
        operation = '-'
    else:
        step = step.split('=')
        operation = '='
    return step[0],step[1],operation

def removeLens(box,label):
    #box = {label:lens}
    if(label in box):
        del box[label]
    return box

def addLens(box,label,lens):
    box[label] = lens
    return box

def calcPower(box,id):
    sum = 0
    id = id+1

    for idx,label in enumerate(box):
        lens = box[label]
        slot= idx+1
        val = id*slot*int(lens)
        sum = sum+val
    return sum



def day15(f):
    f = f.read()
    steps = f.split(',')
    sum = 0
    boxes = {}

    for s in steps:
        label,lens, operation = splitStep(s)
        box = hash(label)
   
        if operation == '-' and box in boxes:
            #remove
            boxes[box] = removeLens(boxes[box],label)
            if len(boxes[box]) == 0:
                del boxes[box]
        elif operation == '=':
            #add
            if box in boxes:
                boxes[box] = addLens(boxes[box],label,lens)
            else:
                boxes[box] = {label:lens}
    #print(boxes)
    for x in boxes.keys():
        val = calcPower(boxes[x],x)
        sum = sum+val
    print(sum)
