'''

Given a sorted integer array, find the floor and ceiling of a given number in it. For a given number x, floor(x) is the largest integer in the array less than or equal to x, and ceil(x) is the smallest integer in the array greater than or equal to x.

The solution should return the (floor, ceil) pair. If the floor or ceil doesn't exist, consider it to be -1.

Input: nums[] = [1, 4, 6, 8, 9], x = 2
Output: (1, 4)
Explanation: The floor is 1 and ceil is 4

Input: nums[] = [1, 4, 6, 8, 9], x = 6
Output: (6, 6)
Explanation: The floor is 6 and ceil is 6

Input: nums[] = [-2, 0, 1, 3], x = 4
Output: (3, -1)
Explanation: The floor is 3 and ceil doesn't exist

'''

def floorandceil(nums,x):
    if len(nums) == 0:
        return (-1,-1)
    if x in nums:
        return (x,x)
    if len(nums) == 1:
        if nums[0] < x:
            return (nums[0],-1)
        elif nums[0] > x:
            return (-1,nums[0])
    if x > nums[-1]:
        return (nums[-1],-1)
    if x < nums[0]:
        return (-1,nums[0])
    if len(nums) == 2 and x > nums[0] and x < nums[1]:
        return (nums[0],nums[1])
    for i in range(1,len(nums)):
        if x > nums[i-1] and x < nums[i]:
            return (nums[i-1],nums[i])


print(floorandceil([1, 4, 6, 8, 9],2))