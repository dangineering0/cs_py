def genParens(n):

    res = []
    if (n == 0): return res
    helper(n, n, "", res)
    return res

def helper(leftP, rightP, sSoFar, res):
    if leftP < 0 or leftP > rightP:
        return

    if leftP == 0 and rightP == 0:
        res.append(sSoFar)

    else:
        helper(leftP-1, rightP, sSoFar+"(", res)
        helper(leftP, rightP - 1, sSoFar+")", res)



print(genParens(3))