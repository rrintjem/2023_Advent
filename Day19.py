def parseParts(f):
    parts = []
    for line in f:
        line = line.strip().strip('{').strip('}')
        attributes = line.split(',')
        part = {}
        for a in attributes:
            a = a.split('=')
            part[a[0]] = int(a[1])
        parts.append(part)
    return parts

def parseRules(f):
    rules = {}
    for idx,line in enumerate(f):
        line = line.strip().strip('}').split('{')
        key = line[0]
        instructions = line[1].split(',')
        rule = [] 
        for i in instructions:
            r = {}
            if ":" in i:
                i = i.split(':')
                r["goto"] = i[1]
                i = i[0]
                r["var"] = i[0]
                r["comp"] = i[1]
                r["amt"] = int(i[2:])
            else:
                r["default"] = i
            rule.append(r)
        rules[key] = rule
    return rules

def checkPart(part,rules):
    pass_part = None
    rule = 'in'

    while pass_part == None:
        curr = rules[rule]
        for step in curr:
            #print(step)
            break_loop = False
            if "default" in step:
                rule = step['default']
                break_loop = True
            else:
                if step['comp'] == '>':
                    if part[step['var']] > step['amt']:
                        rule = step['goto']
                        break_loop = True
                else: #step['comp'] == '<'
                    if part[step['var']] < step['amt']:
                        rule = step['goto']
                        break_loop = True
            
            if (rule == 'A'):
                pass_part = True
                break
            elif (rule == 'R'):
                pass_part = False
                break
            elif break_loop:
                break

    return pass_part

def day19(f):
    sum = 0
    f = f.read()
    f = f.split('\n\n')
    rules = parseRules(f[0].split('\n'))
    parts = parseParts(f[1].split('\n'))

    pass_part = False

    for part in parts:
        total = 0
        #print(part)
        pass_part = checkPart(part,rules)
        #print(pass_part)
        if pass_part:
            for item in part.values():
                total = total + item
        sum = sum + total

    print(sum) 


        

    
    

    
