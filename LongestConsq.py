class Solution(object):

    # @param list of ints unsorted
    # @return int of length of longest conseq seq.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = 0
        #
        # visited = {}
        #
        # #preprocess
        # for n in nums:
        #     visited[n] = False
        # tempAns = 0
        #
        # for n in nums:
        #     low = n -1
        #     high = n +1
        #     visited[n] = True
        #     tempAns += 1
        #     if low in visited and not visited[low]:
        #         tempAns += 1
        #         visited[low] = True
        #     if high in visited and not visited[high]:
        #         visited[high] = True
        #         tempAns+=1
        #
        #     if low not in visited and high not in visited:
        #         ans = max(ans, tempAns)
        #         tempAns = 0

        s = set(nums)
        ans = 0

        while s:
            tempAns = 1
            x = s.pop()

            i = x - 1
            while i in s:
                tempAns+=1
                s.remove(i)
                i-=1

            j = x + 1
            while j in s:
                tempAns+=1
                s.remove(j)
                j+=1

            ans = max(tempAns, ans)

        return ans




print Solution().longestConsecutive([100, 1, 3, 2])