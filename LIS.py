class Solution(object):
    #@param list of int nums
    #@return num of longest increasing sub
    def lengthOfLIS(self, nums):
        ans = 0
        indegrees = {}

        for n in nums:
            indegrees[n] = []

        for i in range(len(nums)-1, 0, -1):
            x = nums[i]
            for j in range(i-1, -1, -1):
                curNum = nums[j]
                if curNum < x:
                    indegrees[x].append(j)


        dp = [1]*len(nums)

        for pos,k in enumerate(nums):
            ind = indegrees[k]
            tempMax = 0
            for incoming in ind:
                indOf = dp[incoming]
                tempMax = max(indOf,tempMax)

            dp[pos] = tempMax + 1
            ans = max(ans, dp[pos])

        return ans


print Solution().lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])