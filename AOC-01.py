### Grab the txt file of the numbers
inputFile = open('AOC-01.txt')
### Reads the lines and makes input equal to it
input = inputFile.readlines()
### creates the lists
listL=[]
listR=[]
listDiff=[]
simmilarityQ = 0
### Removes junk and splist it into two columns
for i in input:
    (item1,item2)=i.strip().split()
    listL.append(int(item1))
    listR.append(int(item2))
### sorts the lists
listL.sort()
listR.sort()
### checks if item in list l is equal to every item in list r then adds iteml * itemrcount to the similarity quotient
for i in listL:
    repeat= 0
    v = 0
    for l in listR:
        if i == listR[v]:
            repeat+=1
        v+=1
    simmilarityQ+= (repeat*i)

### recombines the lists
listsTogether= zip(listL,listR)
###print(list(listsTogether))
### subtracts the two columns
for i in listsTogether:
    listDiff.append(abs(i[0] - i[1]))
####### gives you the answer
print(sum(listDiff))
print(f'similarity = {simmilarityQ}')