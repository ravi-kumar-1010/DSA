import sys
class Solution:
    def findMaxSubarraySum(self,nums):
        maxsum = -sys.maxsize
        current_sum  = 0
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            current_sum = max(current_sum, nums[i])
            maxsum = max(maxsum, current_sum)
        return maxsum
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))
    # print(s.findMaxSubarraySum([-2,-1,-3,-4,-1,-2,-1,-5,-4]))