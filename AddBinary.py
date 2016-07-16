class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aLen = len(a) - 1
        bLen = len(b) - 1

        carryOver = 0
        res = ""
        while (aLen >= 0 or bLen >= 0):
            aChar = 0
            bChar = 0
            if (aLen >= 0):
                aChar = int(a[aLen])
            if (bLen >= 0):
                bChar = int(b[bLen])

            sum = aChar + bChar + carryOver
            if sum >= 2:
                carryOver = 1
                sum = sum % 2
            else:
                carryOver = 0

            res = str(sum) + res
            aLen -= 1
            bLen -= 1

        if (carryOver):
            res = str(1) + res
        return res


print(Solution().addBinary("11", "1"))