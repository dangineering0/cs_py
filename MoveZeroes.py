class Solution(object):
    def moveZeroes(self, nums):

        lastZero = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[x], nums[lastZero] = nums[lastZero], nums[x]  # swap in python
                lastZero += 1
        return nums


Solution().moveZeroes([1,0,3])

