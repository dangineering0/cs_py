def genParens(n):

    if (n == 0):
        return []

    res = []
    helper("", 0, res, n)

    return res


def helper(sSoFar, index, res, n):
    if (index == n*2):
        res.append(sSoFar)
        return
    helper(sSoFar+"(", index+1, res, n)
    helper(sSoFar+")", index+1, res, n)



def isValid(parens):

    stack = []

    for char in list(parens):

        if (char == "("):
            stack.append(char)
        else:
            if (not stack):
                return False
            if stack.pop() != "(":
                return False
    if stack:
        return False
    return True

l = genParens(1)
k = []
for x in l:
    if (isValid(x)):
        k.append(x)

print(list(filter(isValid, genParens(1))))