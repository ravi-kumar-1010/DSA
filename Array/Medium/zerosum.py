'''

Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, 2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

'''

def sum_range(nums,i,j):
    sum = 0
    for i in range(i,j):
        print("adding: ",nums[i])
        sum+=nums[i]
        if sum == 0:
            return True
    
    return False

def hasZeroSumSubarray(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            print(i,j)
            if sum_range(nums,i,j):
                return True
    return False


print(hasZeroSumSubarray([1,-1]))
