class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if (len(s) == 0): return False
        return self.helper(s, 0, wordDict)

    def helper(self, s, index, wordDict):

        if (len(s) == 0):
            return True
        while(index < len(s)):
            if (s[0:index+1] in wordDict):
                res = self.helper(s[index+1:], 0, wordDict)
                if (res):
                    return True
            index += 1
        return False


print(Solution().wordBreak("kkkkk", ["kkk","kk"]))