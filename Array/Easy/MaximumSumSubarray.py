import sys
class Solution:
    def findMaxSubarraySum(self,nums):
        maxsum = -9999999999
        current_sum  = 0
        for i in range(len(nums)):
            current_sum = nums[i]
            for j in range(i,len(nums)):
                if j>i:
                    current_sum += nums[j]
                if current_sum > maxsum:
                    maxsum = current_sum
            current_sum = 0
        return maxsum
if __name__ == "__main__":
    s = Solution()
    # print(s.findMaxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.findMaxSubarraySum([-2,-1,-3,-4,-1,-2,-1,-5,-4]))
