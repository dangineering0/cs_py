
#@param list of int tuples birth and death
#@return int of the year w/ most people alive
def living_people(bAndD):

    births = []
    deaths = []

    for x in sorted(bAndD, key=lambda x:x[0]):
        births.append(x[0])

    for y in sorted(bAndD, key=lambda x:x[1]):
        deaths.append(y[1])

    maxCount = 0
    bIndx = 0
    dIndx = 0
    curAlive=0
    year = 0

    while bIndx < len(births):

        if births[bIndx] < deaths[dIndx]:
            curAlive+=1

            if curAlive > maxCount:
                maxCount = curAlive
                year = births[bIndx]
            bIndx+=1
        else:
            curAlive-=1
            dIndx+=1

    return year





print living_people([(0,10), (2,5), (3,4)])