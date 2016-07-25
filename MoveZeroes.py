class Solution(object):
    def moveZeroes(self, nums):

        lastZeroSeen = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[x], nums[lastZeroSeen] = nums[lastZeroSeen], nums[x]  # swap in python
                lastZeroSeen += 1
        return nums


print Solution().moveZeroes([1,0,3])

