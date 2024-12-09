### Grab the txt file of the numbers
inputFile = open('AOC-02.txt')
### Reads the lines and makes input equal to it
input = inputFile.readlines()
mainList = []
succeses = 0
for i in input:
    line=i.strip()
    mainList.append(line)
#print(mainList)

def test(testCase):
    runs = 0
    thing = 0
    success = 0
    for t in testCase:
        if (t - testCase[(runs-1)]) >= 1 and (t - testCase[(runs-1)]) <= 3:
            thing += 1
        elif (t - testCase[(runs-1)]) <= -1 and (t - testCase[(runs-1)]) >= -3:
            thing -= 1    
        runs+=1
    if abs(thing) == (runs-1):
        success+=1    
    elif success == 0:
        toggle=False
        for i,j in enumerate(testCase):
            copyOfCase = testCase.copy()
            del copyOfCase[i] 
            runs = 0
            thing = 0

        
            for i, f in enumerate(copyOfCase):
                if (f - copyOfCase[(runs-1)]) >= 1 and (f - copyOfCase[(runs-1)]) <= 3 and i != 0:
                    thing += 1
                elif (f - copyOfCase[(runs-1)]) <= -1 and (f - copyOfCase[(runs-1)]) >= -3 and i != 0:
                    thing -= 1    
                runs+=1
            if abs(thing) == (runs-1) and toggle == False:
                success+=1    
                toggle = True
        if success ==0:
            print(testCase)
            

    return success

for i in mainList:
    testCase=i.split()
    testCase = [int(_) for _ in testCase]
    succeses += test(testCase)
    
    #print(testCase)
    
print(succeses)    



        

