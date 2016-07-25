class Solution(object):
    # @return int
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        numMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '*': 0}

        s += '*'

        i = 0
        while i < len(s)-1:

            curNum = numMap[s[i]]
            nextNum = numMap[s[i + 1]]

            if nextNum > curNum:
                res += nextNum - curNum
                i += 2
            else:
                res += curNum
                i+= 1

        return res




print(Solution().romanToInt("MMXIV"))