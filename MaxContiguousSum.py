def maxContiguousSum(nums):

    maxSum = 0
    runningSum  = 0

    for x in nums:
        runningSum += x

        if (runningSum < 0):
            runningSum = 0

        if (runningSum > maxSum):
            maxSum = runningSum



    return maxSum