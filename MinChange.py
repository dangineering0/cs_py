def minChange2(denoms, target):
    res = []
    minChange(0, denoms, target, [], res)
    return res


def minChange(index, denoms, target, numsSoFar, res):

    if (target< 0):
        return 0

    if (target == 0):
        res.append(numsSoFar)
        return

    k = 0
    for x in range(index, len(denoms)):
        n = list(numsSoFar)
        n.append(denoms[x])
        minChange(x, denoms, target - denoms[x], n, res)




print(minChange2([10,5,1], 10))