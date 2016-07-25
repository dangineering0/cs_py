import sys
# @input: list of list of tuple
# @return: list of tuple of free time
# TODO: WALK THROUGH OWN MINI EXAMPLE

def findTime(nums):
    # assume input is good

    # TODO keep vars less than 5 chars
    masterList = []

    temp =[]
    for lst in nums:
        masterList.extend(lst)

    # TODO sorted takes key as "key = lambda x : output
    sorted(masterList,key=lambda x:x[0])

    # TODO put res up top
    res = []


    first = masterList[0]

    # TODO x, y = tuple

    curX, curMaxY = first

    for second in masterList[1:]:

        if curMaxY < second[0]:
            #different x so we write to res
            res.append((curX, curMaxY))
            curX, curMaxY = second

        else:
            curMaxY = max(second[1], curMaxY)

    res.append((curX, curMaxY))

    return intersection(res)

# @ return lst of free times
def intersection(lst):
    res = []
    lastX, lastY = lst[0]

    if lastX > 0:
        res.append((0, lastX))

    for x in lst[1:]:
        res.append((lastY, x[0]))
        lastY = x[0]

    res.append((lastY, sys.maxsize))
    return res


print(findTime([[(1,4)], [(2,5)], [(10,20)]]))