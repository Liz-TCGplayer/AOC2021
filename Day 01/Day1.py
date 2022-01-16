with open('inputday01.txt') as f:
    lines = f.read().splitlines()
print(lines)

linecount = len(lines)
print(linecount)

varcount = 0
for i in range (1, linecount) : 
    if int(lines[i]) > int(lines[i-1]):
        varcount= varcount+1
    #print(i, lines[i], lines[i-1], varcount)
print (varcount)
