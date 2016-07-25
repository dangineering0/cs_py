def stringPerms(s):

    res = [""]

    for curIndx in range(len(s)):

        curLetter = s[curIndx]

        tempLst = []
        for string in res:
            for k in range(len(string)+1):
                if (string[:k] + curLetter + string[k:]) not in tempLst:
                    tempLst.append(string[:k] + curLetter + string[k:])
        res = tempLst

    return res


print(stringPerms("aaa"))
