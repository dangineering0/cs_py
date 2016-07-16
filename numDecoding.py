class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0
        return self.helper(0, s)

    def helper(self, index, s):

        resA = 0
        resB = 0

        if (index == len(s)):
            return 1
        elif (index > len(s)):
            return 0

        if (index <= len(s) - 2):
            two = s[index: index + 2]
            if (int(s[index]) != 0 and int(two) <= 26):
                resA = self.helper(index + 2, s)

        if (int(s[index]) > 0):
            resB = self.helper(index + 1, s)

        return resA + resB


print(Solution().numDecodings("121"))

