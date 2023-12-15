from multiprocessing import Pool

def splitNodes(line):
    node_id = None
    startNode = False
    node = {
        "L":None,
        "R":None
    }

    line = line.strip().split("=")
    node_id = line[0].strip()
    if(node_id[2]=='A'):
        startNode = True

    line = line[1].strip().split(",")
    
    node["L"] = line[0].strip().replace("(","")
    node["R"] = line[1].strip().replace(")","")
    return node_id,startNode ,node

def traverse1(nodes,pattern):
    steps = 0
    activeNode = 'AAA'
    while(activeNode != 'ZZZ'):
        for direction in pattern:
            if(activeNode == 'ZZZ'):
                break
            else:
                curr = nodes[activeNode]
                next = nodes[curr[direction]]
                activeNode = curr[direction]
                steps = steps+1
    return steps

def traverse(nodes,pattern,startNode):
    steps = 0
    activeNode = startNode
    while(activeNode[2] != 'Z'):
        for direction in pattern:
            if(activeNode[2] == 'Z' or activeNode[2] == 'A'):
                break
            else:
                curr = nodes[activeNode]
                next = nodes[curr[direction]]
                activeNode = curr[direction]
                steps = steps+1
    return steps

def day8(f):
    sections = f.read().split("\n\n")
    pattern = [char for char in sections[0].strip()]
    lines = sections[1].strip().split("\n")
    startNodes = {}
    nodes = {}
    startNodeIds = []
    
    for line in lines:
        node_id,isStartNode,node = splitNodes(line)
        if(isStartNode):
            startNodeIds.append(node_id)
            startNodes[node_id] = node
        nodes[node_id] = node
    for start_id in startNodeIds:
        end,result = traverse(nodes,pattern,start_id)
        #startNodes[start_id]=
    print(result)
  


    
    
    

