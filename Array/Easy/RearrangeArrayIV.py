'''

Given an array of positive and negative integers, segregate them in linear time and constant space. The output should contain all negative numbers, followed by all positive numbers.

Input : [9, -3, 5, -2, -8, -6, 1, 3]
Output: [-3, -2, -8, -6, 9, 5, 1, 3] or [-3, -2, -8, -6, 9, 5, 1, 3] or any other valid combination.

Input : [-4, -2, -7, -9]
Output: [-4, -2, -7, -9] or any other valid combination.

Input : [2, 4, 3, 1, 5]
Output: [2, 4, 3, 1, 5] or any other valid combination.

'''

def swap(nums,a,b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

class Solution:
    def rearrange(self, nums):
        pivot = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                swap(nums,i,pivot)
                pivot +=1
        return

if __name__ == "__main__":
    nums =  [9, -3, 5, -2, -8, -6, 1, 3]
    Solution().rearrange(nums)
    print(nums)