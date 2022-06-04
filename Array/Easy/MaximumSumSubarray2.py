import sys
class Solution:
    def findMaxSubarraySum(self,nums):
        maximum = max(nums)
        if maximum < 0:
            return maximum
        max_so_far = 0
        max_ending_here = 0
        for i in nums:
            max_ending_here = max_ending_here + i
            max_ending_here = max(max_ending_here, 0)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
if __name__ == "__main__":
    s = Solution()
    # print(s.findMaxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.findMaxSubarraySum([-2,-1,-3,-4,-1,-2,-1,-5,-4]))
