class Solution(object):
    def moveZeroes(self, nums):
        zeroCount = 0
        insertZeroIndx = 0
        nonZeroIndx = 0

        # find the first non zero index
        #
        for x,i in iter(nums):

            if x != 0:
                break

        nonZeroIndx = i




Solution().moveZeroes([1,2,3])

