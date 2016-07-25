class Solution(object):
    # @return str
    def intToRoman(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        numMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        curNum = s[0]







print(Solution().romanToInt("MMXIV"))