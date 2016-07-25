class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #
        if maxWidth == 0:
            return words
        if words == [""]:
            return [" " * maxWidth]

        ans = []
        curCount = 0
        curWord = ""
        for word in words:

            if curCount == 0:
                #we know first word has to fit
                curWord = word
                curCount = len(word)

            else:

                if curCount + 1 + len(word) > maxWidth:
                    ans.append(curWord)
                    curWord = word
                    curCount = len(word)
                else:
                    curWord += " " + word
                    curCount += len(word) + 1

        if len(curWord) != 0:
            ans.append(curWord)
        res = []
        for pos, word in enumerate(ans):
            if pos == len(ans) - 1:
                res.append(self.expandSpaces(word, maxWidth, True))
            else:
                res.append(self.expandSpaces(word, maxWidth, False))

        return res

    def expandSpaces(self, s, limit, lastLine):

        # find space indices
        if (len(s) == limit):
            return s

        spaces = []
        for pos, c in enumerate(list(s)):
            if (c == ' '):
                spaces.append(pos)
        curCount = len(s)
        i = 0

        while (curCount < limit):
            if (lastLine):
                index = len(s)
                s += " "
                curCount += 1

            else:
                if (len(spaces) == 0):
                    index = len(s)
                else:
                    bottom = i % (len(spaces))
                    if bottom != 0:
                        index = spaces[bottom] + i
                    else:
                        index = spaces[bottom]
                    i += 1

                s = s[:index] + ' ' + s[index:]

                curCount += 1

        return s

print(Solution().fullJustify(["Here","is","an","example","of","text","justification."], 14))