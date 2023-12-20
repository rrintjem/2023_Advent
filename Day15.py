
def hash(str):
    val = 0
    for ch in str:
        val = val + ord(ch)
        val = (val*17)%256

    return val

def day15(f):
    f = f.read()
    steps = f.split(',')
    sum = 0

    for s in steps:
        val = hash(s)
        sum = sum+val
            
    print(sum)
