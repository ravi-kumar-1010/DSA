'''

Given an integer array, find the maximum length contiguous subarray having a given sum.

Input : nums[] = [5, 6, -5, 5, 3, 5, 3, -2, 0], target = 8
Output: [-5, 5, 3, 5]
Explanation: The subarrays with sum 8 are [[-5, 5, 3, 5], [3, 5], [5, 3]]. The longest subarray is [-5, 5, 3, 5] having length 4.

Note: Since an input can contain several maximum length subarrays with given sum, the solution should return any one of the maximum length subarray.

'''

def findMaxLenSubarray(nums,target):
    
    return