class HouseRobber(object):

    def rob(self, nums):

        prevMax = 0
        curMax = 0

        for x in nums:

            temp = curMax
            curMax = max(prevMax + x, curMax)
            prevMax = temp

        return curMax

print(HouseRobber().rob([5, 1, 2, 6, 20, 2]))