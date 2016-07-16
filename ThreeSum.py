class ThreeSum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums) # sorted RETURNS the list
        res = []

        for pos, v in enumerate(nums):
            j = pos+1
            k = len(nums) - 1

            while (j <= k):
                sum = (v + nums[j] + nums[k])
                if (sum == 0):
                    if ([v, nums[j], nums[k]] not in res):
                        res.append([v, nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif (sum > 0):
                    k -= 1
                else:
                    j+=1

        return res


print(ThreeSum().threeSum([-2,0,1,1,2]))