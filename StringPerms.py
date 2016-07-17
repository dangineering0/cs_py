def stringPerms(s):

    res = [""]

    for curIndx in range(len(s)):

        curLetter = s[curIndx]

        tempLst = []
        for string in res:
            for k in range(len(string)+1):
                tempLst.append(string[:k] + curLetter + string[k:])
        res = tempLst

    return res


print(stringPerms("abc"))


t = "cba"

print(sorted(t))