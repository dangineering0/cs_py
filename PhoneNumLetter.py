def letterComb(s):


    wmap = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
    res = []
    self.letterHelper(s, "", res, 0, wmap)
    return res



def letterHelper(s, sSoFar, res, index, wmap):

    if (index == len(s)):
        res.append(sSoFar)
        return

    curLetter = s[index]
    for c in wmap[curLetter]:
        self.letterHelper(s, sSoFar+c, res, index+1, wmap)



print(letterComb("23"))
