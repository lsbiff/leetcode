class Solution:
    def maxSubArray(self, nums) -> int:
        
        curSum = nums[0]
        maxSum = curSum

        for i in range(1, len(nums)):

            if curSum >= 0:

                curSum =  curSum + nums[i]

            else:
                curSum = nums[i]

            if curSum > maxSum:
                maxSum = curSum

        return maxSum


tests = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8], [1,2,3,4,-109, 100], [100,2,3,4,-109, 1], [1,2], [1,2,3,-2,5, 9, -10, 25, -30, 200, -5]]

for tst in tests:
    print(f'{Solution.maxSubArray(None, tst)}')